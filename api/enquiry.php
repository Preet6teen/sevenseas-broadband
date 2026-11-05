<?php
/**
 * Sevenseas Broadband — Production Lead Generation & Enquiry API Handler (Hostinger / Apache + PHP)
 * Validates lead submissions, verifies Turnstile, prevents spam, and stores leads securely.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=UTF-8');
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: SAMEORIGIN');

// Allow CORS if needed
$origin = $_SERVER['HTTP_ORIGIN'] ?? '*';
header("Access-Control-Allow-Origin: $origin");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method Not Allowed']);
    exit;
}

// 1. Rate Limiting Check (Max 5 requests per 15 minutes per IP)
$ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1';
$ipHash = substr(md5($ip), 0, 16);
$rateLimitDir = __DIR__ . '/../data/ratelimit';
if (!is_dir($rateLimitDir)) {
    @mkdir($rateLimitDir, 0750, true);
}
$rateFile = $rateLimitDir . '/' . $ipHash . '.json';
$now = time();

if (file_exists($rateFile)) {
    $rateData = @json_decode(file_get_contents($rateFile), true);
    if ($rateData && isset($rateData['resetTime']) && $now < $rateData['resetTime']) {
        if ($rateData['count'] >= 5) {
            http_response_code(429);
            echo json_encode([
                'success' => false,
                'message' => 'Too many requests. Please try again after 15 minutes or call us directly at 9664985535.'
            ]);
            exit;
        }
        $rateData['count']++;
    } else {
        $rateData = ['count' => 1, 'resetTime' => $now + 900];
    }
} else {
    $rateData = ['count' => 1, 'resetTime' => $now + 900];
}
@file_put_contents($rateFile, json_encode($rateData), LOCK_EX);

// 2. Parse JSON Payload
$rawInput = file_get_contents('php://input');
$data = json_decode($rawInput, true);

if (!is_array($data)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Invalid JSON input.']);
    exit;
}

// 3. Honeypot Check (b_website must be empty)
if (!empty($data['b_website'])) {
    // Silent drop to fool spambots
    echo json_encode(['success' => true, 'leadId' => 'SSB-' . rand(100000, 999999)]);
    exit;
}

// 4. Sanitize and Validate Fields
$fullName = trim((string)($data['fullName'] ?? ''));
$mobileNumber = trim((string)($data['mobileNumber'] ?? ''));
$areaLocality = trim((string)($data['areaLocality'] ?? ''));
$societyBuilding = trim((string)($data['societyBuilding'] ?? ''));
$preferredPlan = trim((string)($data['preferredPlan'] ?? 'Popular 200 Mbps'));
$consent = !empty($data['consent']);
$turnstileToken = (string)($data['turnstileToken'] ?? '');

// Validation Rules
$errors = [];

if (mb_strlen($fullName) < 2 || mb_strlen($fullName) > 80) {
    $errors[] = 'Full name must be between 2 and 80 characters.';
}

if (!preg_match('/^[6-9]\d{9}$/', $mobileNumber)) {
    $errors[] = 'Please enter a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9.';
}

if (mb_strlen($areaLocality) < 2 || mb_strlen($areaLocality) > 100) {
    $errors[] = 'Area / Locality must be between 2 and 100 characters.';
}

if (!$consent) {
    $errors[] = 'Please grant consent to be contacted regarding your connection enquiry.';
}

if (!empty($errors)) {
    http_response_code(422);
    echo json_encode(['success' => false, 'message' => implode(' ', $errors), 'errors' => $errors]);
    exit;
}

// 5. Cloudflare Turnstile Verification (Optional / Configurable)
$turnstileSecret = getenv('CLOUDFLARE_TURNSTILE_SECRET_KEY') ?: '';
if (!empty($turnstileSecret) && !empty($turnstileToken)) {
    $verifyUrl = 'https://challenges.cloudflare.com/turnstile/v0/siteverify';
    $postData = http_build_query([
        'secret' => $turnstileSecret,
        'response' => $turnstileToken,
        'remoteip' => $ip
    ]);
    $ctx = stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
            'content' => $postData,
            'timeout' => 5
        ]
    ]);
    $res = @file_get_contents($verifyUrl, false, $ctx);
    if ($res) {
        $result = json_decode($res, true);
        if (empty($result['success'])) {
            http_response_code(403);
            echo json_encode(['success' => false, 'message' => 'Human verification failed. Please try again.']);
            exit;
        }
    }
}

// 6. Generate Lead Reference ID
$leadId = 'SSB-' . time() . '-' . rand(100, 999);

$leadRecord = [
    'leadId' => $leadId,
    'fullName' => $fullName,
    'mobileNumber' => $mobileNumber,
    'areaLocality' => $areaLocality,
    'societyBuilding' => $societyBuilding,
    'preferredPlan' => $preferredPlan,
    'ip' => $ip,
    'userAgent' => $_SERVER['HTTP_USER_AGENT'] ?? '',
    'createdAt' => date('Y-m-d H:i:s')
];

// 7. Store Lead Securely
$dataDir = __DIR__ . '/../data';
if (!is_dir($dataDir)) {
    @mkdir($dataDir, 0750, true);
}

// A. Append to JSON leads ledger
$leadsFile = $dataDir . '/leads.json';
$currentLeads = [];
if (file_exists($leadsFile)) {
    $currentLeads = @json_decode(file_get_contents($leadsFile), true) ?: [];
}
$currentLeads[] = $leadRecord;
@file_put_contents($leadsFile, json_encode($currentLeads, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), LOCK_EX);

// B. Save to SQLite database if PDO SQLite is available
try {
    $dbPath = $dataDir . '/leads.db';
    $db = new PDO('sqlite:' . $dbPath);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $db->exec("CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id TEXT UNIQUE,
        full_name TEXT,
        mobile_number TEXT,
        area_locality TEXT,
        society_building TEXT,
        preferred_plan TEXT,
        ip TEXT,
        created_at TEXT
    )");
    $stmt = $db->prepare("INSERT INTO leads (lead_id, full_name, mobile_number, area_locality, society_building, preferred_plan, ip, created_at)
        VALUES (:lead_id, :full_name, :mobile_number, :area_locality, :society_building, :preferred_plan, :ip, :created_at)");
    $stmt->execute([
        ':lead_id' => $leadId,
        ':full_name' => $fullName,
        ':mobile_number' => $mobileNumber,
        ':area_locality' => $areaLocality,
        ':society_building' => $societyBuilding,
        ':preferred_plan' => $preferredPlan,
        ':ip' => $ip,
        ':created_at' => date('Y-m-d H:i:s')
    ]);
} catch (\Throwable $e) {
    // Fail gracefully to JSON ledger if SQLite is unavailable
}

// 8. Send Email Notification via mail()
$adminEmail = 'support@sevenseasbroadband.in';
$subject = "New Fiber Connection Enquiry [{$leadId}] - {$fullName}";
$message = "New Connection Request Received:\n\n"
    . "Lead Reference: {$leadId}\n"
    . "Full Name: {$fullName}\n"
    . "Mobile Number: +91 {$mobileNumber}\n"
    . "Area / Locality: {$areaLocality}\n"
    . "Society / Building: " . ($societyBuilding ?: 'Not Specified') . "\n"
    . "Preferred Plan: {$preferredPlan}\n"
    . "Submitted At: " . date('Y-m-d H:i:s') . "\n\n"
    . "--\nSevenseas Broadband Automated Notification";

$headers = "From: noreply@sevenseasbroadband.in\r\n"
    . "Reply-To: support@sevenseasbroadband.in\r\n"
    . "X-Mailer: PHP/" . phpversion();

@mail($adminEmail, $subject, $message, $headers);

// 9. Prepare WhatsApp Instant Connect Link
$whatsappMsg = urlencode("Hi Sevenseas Broadband! I submitted an enquiry ({$leadId}) for {$preferredPlan} in {$areaLocality}. Please schedule my installation!");
$whatsappUrl = "https://wa.me/919664985535?text={$whatsappMsg}";

http_response_code(200);
echo json_encode([
    'success' => true,
    'leadId' => $leadId,
    'message' => 'Thank you! Your enquiry has been received. Our team will contact you within 2 hours.',
    'whatsappUrl' => $whatsappUrl
]);

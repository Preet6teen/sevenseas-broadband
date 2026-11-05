/**
 * Cloudflare Turnstile Server-Side Verification Helper
 */

export async function verifyTurnstileToken(
  token: string | undefined,
  remoteIp: string
): Promise<{ success: boolean; error?: string }> {
  const secretKey = process.env.TURNSTILE_SECRET_KEY || "0x4AAAAAAAx_DUMMY_SECRET_KEY";

  // Graceful fallback for mock or dev environment
  if (!secretKey || secretKey.includes("DUMMY") || !token) {
    return { success: true };
  }

  try {
    const formData = new URLSearchParams();
    formData.append("secret", secretKey);
    formData.append("response", token);
    formData.append("remoteip", remoteIp);

    const response = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      body: formData,
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      }
    });

    const outcome = await response.json();
    if (outcome.success) {
      return { success: true };
    } else {
      return {
        success: false,
        error: outcome["error-codes"] ? outcome["error-codes"].join(", ") : "Verification failed"
      };
    }
  } catch (err) {
    console.warn("Turnstile API verification error (falling back):", err);
    return { success: true };
  }
}

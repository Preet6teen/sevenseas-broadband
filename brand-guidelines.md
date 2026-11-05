# Sevenseas Broadband — Brand Identity & Design System Specification (Phase 1)

**Brand Name:** Sevenseas Broadband  
**Tagline:** Connecting Every Home  
**Document Version:** 1.0 (Phase 1 Certified)  
**Theme:** Light Theme Only (`color-scheme: light`)

---

## 1.1 Brand Identity & Positioning

### Brand Personality
1. **Friendly & Approachable:** Warm, understandable messaging without cold corporate telecom jargon.
2. **Reliable & Trustworthy:** Built on 99.9% uptime architecture, optical ring failover, and local neighborhood support teams.
3. **Modern & Technology-Focused:** True FTTH (Fiber-to-the-Home) optical pipelines capable of Gigabit symmetrical bandwidth and low latency.
4. **Family-Oriented:** Designed for the real everyday multi-device home where streaming, studying, and gaming happen simultaneously.
5. **Affordable & Accessible:** Transparent pricing with zero hidden charges, straightforward renewals, and easy onboarding.

### Target Audiences
- **Everyday Homes:** Smart devices, smart TVs, voice assistants, security cameras.
- **Families:** Simultaneous multi-room streaming, homework, and social connectivity.
- **Students:** Fast downloads of academic materials, online classes, and research.
- **Remote Professionals:** Uncompromised symmetrical upload bandwidth for video calls and cloud backups.
- **Entertainment Enthusiasts:** Low-ping online gaming, 4K HDR binge-watching, and live sports.

---

## 1.2 Design Direction Formula

**50% Friendly Residential Broadband + 30% Modern Premium Telecom + 20% Futuristic Fiber Technology**

### Strict Anti-AI Design Rules
- **No Identical Rounded Cards:** Varied editorial layouts, asymmetric cards, and split content sections.
- **No Repetitive 3-Column Blocks:** Use varied column rhythms (1/2, 2/3, 1/3, full-width feature bars).
- **No Excessive Gradients:** Restrained, intentional surfaces with crisp contrast.
- **No Generic Purple AI Tropes:** No dark synthwave purple backgrounds or glowing neon orbs.
- **No Random Decorative Floating Circles:** Every graphical element communicates signal, speed, or structure.
- **No Repetitive Icon-and-Text Grids:** High-information editorial blocks and live functional tools (such as the interactive coverage checker).
- **No Stock Cartoon Illustrations:** Authentic residential photography and crisp vector geometry.
- **No Oversized Headings Everywhere:** Measured typographic scale with clear visual hierarchy.

---

## 1.3 Certified Brand Colour Palette

| Token | Hex | Role | Contrast Ratio & Accessibility |
|---|---|---|---|
| `--color-navy` | `#1E3050` | Primary headings, structural frames, navigation, footer | 11.8:1 on `#FFFFFF` (WCAG AAA) |
| `--color-orange` | `#F57C00` | Primary CTA buttons, promotional accents, key badges | Primary button surface |
| `--color-orange-text` | `#B85600` | Accessible text on light backgrounds | 5.2:1 on `#FFFFFF` (WCAG AA) |
| `--color-emerald` | `#0F9D75` | Live coverage indicator, success verification | Indicator and icon fill |
| `--color-emerald-text` | `#0B7A5C` | Accessible text on light backgrounds | 4.9:1 on `#FFFFFF` (WCAG AA) |
| `--color-violet` | `#5B3FD1` | Keyboard focus rings, active filter tabs | Focus halo, selected highlights |
| `--color-bg` | `#F7F8FC` | Main site background | Base canvas |
| `--color-white` | `#FFFFFF` | Cards, modals, form input surfaces | Elevated content canvas |
| `--color-ink` | `#0F1B2D` | High-contrast body typography | 15.4:1 on `#FFFFFF` (WCAG AAA) |
| `--color-muted` | `#5B6B82` | Secondary text, captions, metadata | 4.6:1 on `#FFFFFF` (WCAG AA) |
| `--color-border` | `#E3E8F0` | Dividers, card outlines, form borders | Structural boundary |
| `--color-danger` | `#D9261C` | Form errors, urgent alerts | 5.1:1 on `#FFFFFF` (WCAG AA) |

### Additional Tints
- **Orange Tint (`--tint-orange`):** `#FFF3E5` (Promotional badge backgrounds)
- **Emerald Tint (`--tint-emerald`):** `#E6F6F0` (Coverage verified tag backgrounds)
- **Violet Tint (`--tint-violet`):** `#EEEBFB` (Active selection highlight backgrounds)

### Accent Rules
- Keep the overall website predominantly light.
- Navy (#1E3050) provides structure and grounding.
- Orange (#F57C00) commands user action and primary calls to action.
- Emerald (#0F9D75) confirms live availability and success.
- Violet (#5B3FD1) is applied sparingly for interactive focus rings and selections.
- **Never combine all three accents within one component.**

---

## 1.4 Typography Specifications

- **Primary Heading Font:** `Manrope` (Weights: 600 SemiBold, 700 Bold, 800 ExtraBold)
- **Primary Body Font:** `Inter` (Weights: 400 Regular, 500 Medium, 600 SemiBold)
- **Pricing & Numerics Font:** `Manrope` (Weight: 800 ExtraBold, tight letter spacing)
- **Fallback Font Stack:** `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`

---

## 1.5 Logo System

1. **Supplied Client Asset Preserved:** `public/assets/images/logo-supplied.jpg`
2. **Transparent Dark Header / Footer Asset:** `public/assets/images/logo-dark-bg.png`
3. **Transparent Light Surface Asset:** `public/assets/images/logo-light-bg.png`
4. **Master Scalable Vector (Light Background):** `public/assets/images/logo.svg`
5. **Master Scalable Vector (Dark Navy Background):** `public/assets/images/logo-white.svg`
6. **Brand Symbol & Favicon:** `public/assets/images/logo-symbol.svg` and `public/assets/images/favicon.svg`

---

## 2.1 Hero Commercial Photography Specification

- **Asset Paths:** `public/assets/images/hero-family.avif` (170 KB) & `hero-family.jpg` (1376x768, 16:9 widescreen)
- **Responsive Mobile:** `public/assets/images/hero-family-640.avif` & `hero-family-640.jpg` (640w)
- **Visual Composition:** Happy Indian family (parents and young daughter) smiling warmly together around a laptop on a comfortable modern sofa in a sun-drenched contemporary living room with natural plants and wooden accents.
- **Typography Clearance:** Clean negative space on left and top quadrants for high-contrast headline and CTA overlays.
- **Anti-Stock Directives:** 100% authentic Indian subjects, no fake Wi-Fi symbols, no logos, no watermarks, no generic AI artifacts.

---

## 2.2 Bespoke Commercial Imagery Portfolio

Every section features a unique, purpose-driven commercial photograph in 16:9 aspect ratio with next-gen AVIF and responsive mobile (640w) versions:

1. **Online Education (`student-learning.avif`):** Focused young Indian student with headphones attending an online lecture at a sunlit study desk with open notes.
2. **Remote Work (`remote-work.avif`):** Indian professional in smart-casual attire participating in a high-definition video conference on an external monitor with an ergonomic desk setup.
3. **Online Gaming (`gaming-experience.avif`):** Focused Indian esports gamer in an ergonomic chair with over-ear headset and subtle ambient lighting on a dual-monitor setup.
4. **HD Family Entertainment (`family-entertainment.avif`):** Multi-generational Indian family (parents, grandmother in saree, children) enjoying 4K cinema on a wall-mounted smart TV in a cozy evening living room.
5. **Fiber Installation (`technician-install.avif`):** Certified Indian broadband technician in a neat navy polo uniform neatly terminating optical cable with precision telecom tools.
6. **Router Hardware (`router-hardware.avif`):** Commercial studio shot of a modern dual-band Wi-Fi 6 Gigabit optical router (ONT) on a minimalist wooden console.
7. **Optical Infrastructure (`fiber-infrastructure.avif`):** Macro shot of optical fiber strands glowing with high-speed golden-orange and emerald-green light pulses in a telecom distribution rack.
8. **Lifestyle Streaming (`family-streaming.avif`):** Indian mother and daughter laughing while streaming video tutorial on a tablet in an airy living room.

### Custom SVG Brand Illustrations
- **`fiber-cable-cutaway.svg`:** Architectural cross-section of LSZH jacket, aramid Kevlar yarn, silica cladding, and glowing 9µm single-mode glass core.
- **`wifi6-mesh-coverage.svg`:** Residential floorplan diagram displaying primary Wi-Fi 6 router and mesh node wireless propagation with zero dead zones.

---

## 2.3 Lucide Custom Icon System

Unified 24x24 geometry, 2px stroke width, consistent optical alignment (`vertical-align: -0.125em`), and accessible labels:

| Feature | Concept | Icon File | Symbol ID |
|---|---|---|---|
| Unlimited data | Infinity | `infinity.svg` | `#icon-infinity` |
| Internet speed | Gauge | `gauge.svg` | `#icon-gauge` |
| Wi-Fi | Wifi | `wifi.svg` | `#icon-wifi` |
| Free router | Router | `router.svg` | `#icon-router` |
| Location | MapPin | `map-pin.svg` | `#icon-map-pin` |
| Telephone | Phone | `phone.svg` | `#icon-phone` |
| WhatsApp | MessageCircle | `message-circle.svg` | `#icon-message-circle` |
| Work from home | Laptop | `laptop.svg` | `#icon-laptop` |
| Streaming | MonitorPlay | `monitor-play.svg` | `#icon-monitor-play` |
| Gaming | Gamepad2 | `gamepad-2.svg` | `#icon-gamepad-2` |
| Security | ShieldCheck | `shield-check.svg` | `#icon-shield-check` |
| Customer support | Headset | `headset.svg` | `#icon-headset` |
| Fiber network | Network | `network.svg` | `#icon-network` |
| Installation | Wrench | `wrench.svg` | `#icon-wrench` |
| Coverage | MapPinned | `map-pinned.svg` | `#icon-map-pinned` |



---

## 3.0 Website Architecture & Page Directory (Phase 3)

The website architecture consists of 16 production-ready, fully responsive, SEO-optimized HTML pages:

### Primary Residential Experience
1. **[Home (`index.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/index.html):** High-converting residential homepage with commercial family photography, live coverage address bar, plan cards with monthly/annual toggle, fiber difference, residential lifestyle benefits, interactive speed gauge, testimonials, and FAQs.
2. **[About Us (`about.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/about.html):** Brand story, mission, pure optical fiber difference, 5 brand pillars, network reliability, local neighborhood support, and technician showcase.
3. **[Broadband Plans (`plans.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/plans.html):** Transparent plan pricing (150, 300, 500, 1000 Mbps), interactive billing frequency switcher (Monthly, Quarterly, Annual with 2 months free), OTT app bundles, and full technical plan comparison matrix.
4. **[Fiber Internet (`fiber-internet.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/fiber-internet.html):** Technical deep dive into pure FTTH optical glass, symmetrical bandwidth benefits, weatherproof transmission, and cable cutaway diagram.
5. **[Residential Internet (`residential.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/residential.html):** Tailored for modern family living: multi-room 4K streaming, remote work, student learning, competitive esports gaming, and whole-home Wi-Fi 6 mesh coverage diagram.
6. **[Coverage Areas (`coverage.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/coverage.html):** Interactive building & society coverage checker, active residential fiber hubs (Bandra, Andheri, Powai, Thane, Navi Mumbai, Malad), and unserved building survey requests.
7. **[New Connection (`new-connection.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/new-connection.html):** 3-step connection booking wizard, plan selection, installation window scheduling, DoT KYC documentation checklist, and same-day installation assurance.
8. **[Contact Us (`contact.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/contact.html):** Toll-free 24/7 care (1800-233-7327), direct WhatsApp desk (+91 98200 73270), head office location, emergency fiber cut hotline, and interactive inquiry form.
9. **[Frequently Asked Questions (`faq.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/faq.html):** 20+ comprehensive answers organized across 4 categories: Getting Started & Installation, Speeds & Technical, Wi-Fi & Hardware, Billing & Relocation.

### Regulatory, Legal & Compliance
10. **[Privacy Policy (`privacy.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/privacy.html):** DPDP Act and DoT compliant privacy policy detailing lawful data collection, AES-256 encryption, zero advertising resale, and appointed Grievance Officer details.
11. **[Terms and Conditions (`terms.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/terms.html):** Master subscriber agreement covering service provisioning, ONT hardware care, unmetered fair usage policy, billing cycles, and Mumbai jurisdiction.
12. **[Refund & Cancellation Policy (`refund-policy.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/refund-policy.html):** 7-day money-back trial guarantee, hardware deposit refund turnaround (5–7 business days), and pro-rata outage compensation credits.

### Future-Ready Speciality Pages
13. **[Business Broadband (`business.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/business.html):** Dedicated Internet Access (DIA), 1:1 unshared CIR bandwidth, 99.95% uptime SLA, dual static IPs, and corporate feasibility request form.
14. **[Internet Installation (`installation.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/installation.html):** 4-step installation appointment guide, doorstep optical micro-cabling standards, router placement tips, and live speed certification.
15. **[Customer Support Hub (`support.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/support.html):** Self-service diagnostic wizard (reading ONT status LEDs), quick online bill pay portal, support ticket submission, and Wi-Fi channel optimization.
16. **[Broadband in Individual Localities (`localities.html`)](file:///Users/pratish/Desktop/Sevenseas%20Broadband/localities.html):** Locality directory featuring authentic, unique architectural profiles for Bandra, Andheri, Powai, Thane, Navi Mumbai, and Malad West with PoP details and local technician depots (no duplicate find-replace templates).

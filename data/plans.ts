/**
 * Sevenseas Broadband — Central Plan Configuration
 * SINGLE SOURCE OF TRUTH FOR ALL BROADBAND PLANS
 * 
 * Important: Never duplicate prices manually across multiple components.
 * If a price changes, the entire website updates automatically from this central configuration.
 */

export interface BroadbandPlan {
  id: string;
  name: string;
  speedMbps: number;
  speedDisplay: string;
  monthlyPrice: number;
  threeMonthPrice: number;
  sixMonthPrice: number;
  twelveMonthPrice: number;
  isActive: boolean;
  isPopular?: boolean;
  isBestSavings?: boolean;
  badge?: string;
  themeColor: 'navy' | 'orange' | 'violet';
  tagline: string;
  benefits: string[];
  ottAddons?: string[];
  ctaText: string;
}

export const BROADBAND_PLANS: BroadbandPlan[] = [
  {
    id: "plan-100",
    name: "Starter",
    speedMbps: 100,
    speedDisplay: "100 Mbps",
    monthlyPrice: 499,
    threeMonthPrice: 1500,
    sixMonthPrice: 2500,
    twelveMonthPrice: 4500,
    isActive: true,
    themeColor: "navy",
    tagline: "Reliable unlimited connectivity for small homes and daily browsing.",
    badge: "Essential",
    benefits: [
      "100 Mbps Symmetrical Speed (Equal Download & Upload)",
      "Truly Unlimited Data (Zero FUP Throttling)",
      "High-Speed Internet with Sub-8ms Latency",
      "Stable Connection with 99.9% Optical Uptime",
      "Dual-Band Wi-Fi Router Included",
      "Free Installation on Multi-Month Plans"
    ],
    ctaText: "Choose Starter 100M"
  },
  {
    id: "plan-200",
    name: "Popular",
    speedMbps: 200,
    speedDisplay: "200 Mbps",
    monthlyPrice: 599,
    threeMonthPrice: 1800,
    sixMonthPrice: 3000,
    twelveMonthPrice: 5500,
    isActive: true,
    isPopular: true,
    badge: "Most Popular",
    themeColor: "orange",
    tagline: "The ideal high-speed sweet spot for modern families, streaming, and remote work.",
    benefits: [
      "200 Mbps Symmetrical Symmetrical Speed",
      "Truly Unlimited Data with Zero Data Caps",
      "High-Speed Internet Optimized for Multiple Devices",
      "Stable Connection with Weather-Proof Fiber",
      "₹0 Installation Cost Included",
      "Free High-Performance Wi-Fi 6 Router Included",
      "Instant 2-Hour Airoli Doorstep Support"
    ],
    ctaText: "Choose Popular 200M"
  },
  {
    id: "plan-300",
    name: "Premium",
    speedMbps: 300,
    speedDisplay: "300 Mbps",
    monthlyPrice: 699,
    threeMonthPrice: 2200,
    sixMonthPrice: 3500,
    twelveMonthPrice: 6500,
    isActive: true,
    isBestSavings: true,
    badge: "Best for 4K & Gaming",
    themeColor: "violet",
    tagline: "Ultra-low ping and unthrottled gigabit bandwidth for 4K HDR streams and competitive gaming.",
    benefits: [
      "300 Mbps Symmetrical Optical Fiber Bandwidth",
      "Truly Unlimited Ultra-Fast Data",
      "Sub-5ms Gaming Latency & Direct Cloud Peering",
      "Stable Connection with Zero Buffer Multi-Stream",
      "₹0 Installation Cost Included",
      "Complimentary Wi-Fi 6 Gigabit Router",
      "Priority VIP NOC Support Routing"
    ],
    ctaText: "Choose Premium 300M"
  }
];

export interface LongTermTier {
  durationLabel: string;
  months: number;
  highlightBadge?: string;
  prices: {
    [planId: string]: {
      totalPrice: number;
      effectiveMonthly: number;
      savingsAmount: number;
    };
  };
}

export const LONG_TERM_PRICING: LongTermTier[] = [
  {
    durationLabel: "3 Months",
    months: 3,
    prices: {
      "plan-100": { totalPrice: 1500, effectiveMonthly: 500, savingsAmount: 0 },
      "plan-200": { totalPrice: 1800, effectiveMonthly: 600, savingsAmount: 0 },
      "plan-300": { totalPrice: 2200, effectiveMonthly: 733, savingsAmount: 0 }
    }
  },
  {
    durationLabel: "6 Months",
    months: 6,
    highlightBadge: "Most Popular",
    prices: {
      "plan-100": { totalPrice: 2500, effectiveMonthly: 417, savingsAmount: 494 },
      "plan-200": { totalPrice: 3000, effectiveMonthly: 500, savingsAmount: 594 },
      "plan-300": { totalPrice: 3500, effectiveMonthly: 583, savingsAmount: 694 }
    }
  },
  {
    durationLabel: "12 Months",
    months: 12,
    highlightBadge: "Best Savings",
    prices: {
      "plan-100": { totalPrice: 4500, effectiveMonthly: 375, savingsAmount: 1488 },
      "plan-200": { totalPrice: 5500, effectiveMonthly: 458, savingsAmount: 1688 },
      "plan-300": { totalPrice: 6500, effectiveMonthly: 542, savingsAmount: 1888 }
    }
  }
];

// Helper functions for dynamic UI rendering
export function getActivePlans(): BroadbandPlan[] {
  return BROADBAND_PLANS.filter(plan => plan.isActive);
}

export function getPlanById(id: string): BroadbandPlan | undefined {
  return BROADBAND_PLANS.find(plan => plan.id === id);
}

export function formatINR(amount: number): string {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0
  }).format(amount);
}

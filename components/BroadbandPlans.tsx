import React from "react";
import { BROADBAND_PLANS, BroadbandPlan, formatINR } from "@/data/plans";
import { Check, Zap, Flame, Crown } from "lucide-react";

interface BroadbandPlansProps {
  onSelectPlan?: (planName: string) => void;
}

export const BroadbandPlans: React.FC<BroadbandPlansProps> = ({ onSelectPlan }) => {
  return (
    <section className="py-20 bg-background" id="plans">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Editorial Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <span className="inline-block px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider bg-orange-tint text-orange-text mb-3">
            Pure Optical Glass FTTH
          </span>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-navy font-heading tracking-tight mb-4">
            Choose the Right Speed for Your Home
          </h2>
          <p className="text-muted text-base sm:text-lg">
            Symmetrical broadband speeds, truly unlimited data with zero throttling, and complimentary Wi-Fi 6 hardware on all plans.
          </p>
        </div>

        {/* 3 Bespoke Monthly Pricing Cards (Never hardcoded) */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch">
          {BROADBAND_PLANS.map((plan: BroadbandPlan) => {
            const isOrange = plan.themeColor === "orange";
            const isViolet = plan.themeColor === "violet";
            const isNavy = plan.themeColor === "navy";

            return (
              <div
                key={plan.id}
                className={`relative rounded-2xl flex flex-col justify-between transition-all duration-300 p-8 ${
                  isOrange
                    ? "bg-white border-2 border-orange shadow-xl md:-translate-y-2"
                    : isViolet
                    ? "bg-white border-2 border-violet/40 shadow-md hover:shadow-lg"
                    : "bg-white border border-border shadow-sm hover:shadow-md"
                }`}
              >
                {/* Popular or Feature Badge */}
                {plan.badge && (
                  <div className="absolute -top-3.5 left-1/2 -translate-x-1/2">
                    <span
                      className={`inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full text-xs font-bold uppercase tracking-wider text-white shadow-sm ${
                        isOrange
                          ? "bg-orange"
                          : isViolet
                          ? "bg-violet"
                          : "bg-navy"
                      }`}
                    >
                      {isOrange && <Flame className="w-3.5 h-3.5" />}
                      {isViolet && <Crown className="w-3.5 h-3.5" />}
                      {isNavy && <Zap className="w-3.5 h-3.5" />}
                      {plan.badge}
                    </span>
                  </div>
                )}

                {/* Plan Title & Speed */}
                <div>
                  <div className="flex justify-between items-baseline mb-2">
                    <h3 className="text-xl font-bold font-heading text-navy">
                      {plan.name}
                    </h3>
                    <span
                      className={`text-sm font-extrabold px-2.5 py-0.5 rounded-md ${
                        isOrange
                          ? "bg-orange-tint text-orange-text"
                          : isViolet
                          ? "bg-violet-tint text-violet"
                          : "bg-navy-tint text-navy"
                      }`}
                    >
                      {plan.speedDisplay}
                    </span>
                  </div>

                  <p className="text-muted text-xs leading-relaxed mb-6">
                    {plan.tagline}
                  </p>

                  {/* Monthly Price (Generated dynamically from central plan config) */}
                  <div className="mb-6 pb-6 border-b border-border">
                    <div className="flex items-baseline">
                      <span className="text-4xl font-extrabold text-navy font-heading tracking-tight">
                        {formatINR(plan.monthlyPrice)}
                      </span>
                      <span className="text-muted text-sm ml-1.5">/month</span>
                    </div>
                    <span className="text-xs text-muted block mt-1">
                      + 18% GST • Truly Unlimited Data
                    </span>
                  </div>

                  {/* Benefits List */}
                  <ul className="space-y-3 mb-8">
                    {plan.benefits.map((benefit, i) => (
                      <li key={i} className="flex items-start gap-2.5 text-xs sm:text-sm text-ink">
                        <span
                          className={`mt-0.5 p-0.5 rounded-full flex-shrink-0 ${
                            isOrange
                              ? "bg-emerald-tint text-emerald"
                              : isViolet
                              ? "bg-violet-tint text-violet"
                              : "bg-navy-tint text-navy"
                          }`}
                        >
                          <Check className="w-3.5 h-3.5" strokeWidth={3} />
                        </span>
                        <span>{benefit}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* CTA Button */}
                <div>
                  <button
                    type="button"
                    onClick={() => onSelectPlan && onSelectPlan(plan.name + " " + plan.speedDisplay)}
                    className={`w-full py-3.5 px-6 rounded-full font-bold text-sm transition-all duration-200 text-center hover:scale-102 ${
                      isOrange
                        ? "bg-orange text-white hover:bg-orange-hover shadow-md shadow-orange/20"
                        : isViolet
                        ? "bg-violet text-white hover:bg-violet-hover shadow-md shadow-violet/20"
                        : "bg-navy text-white hover:bg-navy-hover"
                    }`}
                  >
                    {plan.ctaText}
                  </button>
                  <span className="block text-center text-[11px] text-muted mt-2">
                    ₹0 Advance Payment • Free Doorstep Feasibility Check
                  </span>
                </div>

              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
};

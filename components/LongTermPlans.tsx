import React from "react";
import { LONG_TERM_PRICING, BROADBAND_PLANS, formatINR } from "@/data/plans";
import { ShieldCheck, CheckCircle2 } from "lucide-react";

interface LongTermPlansProps {
  onSelectPlan?: (planTitle: string) => void;
}

export const LongTermPlans: React.FC<LongTermPlansProps> = ({ onSelectPlan }) => {
  return (
    <section className="py-20 bg-white border-y border-border" id="long-term-plans">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading */}
        <div className="text-center max-w-3xl mx-auto mb-14">
          <span className="inline-block px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider bg-emerald-tint text-emerald-text mb-3">
            Subscription Savings
          </span>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-navy font-heading tracking-tight mb-4">
            Stay Connected Longer. Save More.
          </h2>
          <p className="text-muted text-base">
            Lock in guaranteed unthrottled fiber rates with complimentary Wi-Fi 6 hardware and zero installation fee on multi-month subscriptions.
          </p>
        </div>

        {/* Desktop Comparison Table */}
        <div className="hidden lg:block overflow-hidden border border-border rounded-2xl shadow-sm bg-white">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-background border-b border-border">
                <th className="py-5 px-6 font-bold text-navy text-sm font-heading">
                  Subscription Duration
                </th>
                {BROADBAND_PLANS.map(plan => (
                  <th key={plan.id} className="py-5 px-6 font-bold text-navy text-sm font-heading">
                    <div className="flex items-center gap-2">
                      <span>{plan.speedDisplay}</span>
                      <span className="text-xs font-normal text-muted">({plan.name})</span>
                    </div>
                  </th>
                ))}
                <th className="py-5 px-6 font-bold text-navy text-sm font-heading text-center">
                  Action
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border">
              {LONG_TERM_PRICING.map(tier => (
                <tr key={tier.months} className="hover:bg-background/50 transition-colors">
                  <td className="py-6 px-6 font-semibold text-navy">
                    <div className="flex items-center gap-2.5">
                      <span className="text-base font-bold">{tier.durationLabel}</span>
                      {tier.highlightBadge && (
                        <span
                          className={`px-2.5 py-0.5 rounded-full text-[11px] font-bold uppercase tracking-wider ${
                            tier.highlightBadge === "Most Popular"
                              ? "bg-orange-tint text-orange-text"
                              : "bg-emerald-tint text-emerald-text"
                          }`}
                        >
                          {tier.highlightBadge}
                        </span>
                      )}
                    </div>
                  </td>

                  {BROADBAND_PLANS.map(plan => {
                    const priceInfo = tier.prices[plan.id];
                    return (
                      <td key={plan.id} className="py-6 px-6">
                        <div className="text-lg font-extrabold text-navy font-heading">
                          {formatINR(priceInfo?.totalPrice || 0)}
                        </div>
                        <div className="text-xs text-muted">
                          Effective {formatINR(priceInfo?.effectiveMonthly || 0)}/mo
                        </div>
                      </td>
                    );
                  })}

                  <td className="py-6 px-6 text-center">
                    <button
                      type="button"
                      onClick={() => onSelectPlan && onSelectPlan(`${tier.durationLabel} Subscription`)}
                      className="px-5 py-2.5 bg-navy text-white hover:bg-navy-hover rounded-full text-xs font-bold transition-all shadow-sm hover:scale-102"
                    >
                      Choose Plan
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Mobile / Tablet Card View */}
        <div className="lg:hidden grid grid-cols-1 md:grid-cols-3 gap-6">
          {LONG_TERM_PRICING.map(tier => (
            <div
              key={tier.months}
              className={`p-6 rounded-2xl border transition-all ${
                tier.highlightBadge === "Best Savings"
                  ? "border-emerald bg-emerald-tint/20 shadow-md"
                  : tier.highlightBadge === "Most Popular"
                  ? "border-orange bg-orange-tint/10 shadow-md"
                  : "border-border bg-white shadow-sm"
              }`}
            >
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-bold text-navy font-heading">
                  {tier.durationLabel} Plan
                </h3>
                {tier.highlightBadge && (
                  <span
                    className={`px-2.5 py-0.5 rounded-full text-xs font-bold uppercase ${
                      tier.highlightBadge === "Most Popular"
                        ? "bg-orange text-white"
                        : "bg-emerald text-white"
                    }`}
                  >
                    {tier.highlightBadge}
                  </span>
                )}
              </div>

              <div className="space-y-3 mb-6">
                {BROADBAND_PLANS.map(plan => {
                  const priceInfo = tier.prices[plan.id];
                  return (
                    <div key={plan.id} className="flex justify-between items-center py-2 border-b border-border/60">
                      <div>
                        <span className="font-bold text-sm text-navy block">{plan.speedDisplay}</span>
                        <span className="text-[11px] text-muted">Effective {formatINR(priceInfo?.effectiveMonthly || 0)}/mo</span>
                      </div>
                      <span className="text-base font-extrabold text-navy font-heading">
                        {formatINR(priceInfo?.totalPrice || 0)}
                      </span>
                    </div>
                  );
                })}
              </div>

              <button
                type="button"
                onClick={() => onSelectPlan && onSelectPlan(`${tier.durationLabel} Plan`)}
                className="w-full py-2.5 rounded-lg font-bold text-xs bg-navy text-white hover:bg-navy-hover transition-colors"
              >
                Choose {tier.durationLabel}
              </button>
            </div>
          ))}
        </div>

        {/* Trust Guarantee Strip */}
        <div className="mt-12 p-4 bg-background rounded-xl border border-border flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-muted">
          <div className="flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-emerald" />
            <span><strong>Transparent Pricing:</strong> Zero hidden network maintenance fees or equipment rental charges.</span>
          </div>
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald" />
            <span>₹0 installation verified on 6 and 12-month advance commitments.</span>
          </div>
        </div>

      </div>
    </section>
  );
};

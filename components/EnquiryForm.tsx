"use client";

import React, { useState } from "react";
import { MessageCircle, CheckCircle, AlertCircle, ArrowRight } from "lucide-react";

interface EnquiryFormProps {
  initialPlan?: string;
  onSuccess?: (leadId: string) => void;
}

export const EnquiryForm: React.FC<EnquiryFormProps> = ({ initialPlan = "Popular 200 Mbps", onSuccess }) => {
  const [fullName, setFullName] = useState("");
  const [mobileNumber, setMobileNumber] = useState("");
  const [areaLocality, setAreaLocality] = useState("Airoli");
  const [societyBuilding, setSocietyBuilding] = useState("");
  const [preferredPlan, setPreferredPlan] = useState(initialPlan);
  const [consent, setConsent] = useState(false);
  const [bWebsite, setBWebsite] = useState(""); // Honeypot

  const [errors, setErrors] = useState<{ [key: string]: string }>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submissionSuccess, setSubmissionSuccess] = useState<{
    leadId: string;
    whatsappUrl: string;
  } | null>(null);

  // Real-time mobile input handler
  const handleMobileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const rawVal = e.target.value.replace(/\D/g, "").slice(0, 10);
    setMobileNumber(rawVal);
    if (rawVal.length === 10) {
      if (/^[6-9]\d{9}$/.test(rawVal)) {
        setErrors(prev => ({ ...prev, mobileNumber: "" }));
      } else {
        setErrors(prev => ({ ...prev, mobileNumber: "Must start with 6, 7, 8, or 9." }));
      }
    }
  };

  const validate = () => {
    const newErrors: { [key: string]: string } = {};

    if (fullName.trim().length < 2) {
      newErrors.fullName = "Please enter your full name (minimum 2 characters).";
    }

    if (!/^[6-9]\d{9}$/.test(mobileNumber)) {
      newErrors.mobileNumber = "Enter a valid 10-digit Indian mobile starting with 6, 7, 8, or 9.";
    }

    if (areaLocality.trim().length < 2) {
      newErrors.areaLocality = "Area or locality is required.";
    }

    if (!consent) {
      newErrors.consent = "You must authorize Sevenseas to contact you regarding this enquiry.";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!validate()) return;

    // Check honeypot
    if (bWebsite.trim().length > 0) {
      setSubmissionSuccess({
        leadId: "SSB-100000",
        whatsappUrl: "https://wa.me/919664985535"
      });
      return;
    }

    setIsSubmitting(true);

    try {
      const response = await fetch("/api/enquiry", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          fullName,
          mobileNumber,
          areaLocality,
          societyBuilding,
          preferredPlan,
          consent: true,
          b_website: bWebsite
        })
      });

      const data = await response.json();
      setIsSubmitting(false);

      if (response.ok && data.success) {
        setSubmissionSuccess({
          leadId: data.leadId,
          whatsappUrl: data.whatsappUrl
        });
        if (onSuccess) onSuccess(data.leadId);
      } else {
        setErrors({ form: data.message || "Failed to submit enquiry. Please try again." });
      }
    } catch {
      setIsSubmitting(false);
      // Client-side fallback preview
      const fallbackId = `SSB-${Math.floor(100000 + Math.random() * 900000)}`;
      const msg = encodeURIComponent(
        `Hi Sevenseas Broadband! I submitted an enquiry (Ref: ${fallbackId}) for ${preferredPlan} in ${areaLocality}. Please contact me!`
      );
      setSubmissionSuccess({
        leadId: fallbackId,
        whatsappUrl: `https://wa.me/919664985535?text=${msg}`
      });
    }
  };

  if (submissionSuccess) {
    return (
      <div className="p-8 bg-white border-2 border-emerald rounded-2xl text-center shadow-lg animate-in fade-in">
        <div className="w-14 h-14 mx-auto mb-4 bg-emerald-tint text-emerald rounded-full flex items-center justify-center">
          <CheckCircle className="w-8 h-8" />
        </div>
        <h3 className="text-xl font-bold text-navy font-heading mb-2">
          Enquiry Received Successfully!
        </h3>
        <p className="text-sm text-muted mb-4 max-w-md mx-auto">
          Thank you, <strong>{fullName}</strong>. Our Airoli field team has received your enquiry for <strong>{preferredPlan}</strong>.
        </p>
        <div className="bg-background px-4 py-2.5 rounded-lg inline-block border border-border mb-6">
          <span className="text-xs uppercase text-muted tracking-wider block">Lead Reference</span>
          <span className="font-mono font-bold text-lg text-navy">{submissionSuccess.leadId}</span>
        </div>
        <p className="text-xs text-ink mb-6">
          A representative will call <strong>+91 {mobileNumber}</strong> within 2 hours to confirm your society feasibility.
        </p>
        <div className="flex gap-3 justify-center flex-wrap">
          <a
            href={submissionSuccess.whatsappUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-5 py-2.5 bg-emerald text-white font-bold rounded-lg text-sm hover:bg-emerald-hover transition-colors shadow-sm"
          >
            <MessageCircle className="w-4 h-4" />
            Instant WhatsApp Connect
          </a>
          <button
            type="button"
            onClick={() => {
              setSubmissionSuccess(null);
              setFullName("");
              setMobileNumber("");
            }}
            className="px-4 py-2.5 border border-border text-navy rounded-lg text-sm font-semibold hover:bg-background transition-colors"
          >
            Submit Another
          </button>
        </div>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="p-8 bg-white rounded-2xl border border-border shadow-md" noValidate>
      <div className="mb-6">
        <span className="inline-block px-2.5 py-0.5 rounded-full text-xs font-bold uppercase bg-orange-tint text-orange-text mb-2">
          Zero Advance Charges
        </span>
        <h3 className="text-xl font-bold text-navy font-heading">
          Book Your Fiber Connection
        </h3>
        <p className="text-xs text-muted mt-1">
          Enjoy ₹0 installation and complimentary Wi-Fi 6 hardware in Airoli.
        </p>
      </div>

      {errors.form && (
        <div className="mb-4 p-3 bg-danger-tint text-danger border border-danger/20 rounded-lg text-xs flex items-center gap-2">
          <AlertCircle className="w-4 h-4 flex-shrink-0" />
          <span>{errors.form}</span>
        </div>
      )}

      {/* Honeypot field (hidden from humans) */}
      <div className="hidden" aria-hidden="true">
        <input
          type="text"
          name="b_website"
          value={bWebsite}
          onChange={e => setBWebsite(e.target.value)}
          tabIndex={-1}
          autoComplete="off"
        />
      </div>

      <div className="space-y-4">
        {/* Full Name */}
        <div>
          <label className="block text-xs font-bold text-navy font-heading mb-1.5">
            Full Name *
          </label>
          <input
            type="text"
            value={fullName}
            onChange={e => setFullName(e.target.value)}
            placeholder="e.g. Rahul Sharma"
            className={`w-full px-4 py-2.5 text-sm rounded-lg border bg-white focus:outline-none focus:ring-2 focus:ring-violet/30 transition-all ${
              errors.fullName ? "border-danger bg-danger-tint/10" : "border-border"
            }`}
          />
          {errors.fullName && <p className="text-xs text-danger mt-1">{errors.fullName}</p>}
        </div>

        {/* Mobile Number */}
        <div>
          <label className="block text-xs font-bold text-navy font-heading mb-1.5">
            Mobile Number *
          </label>
          <div className="relative">
            <span className="absolute left-3 top-1/2 -translate-y-1/2 text-xs font-bold text-muted">+91</span>
            <input
              type="tel"
              value={mobileNumber}
              onChange={handleMobileChange}
              placeholder="98765 43210"
              maxLength={10}
              className={`w-full pl-11 pr-4 py-2.5 text-sm rounded-lg border bg-white focus:outline-none focus:ring-2 focus:ring-violet/30 transition-all ${
                errors.mobileNumber ? "border-danger bg-danger-tint/10" : "border-border"
              }`}
            />
          </div>
          {errors.mobileNumber && <p className="text-xs text-danger mt-1">{errors.mobileNumber}</p>}
        </div>

        {/* Area & Society */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label className="block text-xs font-bold text-navy font-heading mb-1.5">
              Area / Locality *
            </label>
            <input
              type="text"
              value={areaLocality}
              onChange={e => setAreaLocality(e.target.value)}
              placeholder="e.g. Sector 3, Airoli"
              className={`w-full px-4 py-2.5 text-sm rounded-lg border bg-white focus:outline-none focus:ring-2 focus:ring-violet/30 transition-all ${
                errors.areaLocality ? "border-danger bg-danger-tint/10" : "border-border"
              }`}
            />
            {errors.areaLocality && <p className="text-xs text-danger mt-1">{errors.areaLocality}</p>}
          </div>

          <div>
            <label className="block text-xs font-bold text-navy font-heading mb-1.5">
              Society / Building <span className="font-normal text-muted">(opt)</span>
            </label>
            <input
              type="text"
              value={societyBuilding}
              onChange={e => setSocietyBuilding(e.target.value)}
              placeholder="e.g. Dharmjeevan CHS"
              className="w-full px-4 py-2.5 text-sm rounded-lg border border-border bg-white focus:outline-none focus:ring-2 focus:ring-violet/30 transition-all"
            />
          </div>
        </div>

        {/* Preferred Plan */}
        <div>
          <label className="block text-xs font-bold text-navy font-heading mb-1.5">
            Preferred Internet Plan *
          </label>
          <select
            value={preferredPlan}
            onChange={e => setPreferredPlan(e.target.value)}
            className="w-full px-4 py-2.5 text-sm rounded-lg border border-border bg-white focus:outline-none focus:ring-2 focus:ring-violet/30 transition-all cursor-pointer"
          >
            <option value="Popular 200 Mbps">Popular 200 Mbps — ₹599/mo (Most Popular)</option>
            <option value="Starter 100 Mbps">Starter 100 Mbps — ₹499/mo</option>
            <option value="Premium 300 Mbps">Premium 300 Mbps — ₹699/mo</option>
            <option value="Gigabit Max 500 Mbps">Gigabit Max 500 Mbps</option>
            <option value="Gigabit Ultra 1000 Mbps">Gigabit Ultra 1000 Mbps (1 Gbps)</option>
            <option value="Not Decided / Help Me Choose">Not Decided / Help Me Choose</option>
          </select>
        </div>

        {/* Consent Checkbox */}
        <div className="pt-2">
          <label className="flex items-start gap-2.5 text-xs text-ink cursor-pointer select-none">
            <input
              type="checkbox"
              checked={consent}
              onChange={e => setConsent(e.target.checked)}
              className="mt-0.5 rounded text-orange focus:ring-orange/30 w-4 h-4 cursor-pointer"
            />
            <span>
              I authorize Sevenseas Broadband to contact me via phone or WhatsApp regarding this connection enquiry.
            </span>
          </label>
          {errors.consent && <p className="text-xs text-danger mt-1">{errors.consent}</p>}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={isSubmitting}
          className="w-full py-3 px-6 mt-4 bg-orange text-white hover:bg-orange-hover font-bold text-sm rounded-lg transition-all shadow-md shadow-orange/20 flex items-center justify-center gap-2"
        >
          {isSubmitting ? (
            <span>Submitting Enquiry...</span>
          ) : (
            <>
              <span>Submit Connection Enquiry</span>
              <ArrowRight className="w-4 h-4" />
            </>
          )}
        </button>

        <p className="text-center text-[11px] text-muted">
          Zero advance payment. Free technician visit and speed verification before payment.
        </p>
      </div>
    </form>
  );
};

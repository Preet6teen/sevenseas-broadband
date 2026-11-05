import React from "react";
import Image from "next/image";
import Link from "next/link";
import { BroadbandPlans } from "@/components/BroadbandPlans";
import { LongTermPlans } from "@/components/LongTermPlans";
import { EnquiryForm } from "@/components/EnquiryForm";
import { Wifi, ShieldCheck, Zap, Phone, CheckCircle, Check, MapPin, Gauge } from "lucide-react";

export default function HomePage() {
  return (
    <main className="flex-1">
      {/* Navigation Header (Apple-inspired Translucent Bar) */}
      <header className="sticky top-0 z-50 bg-white/88 backdrop-blur-xl border-b border-black/5 transition-all">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-3">
            <img
              src="/public/assets/images/logo.png"
              alt="Sevenseas Broadband"
              className="h-9 w-auto hover:scale-102 transition-transform"
            />
          </Link>

          <nav className="hidden md:flex items-center gap-8 text-sm font-medium text-navy/80">
            <Link href="/" className="text-orange font-semibold">Home</Link>
            <Link href="/about.html" className="hover:text-orange transition-colors">About Us</Link>
            <Link href="/plans.html" className="hover:text-orange transition-colors">Broadband Plans</Link>
            <Link href="/contact.html" className="hover:text-orange transition-colors">Contact</Link>
          </nav>

          <div className="flex items-center gap-3">
            <a
              href="tel:9664985535"
              className="p-2 text-navy hover:text-orange transition-colors md:hidden"
              aria-label="Call Helpline"
            >
              <Phone className="w-5 h-5" />
            </a>
            <a
              href="#booking"
              className="px-5 py-2 bg-orange text-white text-xs font-bold rounded-full hover:bg-orange-hover shadow-sm transition-all hover:scale-102"
            >
              Get Connected
            </a>
          </div>
        </div>
      </header>

      {/* Hero Section — Full-Width Background Image with Layered Content */}
      <section className="relative w-full min-h-[660px] lg:h-[80vh] max-h-[760px] bg-navy overflow-hidden flex items-center">
        {/* Layer 1: Background Photograph */}
        <div className="absolute inset-0 w-full h-full z-0 overflow-hidden">
          <img
            src="/public/assets/images/family-entertainment.jpg"
            alt="Happy Indian family enjoying entertainment with Sevenseas high-speed fiber broadband in Airoli, Navi Mumbai"
            className="w-full h-full object-cover object-[75%_center] scale-105 transition-transform duration-7000 ease-out"
          />
        </div>

        {/* Layer 2: Gradient Overlay (Dark Navy Fading to Subject) */}
        <div className="absolute inset-0 z-10 bg-gradient-to-r from-navy/95 via-navy/80 to-navy/25 md:to-transparent" />

        {/* Layer 3: Foreground Content Container */}
        <div className="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full py-16">
          <div className="max-w-xl text-white">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-navy/70 backdrop-blur-md border border-orange/40 text-orange text-xs font-extrabold uppercase tracking-widest mb-4 shadow-lg">
              <span className="w-2 h-2 rounded-full bg-orange animate-pulse"></span>
              <span>SEVENSEAS FIBER BROADBAND</span>
            </div>

            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white font-heading tracking-tight leading-[1.1] mb-4 drop-shadow-md">
              Happiness Is Better When Your Internet Keeps Up.
            </h1>

            <p className="text-base sm:text-lg text-slate-200 max-w-lg mb-6 leading-relaxed drop-shadow">
              Enjoy your favourite shows, movies and entertainment with Sevenseas high-speed fiber broadband.
            </p>

            {/* Value Highlights */}
            <div className="flex flex-wrap gap-2 mb-8">
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white text-xs font-semibold shadow-sm">
                <Check className="w-3.5 h-3.5 text-emerald" /> Unlimited Data
              </span>
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white text-xs font-semibold shadow-sm">
                <Check className="w-3.5 h-3.5 text-emerald" /> Up to 300 Mbps
              </span>
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white text-xs font-semibold shadow-sm">
                <Check className="w-3.5 h-3.5 text-emerald" /> Free Router
              </span>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-wrap items-center gap-4">
              <a
                href="#plans"
                className="px-6 py-3.5 bg-orange text-white font-bold text-sm rounded-lg hover:bg-orange-hover transition-all shadow-lg shadow-orange/30 min-w-[170px] text-center"
              >
                Explore Broadband Plans
              </a>
              <Link
                href="/new-connection.html"
                className="px-6 py-3.5 bg-white/10 backdrop-blur-md border border-white/60 text-white font-bold text-sm rounded-lg hover:bg-white hover:text-navy transition-all min-w-[160px] text-center"
              >
                Check Availability
              </Link>
            </div>
          </div>
        </div>

        {/* Layer 4: Floating Notification Badge (Desktop) */}
        <div className="hidden lg:flex items-center gap-3.5 absolute right-[6%] bottom-[22%] z-20 bg-white/95 backdrop-blur-md border border-white/90 rounded-2xl p-4 shadow-2xl max-w-xs animate-bounce-slow">
          <div className="w-11 h-11 rounded-xl bg-orange/10 text-orange flex items-center justify-center shrink-0">
            <Wifi className="w-6 h-6" />
          </div>
          <div>
            <div className="font-heading font-extrabold text-sm text-navy leading-snug">₹0 Installation &amp; Free Router</div>
            <div className="text-xs text-muted leading-tight mt-0.5">Dual-Band Wi-Fi 6 on commitments</div>
          </div>
        </div>

        {/* Layer 5: Curved Bottom Transition */}
        <div className="absolute bottom-0 left-0 right-0 w-full h-12 z-20 pointer-events-none overflow-hidden leading-none" aria-hidden="true">
          <svg viewBox="0 0 1440 48" preserveAspectRatio="none" fill="none" className="w-full h-full">
            <path d="M0,24 C480,48 960,48 1440,24 L1440,48 L0,48 Z" fill="#F7F8FC" />
          </svg>
        </div>
      </section>

      {/* Broadband Plans Section (Consumes data/plans.ts directly) */}
      <BroadbandPlans />

      {/* Long-Term Pricing Section (Consumes data/plans.ts directly) */}
      <LongTermPlans />

      {/* Interactive Booking & Lead Generation Section */}
      <section className="py-20 bg-background" id="booking">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
            <div className="lg:col-span-6">
              <span className="inline-block px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider bg-orange-tint text-orange-text mb-3">
                Doorstep Activation
              </span>
              <h2 className="text-3xl sm:text-4xl font-extrabold text-navy font-heading tracking-tight mb-4">
                Get Connected in 3 Simple Steps
              </h2>
              <p className="text-muted text-base mb-8">
                Our local Airoli technician will arrive with optical splicing equipment, complete neat cabling, set up your complimentary router, and verify live speed before payment.
              </p>

              <div className="space-y-6">
                <div className="flex gap-4 items-start">
                  <div className="w-8 h-8 rounded-full bg-navy text-white flex items-center justify-center font-bold text-sm flex-shrink-0">1</div>
                  <div>
                    <h4 className="font-bold text-navy text-sm">Choose Your Speed</h4>
                    <p className="text-xs text-muted">Select 100, 200, or 300 Mbps based on your family and streaming needs.</p>
                  </div>
                </div>
                <div className="flex gap-4 items-start">
                  <div className="w-8 h-8 rounded-full bg-orange text-white flex items-center justify-center font-bold text-sm flex-shrink-0">2</div>
                  <div>
                    <h4 className="font-bold text-navy text-sm">Submit Online Enquiry</h4>
                    <p className="text-xs text-muted">Share your contact number and Airoli building details with zero advance fee.</p>
                  </div>
                </div>
                <div className="flex gap-4 items-start">
                  <div className="w-8 h-8 rounded-full bg-emerald text-white flex items-center justify-center font-bold text-sm flex-shrink-0">3</div>
                  <div>
                    <h4 className="font-bold text-navy text-sm">Doorstep Installation &amp; Live Test</h4>
                    <p className="text-xs text-muted">Technician verifies full symmetrical speed on your smartphone before payment.</p>
                  </div>
                </div>
              </div>
            </div>

            <div className="lg:col-span-6">
              <EnquiryForm />
            </div>
          </div>
        </div>
      </section>

      {/* Section 11: Bespoke Purple Ribbon CTA Section */}
      <section className="relative bg-white py-20 px-6 overflow-hidden">
        <img
          src="/public/assets/images/cta-ribbon-left.svg"
          alt=""
          className="absolute -top-8 -left-10 w-72 md:w-96 h-auto pointer-events-none z-0"
          aria-hidden="true"
        />
        <img
          src="/public/assets/images/cta-ribbon-right.svg"
          alt=""
          className="absolute -bottom-8 -right-10 w-72 md:w-96 h-auto pointer-events-none z-0"
          aria-hidden="true"
        />
        <div className="relative z-10 max-w-xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 bg-[#F4EFFF] text-[#7C3AED] border border-[#E9D5FF] px-3.5 py-1.5 rounded-full text-xs font-semibold mb-5">
            <span className="w-2.5 h-2.5 rounded-full border border-[#7C3AED] flex items-center justify-center">
              <span className="w-1 h-1 rounded-full bg-[#7C3AED]"></span>
            </span>
            Reliable Fiber Broadband
          </div>
          <h2 className="text-3xl md:text-5xl font-medium tracking-tight text-[#111827] leading-tight mb-4">
            Ready for a Better<br />Internet Experience?
          </h2>
          <p className="text-sm md:text-base text-slate-500 max-w-lg mx-auto mb-8">
            Get connected with Sevenseas Broadband today. Pure optical fiber connectivity delivered straight to your door across Airoli.
          </p>
          <div className="flex flex-wrap items-center justify-center gap-3.5">
            <a
              href="tel:9664985535"
              className="inline-flex items-center justify-center gap-2 min-h-[48px] px-6 rounded-lg bg-gradient-to-r from-[#7C3AED] to-[#6D28D9] text-white font-medium text-sm shadow-md hover:shadow-lg transition-all"
            >
              Call Now
            </a>
            <a
              href="https://wa.me/919664985535?text=Hi%20Sevenseas%20Broadband,%20I%20am%20interested%20in%20a%20new%20connection"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center gap-2 min-h-[48px] px-6 rounded-lg bg-white border border-[#7C3AED] text-[#7C3AED] font-medium text-sm hover:bg-[#F4EFFF] transition-all"
            >
              WhatsApp Us
            </a>
          </div>
        </div>
      </section>

      {/* Structural Footer */}
      <footer className="bg-navy text-white pt-16 pb-12 border-t border-slate-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-10 mb-12">
            <div>
              <img
                src="/public/assets/images/logo-white.png"
                alt="Sevenseas Broadband"
                className="h-10 w-auto mb-4"
              />
              <p className="text-xs text-slate-300 leading-relaxed mb-4">
                Connecting Every Home. Certified residential optical fiber provider delivering unthrottled gigabit speeds.
              </p>
            </div>

            <div>
              <h4 className="text-sm font-bold text-white uppercase tracking-wider mb-4">Quick Links</h4>
              <ul className="space-y-2 text-xs text-slate-300">
                <li><Link href="/" className="hover:text-orange">Home</Link></li>
                <li><Link href="/about.html" className="hover:text-orange">About Us</Link></li>
                <li><Link href="/plans.html" className="hover:text-orange">Broadband Plans</Link></li>
                <li><Link href="/new-connection.html" className="hover:text-orange">Book Connection</Link></li>
              </ul>
            </div>

            <div>
              <h4 className="text-sm font-bold text-white uppercase tracking-wider mb-4">Fiber Plans</h4>
              <ul className="space-y-2 text-xs text-slate-300">
                <li>Starter 100 Mbps — ₹499/mo</li>
                <li>Popular 200 Mbps — ₹599/mo</li>
                <li>Premium 300 Mbps — ₹699/mo</li>
                <li>Long-Term Subscription Savings</li>
              </ul>
            </div>

            <div>
              <h4 className="text-sm font-bold text-white uppercase tracking-wider mb-4">Office &amp; Contact</h4>
              <ul className="space-y-2 text-xs text-slate-300">
                <li><strong>Helpline:</strong> +91 96649 85535 / +91 74002 22922</li>
                <li><strong>WhatsApp:</strong> +91 96649 85535</li>
                <li>Shop-1, Dharmjeevan CHS, near Railway Stn, Sector 3, Airoli, Navi Mumbai 400708</li>
              </ul>
            </div>
          </div>

          <div className="pt-8 border-t border-slate-800 text-center text-xs text-slate-400">
            © 2026 Sevenseas Broadband. All rights reserved. Registered under Department of Telecommunications (DoT).
          </div>
        </div>
      </footer>
    </main>
  );
}

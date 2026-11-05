import type { Metadata, Viewport } from "next";
import "./globals.css";
import React from "react";

export const viewport: Viewport = {
  themeColor: "#1E3050",
  width: "device-width",
  initialScale: 1,
  colorScheme: "light"
};

export const metadata: Metadata = {
  title: "Sevenseas Broadband — Fast Internet. Better Living.",
  description:
    "Experience high-speed residential fiber broadband with reliable connectivity, symmetrical gigabit speeds, and ₹0 installation in Airoli, Navi Mumbai.",
  metadataBase: new URL("https://sevenseasbroadband.in"),
  openGraph: {
    title: "Sevenseas Broadband — Connecting Every Home",
    description: "Reliable, unthrottled residential fiber broadband in Airoli, Navi Mumbai.",
    url: "https://sevenseasbroadband.in",
    siteName: "Sevenseas Broadband",
    images: [
      {
        url: "/public/assets/images/hero-family.jpg",
        width: 1200,
        height: 675,
        alt: "Sevenseas Broadband Family Internet"
      }
    ],
    locale: "en_IN",
    type: "website"
  },
  robots: {
    index: true,
    follow: true
  },
  icons: {
    icon: "/public/assets/images/favicon.svg"
  }
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap"
          rel="stylesheet"
        />
        <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
      </head>
      <body className="min-h-screen flex flex-col bg-background text-ink antialiased">
        {/* Topbar */}
        <div className="bg-navy text-white text-xs py-2 px-4 border-b border-white/10">
          <div className="max-w-7xl mx-auto flex justify-between items-center">
            <div className="flex items-center gap-4">
              <span>Helpline: <a href="tel:9664985535" className="font-bold text-orange hover:underline">+91 96649 85535</a> / <a href="tel:7400222922" className="hover:underline">+91 74002 22922</a></span>
              <a href="https://wa.me/919664985535" target="_blank" rel="noopener noreferrer" className="text-emerald hover:underline hidden sm:inline">WhatsApp Desk</a>
            </div>
            <div className="flex items-center gap-4 text-slate-300">
              <span>Sector 3, Airoli, Navi Mumbai</span>
            </div>
          </div>
        </div>

        {children}

        {/* Mobile Sticky Action Bar */}
        <aside className="fixed bottom-0 left-0 right-0 z-50 bg-white border-t border-slate-200 px-3 py-2 pb-[calc(0.5rem+env(safe-area-inset-bottom,0px))] shadow-[0_-4px_20px_rgba(15,27,45,0.1)] md:hidden" aria-label="Quick mobile contact actions">
          <div className="grid grid-cols-[1fr_1fr_1.35fr] gap-2 max-w-md mx-auto">
            <a
              href="tel:9664985535"
              className="inline-flex items-center justify-center gap-1.5 min-h-[44px] px-2 py-2 rounded-lg bg-slate-100 text-navy font-heading text-xs font-bold border border-navy/15 active:bg-navy active:text-white"
              aria-label="Call Customer Care 9664985535"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
              <span>Call</span>
            </a>
            <a
              href="https://wa.me/919664985535?text=Hi%20Sevenseas%20Broadband,%20I%20am%20interested%20in%20a%20new%20fiber%20connection"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center gap-1.5 min-h-[44px] px-2 py-2 rounded-lg bg-emerald/10 text-emerald-text font-heading text-xs font-bold border border-emerald/25 active:bg-emerald active:text-white"
              aria-label="Chat with Sevenseas on WhatsApp"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
              <span>WhatsApp</span>
            </a>
            <a
              href="/#new-connection"
              className="inline-flex items-center justify-center gap-1.5 min-h-[44px] px-2 py-2 rounded-lg bg-orange text-white font-heading text-xs font-bold shadow-sm active:bg-orange-hover"
              aria-label="Get Connected Online"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              <span>Get Connected</span>
            </a>
          </div>
        </aside>
      </body>
    </html>
  );
}

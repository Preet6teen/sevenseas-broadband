import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./data/**/*.{js,ts,jsx,tsx,mdx}"
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          DEFAULT: "#1E3050",
          hover: "#152238",
          tint: "#EBF0F7"
        },
        orange: {
          DEFAULT: "#F57C00",
          hover: "#D66C00",
          text: "#B85600",
          tint: "#FFF3E5"
        },
        emerald: {
          DEFAULT: "#0F9D75",
          hover: "#0D8563",
          text: "#0B7A5C",
          tint: "#E6F6F0"
        },
        violet: {
          DEFAULT: "#5B3FD1",
          hover: "#492FB5",
          tint: "#EEEBFB"
        },
        background: "#F7F8FC",
        surface: "#FFFFFF",
        ink: "#0F1B2D",
        muted: "#5B6B82",
        border: "#E3E8F0",
        danger: {
          DEFAULT: "#D9261C",
          tint: "#FDF2F2"
        }
      },
      fontFamily: {
        heading: ["Space Grotesk", "sans-serif"],
        body: ["Inter", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "sans-serif"]
      },
      boxShadow: {
        sm: "0 1px 3px rgba(15, 27, 45, 0.05)",
        md: "0 4px 16px rgba(15, 27, 45, 0.08)",
        lg: "0 12px 32px rgba(15, 27, 45, 0.12)",
        focus: "0 0 0 3px rgba(91, 63, 209, 0.25)"
      },
      borderRadius: {
        sm: "6px",
        md: "10px",
        lg: "16px",
        pill: "9999px"
      }
    }
  },
  plugins: []
};

export default config;

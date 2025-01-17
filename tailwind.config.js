/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/**/*.js",
  ],
  theme: {
    extend: {
      container: {
        center: true,
        padding: '1rem',
      },
      fontFamily: {
        sans: ['Inter', 'Helvetica', 'Arial', 'sans-serif'],
        serif: ['Merriweather', 'Georgia', 'serif'],
        mono: ['Source Code Pro', 'Courier New', 'monospace'],
      },
      colors: {
        userBubble: '#f3f4f6', // Gris claro
        assistantText: '#1f2937', // Gris oscuro
        textBlue: '#1d4ed8',
        textGray: '#4b5563',
        accentColor: '#0ea5e9',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('daisyui'),
  ],
  daisyui: {
    themes: [
      {
        light: {
          ...require("daisyui/src/theming/themes")["light"],
          primary: "#1d4ed8",
          secondary: "#4b5563",
          accent: "#0ea5e9",
        },
      },
    ],
  },
}


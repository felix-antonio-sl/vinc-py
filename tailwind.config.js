/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
    // Otros paths según tu estructura
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}


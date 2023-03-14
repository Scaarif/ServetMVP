/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    // specify sizes meaning
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl:'1440px'
    },
    extend: {
      // specify (define) custom colors (3 variants of blue) + white
      colors: {
        NormalBage:'F3ECD1',
        ActiveBage: 'E9D89D',
        CardGray: '7A7A7A',
        CardBorderGray: 'B5B5B5',
        // zenith features
        HeaderBlue: '#4D9DCA',
        ActiveBlue: '#52A4D2',
        SidebarBlue: '#EBF4F9',
        ProfileBlue: '#B1D5E8'
      }

    },
  },
  plugins: [
    require('@tailwindcss/forms'), // to include tailwind forms ...
  ],
}


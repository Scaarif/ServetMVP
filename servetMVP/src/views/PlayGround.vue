<template>
  <div class="flex items-center">
    <h1>Let's play... Well, take a tour!</h1>
    <div class="flex flex col items-center">
      <select v-model="selectedCountry">
      <option value="">Select a country</option>
      <option v-for="country, idx in countries" :key="idx" :value="country.id">{{ country.name }}</option>
    </select>
    <select v-model="selectedCounty" v-if="selectedCountry">
      <option value="">Select a county/state</option>
      <option v-for="county, idx in counties" :key="idx" :value="county.id">{{ county.name }}</option>
    </select>
    <select v-model="selectedLocale" v-if="selectedCounty">
      <option value="">Select a locale</option>
      <option v-for="locale, idx in locales" :key="idx" :value="locale.id">{{ locale.name }}</option>
    </select>
    </div>
  </div>
</template>
<script>
export default {
   data() {
      return {
         selectedCountry: null,
         selectedCounty: null,
         selectedLocale: null,
         countries: [],
         counties: [],
         locales: []
      }
   },
   mounted() {
      fetch('/api/countries')
         .then(response => response.json())
         .then(data => {
            this.countries = data
         })
   },
   watch: {
      selectedCountry(countryId) {
         if (!countryId) return
         fetch(`/api/countries/${countryId}/counties`)
            .then(response => response.json())
            .then(data => {
            this.counties = data
            })
      }
   },

}
</script>
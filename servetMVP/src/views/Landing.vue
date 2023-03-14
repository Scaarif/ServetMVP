<template>
    <div class="flex flex-col items-center w-full">
       <div class="flex flex-col items-center space-y-2 py-4 space">
            <span class="text-[40px] font-medium max-w-xl w-full text-center">Welcome to Servet, the market place for services</span>
            <span class="text-md max-w-lg text-center">Browse for the service you need and get connected to the provider instantly</span>
       </div>
       <div class="w-full px-32 flex items-center justify-between mt-32 mb-8">
            <span class="text-lg py-2 border-b border-transparent transition-all hover:border-slate-900 cursor-pointer">
                New to the site? Take an interactive tour
            </span>
            <span class="text-lg text-slate-700">or</span>
            <span class="text-lg">Choose your location to start
                <select class="text-lg rounded-sm ring-0 border-none active:border-none active:ring-0 hover:ring-0
                    hover:border-none select:ring-0 select:border-none"
                    v-model="location"
                    @change="setLocation"
                >
                    <option value="kenya">Kenya</option>
                    <option value="Nigeria">Nigeria</option>
                </select>
            </span>
       </div>
       <div class="self-end mr-64 text-slate-700 mb-16">optionally</div>
       <div class="self-end mr-48 text-slate-700 mb-32 bg-[#F3ECD1] px-16 py-2 transition-all hover:bg-[#E9D89D]">Login</div>
    </div>
</template>
<script>

export default {
    data() {
        return {
            location: 'kenya',
            selectedLocation: '',
        }
    },
    methods: {
        setLocation() {
            this.selectedLocation = this.location
            console.log('selectedLocation: ', this.selectedLocation)
            // redirect to services page (read more on $router controls and guards)
            this.$router.push({name: 'services'})
        }
    }
}
</script>

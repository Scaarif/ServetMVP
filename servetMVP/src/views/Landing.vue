<template>
    <div class="flex flex-col items-center w-full h-full">
       <div class="flex flex-col items-center space-y-2 py-4 space">
            <span class="text-[26px] md:text-[40px] font-medium max-w-xl w-full text-center">Welcome to Servet, the market place for services</span>
            <span class="text-md max-w-md text-center">Browse for the service you need and get connected to the provider instantly</span>
       </div>
       <div class="w-full flex flex-col items-center justify-center space-y-2 md:space-y-4 lg:space-y-0 lg:flex-row lg:px-32 lg:justify-between mt-32 mb-16">
            <span class="text-md md:text-lg py-2 border-b border-transparent transition-all hover:border-slate-900 cursor-pointer">
                New to the site? Take an interactive tour
            </span>
            <span class="text-md md:text-lg text-slate-700">or</span>
            <span class="text-md md:text-lg text-center">Choose your location to start
                <select class="w-[10rem] ring-0 bg-gray-50 border-slate-300 rounded focus:ring-0 focus:border-slate-400"
                    v-model="location"
                    @change="setLocation"
                    v-if="location === 'Country'"
                >
                    <option value="Country">Country</option>
                    <option value="kenya">Kenya</option>
                    <option value="nigeria">Nigeria</option>
                   
                </select> 
                <!-- select county/state -->
                <select name="" id="counties" v-if="selectedLocation && region === 'County'"
                    v-model="region" @change="setRegion"
                    class="w-[10rem] border-slate-300 bg-gray-50 rounded focus:border-slate-400 focus:ring-0"
                    >
                    <option value="County">County</option>
                    <option v-for="region, idx in Object.values(regions)[0]" :key="idx" :value=region>{{ region.name }}</option>
                </select>
                <!-- select subcounty/locale -->
                <select name="" id="" v-if="selectedState" v-model="locale" @change="setLocale"
                    class="w-[10rem] border-slate-300 bg-gray-50 rounded focus:border-slate-400 focus:ring-0"
                    >
                    <option value="Sub County">Sub County</option>
                    <!-- <option v-for="locale, idx in selectedState.sub_counties" :key="idx" :value=locale>{{ locale }}</option> -->
                    <option v-for="locale, idx in sub_counties" :key="idx" :value=locale>{{ locale }}</option>
                </select>
            </span>
       </div>
       <div class="text-center lg:self-end lg:mr-64 text-slate-700 mb-16">optionally</div>
       <router-link :to="{name: 'login'}" class="text-center lg:self-end lg:mr-48 mb-32 bg-NormalBage px-16
            py-2 md:px-20 font-medium transition-all hover:bg-ActiveBage">Login</router-link>
    </div>
</template>
<script>
import { mapState, mapMutations, mapActions } from 'vuex';
import axios from 'axios';
import ke_counties from '../kenyan_counties.json'; 

export default {
    data() {
        return {
            location: 'Country',
            selectedLocation: '',
            queue: [],
            regions: [],
            done: false,
            region: 'County',
            selectedState: '',
            sub_counties: null,
            locale: 'Sub County',
        }
    },
    created() {
        // fetch locations
        this.fetchLocations([1, 5])
    },
    computed: {
        ...mapState(['isLanding'])
    }, 
    methods: {
        ...mapMutations(['toggleIsLanding', 'setCounties', 'setSelectedLocation']),
        ...mapActions(['fetchServices', 'fetchLocations']),
        setLocation() {
            if (this.location !== 'Country') {
                this.selectedLocation = this.location
                console.log('selectedLocation: ', this.selectedLocation)
                this.toggleIsLanding()
                this.allRegions()
            }
        },
        createQueue() {
            let reqs = this.selectedLocation === 'kenya' ? 5 : 4
            for (let i = 0; i < reqs; i++)
                this.queue.push((i * 10).toString())
            console.log('created queue: ' + this.queue, this.queue.length)
        },
        setRegions(regions) {
            // console.log(regions)
            this.regions.push(regions);
            console.log('so far: ', this.regions)
            if (this.selectedLocation === 'nigeria')
                console.log('first: ', Object.values(this.regions)[0][0], Object.values(this.regions)[0][0].uri)
            else
            console.log('first: ', Object.values(this.regions)[0][0])
        },
        async setRegion() {
            this.selectedState = this.region
            if (this.selectedLocation === 'kenya')
                this.sub_counties = this.selectedState.sub_counties
            else {
                const res = await axios.get(this.selectedState.uri)
                this.sub_counties = res.data.lgas
                console.log('sub_counties: ', this.sub_counties, Object.keys(this.sub_counties))
            } 
            // console.log(this.selectedState + 'with subcounties: ' + this.selectedState.sub_counties)
        },
        setLocale() {
            console.log(this.locale)
            // fetch services based on location (& currently, service_category)
            const country_id = this.selectedLocation === 'kenya' ? '1' : '2'
            const queryStr = '?country=' + country_id + '&service_category=2'
            // const queryStr = '?country=' + '2' + '&service_category=1'
            // console.log(queryStr)
            this.fetchServices(queryStr)
            // redirect to services page
            this.$router.push({name: 'services'})
            this.setSelectedLocation([this.selectedState.name, this.locale])
        },
        toggleDone() {
            const len = this.selectedLocation === 'kenya' ? 47 : 36
            if (this.selectedState && !this.done) {
                this.done = !this.done
            }
        },
        // get states/counties in country
        async allRegions() {
            let res;
            if (this.selectedLocation === 'nigeria') {
                res = await axios.get('https://api.facts.ng/v1/states')
                if (res !== null) {
                    console.log('nigeria states: ', res)
                    this.setRegions(res.data)
                }
            }
            else {
                res = ke_counties
                // console.log('ke_counties: ', ke_counties)
                this.setRegions(res)
            }
        },
    },
}
</script>
<template>
    <div class="flex flex-col items-center w-full h-full">
       <div class="flex flex-col items-center space-y-2 py-4 space">
            <span class="text-[40px] font-medium max-w-xl w-full text-center">Welcome to Servet, the market place for services</span>
            <span class="text-md max-w-md text-center">Browse for the service you need and get connected to the provider instantly</span>
       </div>
       <div class="w-full px-32 flex items-center justify-between mt-32 mb-16">
            <span class="text-lg py-2 border-b border-transparent transition-all hover:border-slate-900 cursor-pointer">
                New to the site? Take an interactive tour
            </span>
            <span class="text-lg text-slate-700">or</span>
            <span class="text-lg">Choose your location to start
                <select class="w-[10rem] ring-0 border-slate-300 rounded focus:ring-0 focus:border-slate-400"
                    v-model="location"
                    @change="setLocation"
                    v-if="location === 'Country'"
                >
                    <option value="Country">Country</option>
                    <option value="kenya">Kenya</option>
                    <option value="nigeria">Nigeria</option>
                   
                </select> 
                <!-- select county/state -->
                <select name="" id="" v-if="Object.values(regions).length && region === 'County'"
                    v-model="region" @change="setRegion"
                    class="w-[10rem] border-slate-300 rounded focus:border-slate-400 focus:ring-0 overflow-hidden"
                    >
                    <option value="County">County</option>
                    <option v-for="region, idx in Object.values(regions)[0]" :key="idx" :value=region>{{ region.name }}</option>
                </select>
                <!-- select subcounty/locale -->
                <select name="" id="" v-if="selectedState" v-model="locale" @change="setLocale"
                    class="w-[10rem] border-slate-300 rounded focus:border-slate-400 focus:ring-0"
                    >
                    <option value="Sub County">Sub County</option>
                    <!-- <option v-for="locale, idx in selectedState.sub_counties" :key="idx" :value=locale>{{ locale }}</option> -->
                    <option v-for="locale, idx in sub_counties" :key="idx" :value=locale>{{ locale }}</option>
                </select>
            </span>
       </div>
       <div class="self-end mr-64 text-slate-700 mb-16">optionally</div>
       <router-link :to="{name: 'login'}" class="self-end mr-48 mb-32 bg-NormalBage px-16
            py-2 font-medium transition-all hover:bg-ActiveBage">Login</router-link>
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
    computed: {
        ...mapState(['isLanding'])
    }, 
    methods: {
        ...mapMutations(['toggleIsLanding', 'setCounties']),
        ...mapActions(['fetchServices']),
        setLocation() {
            if (this.location !== 'Country') {
                this.selectedLocation = this.location
                console.log('selectedLocation: ', this.selectedLocation)
                this.toggleIsLanding()
                // create a queue
                // this.createQueue()
                // get the regions (state/county) in country
                this.allRegions()
                // redirect to services page (read more on route control/protection and guards)
                // if (this.done)
                //     this.$router.push({name: 'services'})
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
                const res = await axios.get(`https://api.facts.ng/v1/states/${this.selectedState}`)
                this.sub_counties = res.data
                console.log('sub_counties: ', this.sub_counties)
            } 
            // console.log(this.selectedState + 'with subcounties: ' + this.selectedState.sub_counties)
        },
        setLocale() {
            console.log(this.locale)
            // fetch services based on location (& currently, service_category)
            const country_id = this.selectedLocation === 'kenya' ? '1' : '2'
            const queryStr = '?country=' + country_id + '&service_category=1'
            // const queryStr = '?country=' + '2' + '&service_category=1'
            console.log(queryStr)
            this.fetchServices(queryStr)
            // redirect to services page
            this.$router.push({name: 'services'})
        },
        toggleDone() {
            const len = this.selectedLocation === 'kenya' ? 47 : 36
            if (this.selectedState && !this.done) {
                this.done = !this.done
            }
        },
        // get states/counties in country
        async allRegions() {
            // const countryCode = this.selectedLocation === 'kenya' ? 'KE' : 'NG';
            // const options = {
            // method: 'GET',
            // url: 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries/' + countryCode + '/regions',
            // params: {limit: '50'},
            // headers: {
            //     'X-RapidAPI-Key': '080ce19c49msh6a7e158b86a77ebp11b231jsnc312862eade4',
            //     'X-RapidAPI-Host': 'wft-geo-db.p.rapidapi.com'
            // }
            // };

            // options.params['offset'] = this.queue.shift()
            // console.log('queue length' + this.queue.length, 'offset ->' + options.params.offset)
            let res;
            // res = await axios.request(options).then(function (response) {
            //     // console.log(response.data.data);
            //     return response.data.data;
            // }).catch(function (error) {
            //     console.error(error);
            //     return {'status': 400}
            // });
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
            // if (res !== null) {
            //     // console.log(res)
            //     this.setRegions(res.data)
            // }
            // delay subsequent requests by 1 second
            // if (this.queue.length > 0) {
            //     setTimeout(this.allRegions, 2000)
            // } else {
            //     this.toggleDone()
            //     this.setCounties(this.regions)
            // }
        },
    },
}
</script>

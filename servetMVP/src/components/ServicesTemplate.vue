<template>
    <div class="w-full flex flex-col items-center">
        <!-- header (slogan & filter bar) -->
        <div class="w-full flex flex-col space-y-2 items-center md:flex-row md:justify-between md:space-y-0 px-8 mb-8">
            <span class="max-w-sm w-full capitalize">
                <select
                    class="w-full text-sm max-w-md text-start border-slate-300 rounded-md focus:ring-0 focus:border-slate-400 capitalize"
                    v-model="s_category">
                    <option :value="s_category" class="text-sm capitalize">{{ s_category }}</option>
                    <option v-for="category in categories" :key="category.id" :value="category.id">{{category.name}}</option>
                </select>
            </span>
            <span class="text-md text-slate-900 font-medium flex sm:flex-col md:flex-row
                md:items-center md:space-x-2">
                <span>Filter services by</span>
                <span class="border rounded bg-white">
                <select class="text-sm rounded-sm ring-0 border-none focus:border-slate-none focus:ring-0 capitalize"
                    v-model="country"
                    @change="setStates"
                >
                    <option value="country">Country</option>
                    <option v-for="id, country in countries" :key="id" :value="id">{{ country }}</option>
                </select>
                <select class="text-sm rounded-sm ring-0 border-none focus:border-slate-none focus:ring-0 capitalize"
                    v-model="state"
                    @change="setLocations"
                >
                    <option value="state">State</option>
                    <option v-for="state in states.states" :key="state.id" :value="state.id">{{ state.name }}</option>
                </select>
                <select class="text-sm rounded-sm ring-0 border-none focus:border-slate-none focus:ring-0 capitalize"
                    v-model="location"
                    @change="setServices"
                >
                    <option value="location">Location</option>
                    <option v-for="loc in locations.locations" :key="loc.id" :value="loc.id">{{ loc.name }}</option>
                </select>
            </span>
            </span>
        </div>
        <!-- services display -->
        <span v-if="!isAuthorized" class="self-start text-slate-900 text-lg font-bold ml-4"
        >Most popular at {{ d_location.locale }}, {{ d_location.county }}</span>
        <span v-else class="md:self-start text-slate-900 text-lg font-bold ml-4"
        >Most popular in relation to your previous searches</span>
        <div class="w-full flex items-center mt-8 flex-wrap px-8 sm:justify-center" v-if="fetched">
            <!-- <ServiceCard v-for="service, idx in dummy_services" :key="idx" @click="toggleShowService(2, csrfToken, '')" /> -->
            <ServiceCard v-for="service, idx in Object.values(getServices)" :key="idx" 
                :service="service"
                @click="toggleShowService(service.sps_id, csrfToken, '')" />
        </div>
        <div class="w-full flex items-center mt-8 flex-wrap px-8 sm:justify-center" v-else>
            <span>We have no {{ categories.filter((cat) => cat.id === s_category).name }} services registered from this location</span>
        </div>
        <!-- see more -->
        <span v-if="getServices.length > 6" class="self-end text-slate-900 text-md border-b border-transparent p-2 mb-16
            mr-8 transition-all hover:border-slate-800 cursor-pointer" @click="loadMore">
            see more ...
        </span>
        <div v-if="showService" class="absolute top-0 z-5 w-full bg-gray-50">
            <Service :serviceDets="getService || d_service" :id="currentService_id"/>
        </div>
    </div>
</template>
<script>
import ServiceCard from './ServiceCard.vue';
import Service from './Service.vue';
import httpClient from '../httpClient';
import config from '../config';


import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';

export default {
    data() {
        return {
            s_category: 'select service category',
            country:'country',
            state:'state',
            location:'location',
            providerName: '',
            d_location: {'county': 'Nairobi', 'locale': 'CBD'},
            dummy_services: ['some service', 'some', 'test service', 'test wrapping', 'another', 'see'],
            // services: '',
            d_service: {'description': 'test description', 'first_name': 'test', 'last_name': 'testLast', 'rating': 2, 'reviews': [{'content': 'test review', 'customer_first_name': 'test', 'customer_last_name':'test'}]},
            fetched: false,
        }
    },
    computed: {
        ...mapState(['showService', 'services', 'isAuthorized', 'csrfToken', 'currentService_id', 'categories', 'countries', 'states', 'locations']),
        ...mapGetters(['getService', 'getServices']),
    },
    components: {
        ServiceCard,
        Service,
    },
    created() {
        this.getCategories() // fetch service categories
        if (Object.values(this.getServices).length > 0)
            this.fetched = true
    },
    updated(){
        if (this.fetched) {
            console.log('fetched: ', this.fetched)
        }
    },
    methods: {
        ...mapMutations(['toggleShowService', 'setCategories', 'setSelectedLocation']),
        ...mapActions(['getCategories', 'fetchLocations', 'fetchStates', 'fetchServices',]),
        setStates() {
           this.fetchStates(this.country)
        },
        setLocations() {
            console.log('state_id: ', this.state)
            this.fetchLocations([this.country, this.state])
        },
        async setServices() {
            this.fetched = false; // start off as false
            let queryStr;
            if (this.s_category !== 'select service category')
                queryStr = '?country=' + this.country + '&service_category=' + this.s_category
            else
                queryStr = '?country=' + this.country + '&service_category=2' 
            queryStr += '&state=' + this.state + '&location=' + this.location
            // set the location to this selected:
            let state_name = Object.values(this.states.states.filter((state) => state.id === this.state))[0].name
            let location_name = Object.values(this.locations.locations.filter((loc) => loc.id === this.location))[0].name
            // console.log('current state: ', state_name, '& location: ', location_name)
            this.setSelectedLocation([state_name, location_name])
            await this.fetchServices(queryStr)
            if (Object.values(this.getServices).length > 0) {
                this.fetched = true
                console.log('fetched services: ', this.getServices, ' for the location: ', state_name, ' at ', location_name)
            } else {
                console.log('no services based on metrics')
            }
            
        },
        loadMore() {
            // console.log('loaded services: ', this.services.services[0])
            console.log('loaded services: ', this.getServices)
        },
    }
}
</script>
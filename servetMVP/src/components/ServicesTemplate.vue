<template>
    <div class="w-full flex flex-col items-center">
        <!-- header (slogan & filter bar) -->
        <div class="w-full flex flex-col space-y-4 items-center md:flex-row md:justify-between px-8 mb-8">
            <input v-if="isAuthorized"
                class="w-full text-sm max-w-md text-center border-slate-300 rounded-md focus:ring-0 focus:border-slate-400"
                type="text" placeholder="Search for service by provider username"
                v-model="providerName" @keypress.enter="searchServices">
                <!-- placeholder inline block (to maintain layout i.e. filter bar on the right end) -->
            <span v-else class="text-md"></span>
            <span class="text-md text-slate-900 font-medium">Filter services by
                <select class="text-sm rounded-sm ring-0 border-none focus:border-none focus:ring-0 hover:ring-0
                    hover:border-none capitalize"
                    v-model="metrics"
                    @change="setFilterMetrics"
                >
                    <option value="filterMetrics">Filter Metrics</option>
                    <option value="service category">service category</option>
                    <option value="location">location</option>
                </select>
            </span>
        </div>
        <!-- services display -->
        <span v-if="!isAuthorized" class="self-start text-slate-900 text-lg font-bold ml-4"
        >Most popular at {{ location.locale }}, {{ location.county }}</span>
        <span v-else class="md:self-start text-slate-900 text-lg font-bold ml-4"
        >Most popular in relation to your previous searches</span>
        <div class="w-full flex items-center mt-8 flex-wrap px-8 sm:justify-center">
            <!-- <ServiceCard v-for="service, idx in dummy_services" :key="idx" @click="toggleShowService(2, csrfToken, '')" /> -->
            <ServiceCard v-for="service, idx in Object.values(getServices)" :key="idx" 
                :service="service"
                @click="toggleShowService(service.sps_id, csrfToken, '')" />
        </div>
        <!-- see more -->
        <span v-if="getServices.length > 6" class="self-end text-slate-900 text-md border-b border-transparent p-2 mb-16
            mr-8 transition-all hover:border-slate-800 cursor-pointer" @click="loadMore">
            see more ...
        </span>
        <div v-if="showService" class="absolute top-0 z-5 w-full bg-gray-50">
            <Service :serviceDets="getService || service" :id="service.sps_id"/>
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
            metrics: 'filterMetrics',
            providerName: '',
            searchMetrics: '',
            location: {'county': 'Nairobi', 'locale': 'CBD'},
            dummy_services: ['some service', 'some', 'test service', 'test wrapping', 'another', 'see'],
            // services: '',
            service: {'description': 'test description', 'first_name': 'test', 'last_name': 'testLast', 'rating': 2, 'reviews': [{'content': 'test review', 'customer_first_name': 'test', 'customer_last_name':'test'}]}
        }
    },
    computed: {
        ...mapState(['showService', 'services', 'isAuthorized', 'csrfToken']),
        ...mapGetters(['getService', 'getServices']),
    },
    components: {
        ServiceCard,
        Service,
    },
    created() {
        console.log('load categories: ', this.getCategories())
    },
    methods: {
        ...mapMutations(['toggleShowService', 'setCategories']),
        // ...mapActions(['fetchServices']),
        setFilterMetrics() {
            this.searchMetrics = this.metrics
           console.log('searchMetrics ->', this.searchMetrics)
        },
        searchServices() {
            console.log('Searching for services by ->', this.providerName)
        },
        loadMore() {
            // console.log('loaded services: ', this.services.services[0])
            console.log('loaded services: ', this.getServices)
        },
        async getCategories() {
            const res = await httpClient.loggedOutGet(config.DEFAULT + '/serviceCategories')
            // console.log(res.data)
            if (res.data.length && res.status === 200)
                this.setCategories(res.data)
        },
    }
}
</script>
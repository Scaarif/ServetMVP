<template>
    <div class="w-full flex flex-col items-center">
        <!-- header (slogan & filter bar) -->
        <div class="w-full flex items-center justify-between px-8 mb-8">
            <input v-if="token"
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
        <span v-if="!token" class="self-start text-slate-900 text-lg font-bold ml-4"
        >Most popular at {{ location.locale }}, {{ location.county }}</span>
        <span v-else class="self-start text-slate-900 text-lg font-bold ml-4"
        >Most popular in relation to your previous searches</span>
        <div class="w-full flex items-center mt-8 flex-wrap px-8">
            <ServiceCard v-for="service, idx in dummy_services" :key="idx" @click="toggleShowService" />
        </div>
        <!-- see more -->
        <span class="self-end text-slate-900 text-md border-b border-transparent p-2 mb-16
            mr-8 transition-all hover:border-slate-800 cursor-pointer" @click="loadMore">
            see more ...
        </span>
        <div v-if="showService" class="absolute top-0 z-5 w-full bg-gray-50">
            <Service />
        </div>
    </div>
</template>
<script>
import ServiceCard from './ServiceCard.vue';
import Service from './Service.vue';


import { mapState, mapGetters, mapMutations } from 'vuex';

export default {
    data() {
        return {
            metrics: 'filterMetrics',
            providerName: '',
            searchMetrics: '',
            location: {'county': 'Nairobi', 'locale': 'CBD'},
            dummy_services: ['some service', 'some', 'test service', 'test wrapping', 'another', 'see'],
        }
    },
    computed: {
        ...mapState(['showService', 'token', 'services']),
        ...mapGetters(['getService', 'getServices']),
    },
    components: {
        ServiceCard,
        Service,
    },
    methods: {
        ...mapMutations(['toggleShowService']),
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
        }
    }
}
</script>
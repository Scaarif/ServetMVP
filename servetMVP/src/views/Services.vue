<template>
    <div class="w-full flex flex-col items-center">
        <!-- header (slogan & filter bar) -->
        <div class="w-full flex items-center justify-between px-8 mb-8">
            <span class="text-md max-w-md text-center">
                Browse for the service you need and get connected to the provider instantly
            </span>
            <span class="text-md font-medium">Filter services by
                <select class="text-sm rounded-sm ring-0 border-none active:border-none active:ring-0 hover:ring-0
                    hover:border-none select:ring-0 select:border-none capitalize"
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
        <span class="self-start text-slate-900 text-lg font-bold ml-4">Most popular at {{ location.locale }}, {{ location.county }}</span>
        <div class="w-full flex items-center mt-8 flex-wrap px-8">
            <ServiceCard v-for="service, idx in services" :key="idx" @click="toggleShowService" />
        </div>
        <!-- see more -->
        <span class="self-end text-slate-900 text-md border-b border-transparent p-2 mb-16
            mr-8 transition-all hover:border-slate-800 cursor-pointer">
            see more ...
        </span>
        <div v-if="showService" class="absolute top-0 z-5 w-full bg-gray-50">
            <Service />
        </div>
    </div>
</template>
<script>
import ServiceCard from '../components/ServiceCard.vue';
import Service from '../components/Service.vue';


import { mapState, mapMutations } from 'vuex';

export default {
    data() {
        return {
            metrics: 'filterMetrics',
            location: {'county': 'Nairobi', 'locale': 'CBD'},
            services: ['some service', 'some', 'test service', 'test wrapping', 'another', 'see'],
        }
    },
    computed: {
        ...mapState(['showService']),
    },
    components: {
        ServiceCard,
        Service,
    },
    methods: {
        ...mapMutations(['toggleShowService']),
        setFilterMetrics() {
           console.log('searchMetrics')
        }
    }
}
</script>
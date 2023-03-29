<template>
    <div class="w-full flex flex-col space-y-4 p-4 pb-16">
       <!-- Provider services (folded up) -->
       <div class="w-full flex flex-col space-y-2 border p-4 rounded">
            <div class="flex space-x-2 items-center relative mb-4">
                <span class="text-lg font-medium">My Services</span>
                <span class="absolute top-1 left-28" @click="toggleshowPending">
                    <svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18.5 9L12.5 15L6.5 9" stroke="black" stroke-width="2"/>
                    </svg>
                </span>
                <span class="absolute right-0 px-8 py-2 rounded-sm text-sm font-medium bg-[#F3ECD1]
                    transition-all hover:bg-[#E9D89D] cursor-pointer capitalize" @click="toggleProviderShopping"
                >See all Services</span>
            </div>
            <!-- the services -->
            <div v-show="showPending" class="flex flex-wrap">
                <!-- a service -->
                <div v-for="service, idx in services" :key="idx"
                    class="w-full md:w-1/2 flex items-center justify-between p-4 mb-2 mr-2 border rounded-sm bg-gray-100">
                    <span class="text-md font-medium">Some Service</span>
                    <div class="flex items-center">
                        <span class="text-sm px-3 py-1 border border-[#F3ECD1] bg-[#F3ECD1] cursor-pointer transition-all
                            hover:bg-[#E9D89D] capitalize" @click="toggleShowModal(), setServiceId(4)">edit</span>
                        <span class="text-sm border-y border-r border-[#F3ECD1] px-2 py-1 cursor-pointer transition-all
                            hover:bg-[#E9D89D] capitalize">delete</span>
                    </div>
                </div>
                <span class="md:w-1/2 w-full px-8 py-2 rounded-sm text-md font-medium text-center bg-[#F3ECD1]
                    transition-all hover:bg-[#E9D89D] cursor-pointer capitalize" @click="toggleShowModal"
                >add a new Service</span>
            </div>
       </div>
       <!-- Service Modification & Creation Modal -->
       <NewAndEditService v-if="showModifyServiceModal" :toggle="toggleShowModal" :id="serviceId" :setServiceId="setServiceId"/>
       <!-- Analytics (table) -->
       <div class="flex flex-col space-y-2 p-4 pb-6 border rounded">
            <span class="text-lg font-medium mb-4">Analytics</span>
            <table class="md:max-w-lg w-full">
                <thead class="bg-gray-100">
                    <tr>
                        <th class="border text-start p-2">Service</th>
                        <th class="border text-start p-2">Avg Rating</th>
                        <th class="border text-start p-2">Reviews</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="i in (1, 4)" :key="i">
                        <td class="border pl-4 py-1">Some Service</td>
                        <td class="border pl-4 py-1">{{ i + 1 }}</td>
                        <td class="border pl-4 py-1">{{ i }}</td>
                    </tr>
                </tbody>
            </table>
       </div>
       <!-- Analytics (graphs) -->
       <div class="flex flex-col space-y-2 border p-4 pb-6 rounded">
            <span class="text-lg font-medium mb-4">Comparative graphs</span>
            <div class="flex flex-col border py-12 px-4 bg-gray-100">
                <span class="w-1/2 text-sm text-slate-600">This' the comparative graph section (not sure yet how to do it - maybe canva? Is it that time now?)</span>
               <AnalyticsCopy />
            </div>
       </div>
       <!-- All services page (with all capabilities, similar to a customer - they too can shop/browse services) -->
       <AllServicesAlt v-if="provider_shopping"/>
    </div>
</template>
<script>
import NewAndEditService from './NewAndEditService.vue'
import AnalyticsCopy from './Analytics copy.vue'
import AllServicesAlt from './AllServicesAlt.vue'

import { mapMutations, mapState } from 'vuex'


export default {
    data() {
        return {
            showPending: true,
            services: ['some service', 'test service'],
            showModifyServiceModal: false,
            serviceId: '',
        }
    },
    components: {
        NewAndEditService,
        AnalyticsCopy,
        AllServicesAlt,
    },
    created() {
        console.log('loading my services')
        this.loadMyServices()
    },
    computed: {
        ...mapState(['csrfToken', 'provider_shopping']),
    },
    methods: {
        ...mapMutations(['toggleProviderShopping']),
        toggleshowPending() {
            this.showPending = !this.showPending
        },
        toggleShowModal() {
            this.showModifyServiceModal = !this.showModifyServiceModal
            // console.log('clicked')
        },
        setServiceId(id) {
            this.serviceId = id
            console.log(this.serviceId)
        },
        loadMyServices() {
            let provider_id = '40338897-3dfe-4cb6-8931-fdb6057a2187'
            let url = 'http://localhost:5000/api/v1/serviceProviders/' + provider_id + '/services'
            fetch(url, {
                method: "GET",
                headers: {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.csrfToken
                },
                credentials: "include",
                // body: JSON.stringify(data),
                })
                .then((res) => res.json())
                .then((data) => {
                    console.log('my services: ', data);
                    // set services to the fetched data
                })
                .catch((err) => {
                    console.log('error: ', err);
                    // res = err
                });
        }
    }
}
</script>
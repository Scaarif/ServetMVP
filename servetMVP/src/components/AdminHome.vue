<template>
    <div class="w-full flex flex-col space-y-4 p-4 pb-16">
       <!-- Pending services (unverified/un-vetted) -->
       <div class="w-full flex flex-col space-y-2 border p-4 rounded">
            <div class="flex space-x-2 items-center relative mb-4">
                <span class="text-lg font-medium">Pending Services</span>
                <span class="absolute top-1 left-36" @click="toggleShowPending">
                    <svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18.5 9L12.5 15L6.5 9" stroke="black" stroke-width="2"/>
                    </svg>
                </span>
                <span class="absolute right-0 px-8 py-2 rounded-sm text-sm font-medium bg-NormalBage
                    transition-all hover:bg-ActiveBage cursor-pointer capitalize" @click="setActiveUser('customer')"
                >See all Services</span>
            </div>
            <!-- the pending services -->
            <div v-show="showPending" class="flex flex-col space-y-2 pb-2">
                    <table class="md:max-w-lg w-full">
                        <thead class="bg-gray-100">
                            <tr>
                                <th class="border text-start p-2">Service</th>
                                <th class="border text-start p-2">Vetted</th>
                                <th class="border text-start p-2">Verified</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- this bit needs work (how to mark as verified/ vetted??? default to No and provide a Yes option) -->
                            <tr v-for="i in (1, 4)" :key="i">
                                <td class="border pl-4 py-1">Some Service</td>
                                <td class="border pl-4 py-1">{{ (i + 1) % 2 === 0 ? 'No' : 'Yes' }}</td>
                                <td class="border pl-4 py-1">No</td>
                            </tr>
                        </tbody>
                    </table>
            </div>
        </div>
       <!-- Analytics (table) -->
       <div class="flex flex-col space-y-2 p-4 pb-6 border rounded">
            <span class="text-lg font-medium mb-4">Analytics</span>
            <table class="md:max-w-lg w-full">
                <thead class="bg-gray-100">
                    <tr>
                        <th class="border text-start p-2">Service Category</th>
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
                <Analytics />
            </div>
       </div>
    </div>
</template>
<script>

import { mapMutations } from 'vuex'
import Analytics from './Analytics.vue'

export default {
    components: {
        Analytics,
    },
    data() {
        return {
            showPending: true,
            services: ['some service', 'test service'],
        }
    },
    methods: {
        ...mapMutations(['setActiveUser',]),
        toggleShowPending() {
            this.showPending = !this.showPending
        },
    }
}
</script>
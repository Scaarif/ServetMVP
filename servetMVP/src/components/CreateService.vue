<template>
    <form v-if="!isAdmin" class="absolute top-0 sticky top-24 z-10 bg-gray-50 w-full px-4 flex flex-col space-y-1 min-h-full">
        <h1 class="text-center font-medium text-slate-800 bg-ProfileBlue
            p-4 mb-2 rounded-sm"
            >Create a new Service</h1>
        <div class="flex flex-col space-y-2 py-4 pl-4 border rounded-sm">
           <div class="flex space-x-4 items-center" v-for="item, idx in serviceDetails" :key="idx">
                <span class="w-1/3 text-md text-slate-800 capitalize">{{ item }}</span>
                <input class="text-sm text-slate-800 max-w-md bg-SidebarBlue
                        w-full p-2 focus:text-ActiveBlue focus:outline-ActiveBlue">
           </div>
           <!-- back button -->
           <div class="flex justify-end py-4">
                <span @click="toggleCreateService"
                    class="text-slate-800 text-md font-medium py-1.5 border border-ProfileBlue px-8 mr-8
                    rounded-sm transition-all hover:border-ActiveBlue hover:text-slate-600 cursor-pointer">Save</span>
            </div>
        </div>
    </form>
    <!-- I essentially need to change up a class (the sticky positioning) -->
    <form v-else class="absolute top-0 z-5 bg-gray-50 w-full px-4 flex flex-col space-y-1 min-h-full">
        <h1 class="text-center font-medium text-slate-800 bg-ProfileBlue
            p-4 mb-2 rounded-sm"
            >Create a new Service</h1>
        <div class="flex flex-col space-y-2 py-4 pl-4 border rounded-sm">
           <div class="flex space-x-4 items-center" v-for="item, idx in serviceDetails" :key="idx">
                <span class="w-1/3 text-md text-slate-800 capitalize">{{ item }}</span>
                <input class="text-sm text-slate-800 max-w-md bg-SidebarBlue
                        w-full p-2 focus:text-ActiveBlue focus:outline-ActiveBlue">
           </div>
           <!-- back button -->
           <div class="flex justify-end py-4">
                <span @click="toggleCreateService"
                    class="text-slate-800 text-md font-medium py-1.5 border border-ProfileBlue px-8 mr-8
                    rounded-sm transition-all hover:border-ActiveBlue hover:text-slate-600 cursor-pointer">Save</span>
            </div>
        </div>
    </form>
</template>
<script>
 import { mapMutations, mapState } from 'vuex';
 export default {
     data() {
         return {
            serviceDetails: ['service name', 'service description', 'locations available', 'booking status'],
         }
     },
     computed: {
        ...mapState(['isAdmin'])
     },
     methods: {
         ...mapMutations(['toggleCreateService'])
     }
 }
 </script>
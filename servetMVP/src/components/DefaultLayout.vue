<template>
    <div class="bg-gray-50 min-h-screen h-full relative text-slate-800">
        <Navbar v-if="isAuthorized"/>
        <!-- <main class="mx-4 top-16 relative flex flex-col items-center w-full"> -->
        <main class="mx-4 top-16 relative flex flex-col w-full">
            <router-view />
        </main>
    </div>
</template>

<script>
import Navbar from './Navbar.vue';

import { mapState } from 'vuex';

export default {
    components: {
        Navbar
    },
    data() {
        return {
          
        }
    },
    computed: {
        ...mapState(['isAuthorized'])
    },
    methods: {
        
    }
}
</script>
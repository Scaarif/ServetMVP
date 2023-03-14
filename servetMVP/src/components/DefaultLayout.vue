<template>
    <div class="bg-gray-50 min-h-screen relative">
        <Navbar v-if="!isLanding"/>
        <main class="mx-4 top-16 relative flex flex-col items-center">
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
            showNotifications: true,
        }
    },
    computed: {
        ...mapState(['isLanding'])
    },
    methods: {
        toggleShowNotifications() {
            this.showNotifications = !this.showNotifications
        }
    }
}
</script>
<template>
    <div class="w-full flex flex-col items-center">
        <ServicesTemplate v-if="activeUser === 'customer' || !activeUser"/>
        <ProvidersHome v-if="activeUser === 'provider'"/>
        <AdminHome v-if="activeUser === 'admin'"/>
    </div>
</template>
<script>
import ServicesTemplate from '../components/ServicesTemplate.vue'
import ProvidersHome from '../components/ProvidersHome.vue'
import AdminHome from '../components/AdminHome.vue'

import { mapState } from 'vuex'

export default {
    components: {
        ServicesTemplate,
        ProvidersHome,
        AdminHome,
    },
    data() {
        return {
            
        }
    },
    computed: {
        ...mapState(['token', 'activeUser']),
    },
    created() {
        this.checkIfLoggedIn()
    },
    methods: {
        checkIfLoggedIn() {
            if (!this.token)
                this.$router.push({name: 'landing'}) //redirect back landing page if user not logged
       }
    }
}
</script>
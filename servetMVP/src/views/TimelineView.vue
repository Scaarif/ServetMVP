<template>
    <div class="">
        <ServicesTemplate v-if="activeUser === 'customer' || (!activeUser && !loggedInUser) || loggedInUser.user_type === 'CUS'"/>
        <ProvidersHome v-if="activeUser === 'provider' || loggedInUser.user_type === 'SP'"/>
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
        ...mapState(['activeUser', 'isAuthorized', 'loggedInUser', 'provider_shopping']),
    },
    created() {
        this.checkIfLoggedIn()
    },
    methods: {
        checkIfLoggedIn() {
            if (!this.isAuthorized)
                this.$router.push({name: 'landing'}) //redirect back landing page if user not logged
       }
    }
}
</script>
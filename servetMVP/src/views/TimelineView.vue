<template>
    <div class="flex items-center">
        <h1>Hello & welcome to Servet!</h1>
    </div>
</template>
<script>
// import AdminsDashBoard from '../components/AdminsDashBoard.vue';

import { mapState } from 'vuex'

export default {
    components: {
    
    },
    data() {
        return {
            
        }
    },
    computed: {
        ...mapState(['token']),
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
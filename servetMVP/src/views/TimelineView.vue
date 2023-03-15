<template>
    <div class="w-full flex flex-col items-center">
        <ServicesTemplate />
    </div>
</template>
<script>
import ServicesTemplate from '../components/ServicesTemplate.vue'

import { mapState } from 'vuex'

export default {
    components: {
        ServicesTemplate,
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
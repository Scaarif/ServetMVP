<template>
    <div class="">
        <ServicesTemplate v-if="servicesLoaded"/>
        <Loading v-else/>
    </div>
</template>
<script>
import ServicesTemplate from '../components/ServicesTemplate.vue';
import Loading from '../components/Loading.vue'


import { mapState, mapMutations, mapGetters } from 'vuex';

export default {
    data() {
        return {
        }
    },
    computed: {
        ...mapState(['showService']),
        ...mapGetters(['servicesLoaded']),
    },
    components: {
        ServicesTemplate,
        Loading,
    },
    methods: {
        ...mapMutations(['toggleShowService']),
    }
}
</script>
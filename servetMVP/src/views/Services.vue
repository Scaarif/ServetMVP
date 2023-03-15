<template>
    <div class="">
        <ServicesTemplate />
    </div>
</template>
<script>
import ServicesTemplate from '../components/ServicesTemplate.vue';


import { mapState, mapMutations } from 'vuex';

export default {
    data() {
        return {
        }
    },
    computed: {
        ...mapState(['showService']),
    },
    components: {
        ServicesTemplate
    },
    methods: {
        ...mapMutations(['toggleShowService']),
    }
}
</script>
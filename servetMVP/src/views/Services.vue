<template>
    <div class="w-full flex flex-col items-center">
        Services page
    </div>
</template>
<script>
// import ServiceCard from '../components/subComponents/ServiceCard.vue';

import { mapMutations } from 'vuex';

export default {
    data() {
        return {
            services: ['some service', 'some other service', 'test service'],
        }
    },
    components: {
    },
    methods: {
        ...mapMutations([''])
    }
}
</script>
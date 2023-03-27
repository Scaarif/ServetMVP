<template>
    <div class="h-16 flex items-center justify-center w-full fixed z-10">
        <router-link :to="{name: 'home'}"
            class="absolute left-4 text-slate font-semibold text-xl px-4 py-1 rounded bg-gray-50"
        >Servet</router-link>
        <div class="bg-gray-50 max-w-md w-full rounded-sm relative">
        </div>
        <!-- add a logout button -->
        <div class="absolute z-10 border py-1 px-4 rounded right-8 bg-gray-50 hover:bg-NormalBage cursor-pointer" @click="handleLogout">Logout</div>
        <!-- toggle User (for demonstration purposes) -->
        <div class="absolute top-50% right-32 flex items-center space-x-2">
            <select class="text-sm text-slate-800 font-medium border-none focus:border-none focus:outline-none
                focus:ring-0 rounded-sm bg-gray-50 capitalize"
                v-model="user"
                @change="toggleUser()"
                >
                <option v-for="user, idx in users" :key="idx"
                    class="border-none outline-none ring-0 focus:border-none focus:outline-none focus:ring-0 capitalize"
                    :value="user" >{{ user }}</option>
            </select>
        </div>
        <!-- small devices have a hamburger menu (add hamburger) -->
    </div>
</template>
<script>
import { mapState, mapMutations } from 'vuex'

export default {
    data() {
        return {
            searchValue: '',
            users: ['admin', 'customer', 'provider'],
            user:'customer',
        }
    },
    computed: {
        ...mapState(['isCustomer', 'isAdmin', 'searchName']),
    },
    methods: {
        ...mapMutations(['setActiveUser', 'handleLogout']),
        toggleUser() {
            // console.log('selected user:', this.user)
            this.setActiveUser(this.user)
        }
    }
}
</script>
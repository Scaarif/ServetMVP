<template>
    <div class="flex flex-col items-center justify-center min-h-screen h-full bg-gray-50">
        <form @submit.prevent="handleSubmit" class="flex flex-col items-center space-y-2 pt-16 pb-32 px-16 border rounded-md shadow-sm">
            <span class="pb-16 text-lg">Welcome to <b>Servet</b></span>
            <div class="w-full flex items-center space-x-4">
                <span class="min-w-sm w-full text-md capitalize">User name:<b>*</b></span>
                <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                    focus:ring-0 focus:border-slate-600 valid:bg-blue-50" type="text" required>
            </div>
            <div class="w-full flex items-center space-x-4">
                <span class="min-w-sm w-full text-md capitalize">Password:<b>*</b></span>
                <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100 focus:ring-0
                    focus:border-slate-600 valid:bg-blue-50" type="password" required>
            </div>
            <div class="self-end flex flex-col items-center">
                <button class="md:min-w-[468px] w-full rounded-sm bg-[#F3ECD1] py-2 mt-8 transition-all
                    hover:bg-[#E9D89D] text-md font-medium">Login</button>
            </div>
            <!-- call to action - sign up (instead) -->
            <div class="self-start pt-8">
                <span class="min-w-sm w-full text-md">Don't have an account yet?
                    <router-link :to="{name: 'signup'}" class="text-md border-b border-transparent p-1 font-medium transition-all
                        hover:border-slate-700 cursor-pointer">Sign Up</router-link>
                </span>
            </div>
        </form>
    </div>
</template>
<script>
import { mapMutations, mapState } from 'vuex';
export default {
    computed: {
        ...mapState(['token', 'isLanding']),
    },
    methods: {
        ...mapMutations(['toggleToken', 'toggleIsLanding']),
        handleSubmit() {
            if (this.isLanding)
                this.toggleIsLanding()
            // handle data submission (POST)
            console.log('logged in!')
            if (!this.token) {
                this.toggleToken()
                console.log('token -> ', this.token)
            }
            if (this.token)
                this.$router.push({name: 'home'}) //redirect back home page -> user logged in!
        }
    }
}
</script>
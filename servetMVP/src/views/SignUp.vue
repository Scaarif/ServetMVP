<template>
    <div class="flex flex-col items-center justify-center min-h-screen h-full bg-gray-50">
        <form @submit.prevent="handleSubmit" class="flex flex-col items-center space-y-2 pb-32 pt-16 px-16 border rounded-md shadow-sm">
            <span class="pb-16 text-lg">Welcome to <b>Servet</b></span>
            <!-- select user type -->
            <div class="self-end flex items-center space-x-2 mb-16 pl-2 rounded-sm">
               <span class="text-lg font-medium"> Sign Up as a</span>
               <select class="text-sm bg-slate-50 ring-0 border-slate-300 rounded focus:border-slate-400 focus:ring-0"
                    v-model="user"
                    @change="setUser"
               >
                    <option class="hover:bg-gray-100" value="customer">Customer</option>
                    <option class="hover:bg-gray-100" value="provider">Service Provider</option>
               </select>
            </div>
            <div v-for="value, idx in fields" :key="idx" 
                class="w-full flex items-center space-x-4">
                <span class="min-w-sm w-full text-md capitalize">{{ Object.keys(value)[0] }}:<b>*</b></span>
                <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                    focus:ring-0 focus:border-slate-600 text-center valid:bg-blue-50"
                    :type="Object.keys(value)[0].includes('password') ? 'password' : 'text'" :placeholder="Object.values(value)[0]" required>
            </div>
            <div class="w-full flex items-center space-x-4">
                <span class="min-w-sm w-full text-md capitalize">email address:<b>*</b></span>
                <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                    focus:ring-0 focus:border-slate-600 text-center invalid:border-red-700 valid:bg-blue-50"
                    type="email" placeholder="email address" required>
            </div>
            <div class="flex flex-col items-center space-y-2" v-if="signUpUser === 'provider'">
                <div v-for="value, idx in providerFields" :key="idx" 
                    class="w-full flex items-center space-x-4 relative">
                    <span class="min-w-sm w-full text-md capitalize">{{ Object.keys(value)[0] }}:<b>*</b></span>
                    <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                        focus:ring-0 focus:border-slate-600 text-center valid:bg-blue-50" type="text"
                        :placeholder="Object.values(value)[0]" required>
                </div>
            </div>
            <div class="self-end flex flex-col items-center">
                <button class="md:min-w-[468px] w-full rounded-sm bg-[#F3ECD1] py-2 mt-8 transition-all
                    hover:bg-[#E9D89D] text-md font-medium">Sign up</button>
            </div>
            <!-- call to action - sign up (instead) -->
            <div class="self-start pt-8">
                <span class="min-w-sm w-full text-md">Already have an account?
                    <router-link :to="{name: 'login'}" class="text-md border-b border-transparent p-1 font-medium transition-all
                        hover:border-slate-700 cursor-pointer">Login</router-link>
                </span>
            </div>
        </form>
    </div>
</template>
<script>
export default {
    data() {
        return {
            // field and its placeholder value
            fields: [
                {'full name': 'your full name'},
                {'phone number': 'your phone number'},
                {'password': 'set a password'},
                {'confirm password': 'confirm password'},
            ],
            providerFields: [
                {'service category': 'your service category'},
                {'service description': 'your service description'},
                {'location': 'your location'},
                {'whats app number': 'your whats app number'},
                {'social media links': 'your social media links'},
                {'profile photo': 'upload profile photo'},
            ],
            user: 'customer',
            signUpUser: '',
            showSelect: true,
        }
    },
    methods: {
        setUser() {
            this.signUpUser = this.user
            console.log('sign up as: ', this.signUpUser)
        },
        handleSubmit() {
            // handle data submission (POST)
            console.log('signed up!')
        }
    }
}
</script>
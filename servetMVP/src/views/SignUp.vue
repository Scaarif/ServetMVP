<template>
    <div class="flex flex-col items-center justify-center min-h-screen h-full bg-gray-50">
        <form @submit.prevent="handleSubmit" class="flex flex-col items-center space-y-2 pb-32 pt-16 md:px-16 md:border
            md:rounded-md md:shadow-sm">
            <span class="pb-16 text-lg">Welcome to <b>Servet</b></span>
            <!-- select user type -->
            <div class="w-full md:w-fit md:self-end flex items-center space-x-2 mb-16 md:pl-2 rounded-sm">
               <!-- <span class="text-lg font-medium"> Sign Up as a</span> -->
               <select class="text-sm bg-slate-50 ring-0 border-slate-300 rounded focus:border-slate-400 focus:ring-0 w-full"
                    v-model="user"
                    @change="setUser"
               >
                    <option class="hover:bg-gray-100" value="" default>Sign up as...</option>
                    <option class="hover:bg-gray-100" value="customer">Customer</option>
                    <option class="hover:bg-gray-100" value="provider">Service Provider</option>
               </select>
            </div>
            <div v-for="value, idx in fields" :key="idx" 
                class="w-full flex items-center flex-col md:flex-row md:space-x-4">
                <span class="md:min-w-sm w-full text-md capitalize">{{ Object.keys(value)[0] }}:<b>*</b></span>
                <input class="md:min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                    focus:ring-0 focus:border-slate-600 text-center valid:bg-blue-50"
                    :type="Object.keys(value)[0].includes('password') ? 'password' : 'text'"
                    :placeholder="Object.values(value)[0]" required :name="Object.values(value)[0]"
                    :ref="Object.values(value)[0]" :class="error && 'highlight'"  
                >
            </div>
            <div class="w-full flex flex-col items-center md:flex-row md:space-x-4">
                <span class="md:min-w-sm w-full text-md capitalize">email address:<b>*</b></span>
                <input class="md:min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                    focus:ring-0 focus:border-slate-600 text-center invalid:border-red-700 valid:bg-blue-50"
                    type="email" placeholder="email address" required v-model="email">
            </div>
            <div class="w-full flex flex-col items-center space-y-2" v-if="signUpUser === 'provider'">
                <div v-for="value, idx in providerFields" :key="idx" 
                    class="w-full flex items-center flex-col md:flex-row md:space-x-4 relative">
                    <span class="md:min-w-sm w-full text-md capitalize">{{ Object.keys(value)[0] }}:<b>*</b></span>
                    <input class="md:min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                        focus:ring-0 focus:border-slate-600 text-center valid:bg-blue-50" :type="Object.keys(value)[0] === 'profile photo' ? 'file' : 'text'"
                        :placeholder="Object.values(value)[0]" required
                        :ref="Object.values(value)[0]" :class="error && 'highlight'"
                    >
                </div>
            </div>
            <div class="w-full md:self-end md:w-fit flex flex-col items-center">
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
import { ref } from 'vue'
export default {
    data() {
        return {
            // field and its placeholder value
            fields: [
                {'full name': 'full name'},
                {'username': 'username'},
                {'phone number': 'phone'},
                {'password': 'password'},
                {'confirm password': 'confirm password'},
            ],
            providerFields: [
                // {'service category': 'category'},
                // {'service description': 'description'},
                {'location': 'location'},
                {'whats app number': 'whats app'},
                // {'social media links': 'social media'},
                {'profile photo': 'photo'},
            ],
            user: 'customer',
            signUpUser: '',
            showSelect: true,
            email: '',
            csrfToken: '',
            isAuthenticated: false,
            error: false,
        }
    },
    mounted() {
        this.getSession()
    },
    methods: {
        setUser() {
            this.signUpUser = this.user
            console.log('sign up as: ', this.signUpUser)
        },
        handleSubmit() {
            // handle data submission (POST)
            let toSet = {};
            let set = Object.values(this.fields)
            if (this.signUpUser === 'provider')
                set.push(...Object.values(this.providerFields))
            set.map(val => {
                let field = Object.values(val)[0]
                toSet[field] = this.$refs[field][0].value
                // validate values (input)
                if (field === 'full name' && !toSet[field].split(' ')[1])
                    this.error = true
                if (field === 'confirm password' && !(toSet['password'] === toSet[field]))
                    this.error = true
            })
            console.log('toSet: ', toSet)
            if (this.error)
                return
            // console.log(this.$refs['full name'][0].value, this.$refs['username'][0].value)
            // let data = {}
            let data = new FormData()
            data.append('first_name', toSet['full name'].split(' ')[0])
            data.append('username', toSet.username)
            data.append('last_name', toSet['full name'].split(' ')[1])
            data.append('email', this.email)
            data.append('password', toSet.password)
            data.append('phone', toSet.phone)
            data.append('profile_pic', toSet.photo)
            data.append('csrf_token', this.csrfToken)

            // data['first_name'] = toSet['full name'].split(' ')[0]
            // data['username'] = toSet.username
            // data['last_name'] = toSet['full name'].split(' ')[1]
            // data['email'] = this.email
            // data['password'] = toSet.password
            // data['phone'] = toSet.phone
            // data['csrf_token'] = this.csrfToken

            if (this.signUpUser === 'provider'){
                // console.log('signing up as provider')
                data.append('whatsapp', toSet['whats app'])
                data.append('location', toSet.location)
                // data.append('profile_pic', toSet.photo)
            }
            // this.signup(JSON.stringify(data))
            this.signup(data)
        },
        getSession() {
            fetch("http://localhost:5000/api/v1/getsession", {
                            credentials: "include",
                            })
                            .then((res) => res.json())
                            .then((data) => {
                            console.log(data);
                            if (data.login == true) {
                                this.isAuthenticated = true;
                            } else {
                                this.isAuthenticated = false;
                                this.csrf();
                            }
                            })
                            .catch((err) => {
                            console.log(err);
                            });
        },
        csrf() {
            fetch("http://localhost:5000/api/v1/getcsrf", {
                    credentials: "include",
                    })
                    .then((res) => {
                    this.csrfToken = res.headers.get(["X-CSRFToken"]);
                    // console.log(csrfToken);
                    })
                    .catch((err) => {
                    console.log(err);
                    });

        },
        signup(data) {
            console.log(data.entries())
            let url = 'http://localhost:5000/api/v1'
            url += this.signUpUser === 'provider' ? '/serviceProviders/signup' : '/customers/signup'
            // console.log('signup url: ', url)
            fetch(url, {
                method: "POST",
                headers: {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    // "Content-Type": "application/json",
                    // "X-CSRFToken": this.csrfToken
                },
                credentials: "include",
                // body: JSON.stringify({ username: this.userName, password: this.password }),
                body: data
                })
                .then((res) => res.json())
                .then((data) => {
                console.log(data);
                // if (data.login == true) {
                //     isAuthenticated = true;
                // }
                }
                )
                .catch((err) => {
                console.log(err);
                });
        },
        printValue(val){
            console.log(val+': ' + this.$refs[val][0].value)
        },
    }
}
</script>
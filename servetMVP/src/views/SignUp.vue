<template>
    <div class="flex flex-col items-center justify-center min-h-screen h-full bg-gray-50">
        <form @submit.prevent="handleSubmit" class="flex flex-col items-center space-y-2 pb-32 pt-16 px-16 border
            rounded-md shadow-sm">
            <span class="pb-16 text-lg">Welcome to <b>Servet</b></span>
            <!-- select user type -->
            <div class="md:self-end flex items-center space-x-2 mb-16 pl-2 rounded-sm">
               <!-- <span class="text-lg font-medium"> Sign Up as a</span> -->
               <select class="text-sm bg-slate-50 ring-0 border-slate-300 rounded focus:border-slate-400 focus:ring-0"
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
                    :placeholder="Object.values(value)[0]" required>
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
                        focus:ring-0 focus:border-slate-600 text-center valid:bg-blue-50" type="text"
                        :placeholder="Object.values(value)[0]" required>
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
export default {
    data() {
        return {
            // field and its placeholder value
            fields: [
                {'full name': 'your full name'},
                {'username': 'preferred username'},
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
            fullname: 'farahh Alachi',
            email: 'farah@alachi',
            password: 'test',
            phone: '07xx xxxx11',
            whatsapp: '07xx xxxxx11',
            location: 6, // kasarani
            csrfToken: '',
            isAuthenticated: false,
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
            let data = {}
            data['first_name'] = this.fullname.split(' ')[0]
            data['username'] = this.fullname.split(' ')[1]
            data['last_name'] = this.fullname.split(' ')[1]
            data['email'] = this.email
            data['password'] = this.password
            data['phone'] = this.phone
            data['csrf_token'] = this.csrfToken

            if (this.signUpUser === 'provider'){
                // console.log('signing up as provider')
                data['whatsapp'] = this.whatsapp
                data['location'] = this.location
            }
            this.signup(JSON.stringify(data))
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
            console.log(data)
            let url = 'http://localhost:5000/api/v1'
            url += this.signUpUser === 'provider' ? '/serviceProviders/signup' : '/customers/signup'
            // console.log('signup url: ', url)
            fetch(url, {
                method: "POST",
                headers: {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.csrfToken
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
    }
}
</script>
<template>
    <div class="flex flex-col items-center justify-center min-h-screen h-full bg-gray-50">
        <form @submit.prevent="handleSubmit" name="form" class="flex flex-col items-center space-y-2 pt-16 pb-32 px-16 border rounded-md shadow-sm">
            <span class="pb-16 text-lg">Welcome to <b>Servet</b></span>
            <div class="w-full flex items-center space-x-4">
                <span class="min-w-sm w-full text-md capitalize">User name:<b>*</b></span>
                <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                    focus:ring-0 focus:border-slate-600 valid:bg-blue-50" type="text" required v-model="userName">
            </div>
            <div class="w-full flex items-center space-x-4">
                <span class="min-w-sm w-full text-md capitalize">Password:<b>*</b></span>
                <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100 focus:ring-0
                    focus:border-slate-600 valid:bg-blue-50" type="password" required v-model="password">
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
    data() {
        return {
            userName: '',
            password: '',
            // csrf: '',
            csrfToken: '',
            isAuthenticated: false,
        }
    },
    computed: {
        ...mapState(['token', 'isLanding']),
    },
    mounted() {
        this.getSession()
    },
    methods: {
        ...mapMutations(['toggleToken', 'toggleIsLanding', 'setCsrfToken']),
        handleSubmit() {
            // const formData = new FormData(form)
            // // add key-value pairs (to post)
            // // formData.append('username', this.userName)
            // // formData.append('password', this.password)
            // // const values = [...formData.entries()]
            // // console.log('formData: ', values)
            // // test login endpoint
            // this.login(formData)
            // if (this.isLanding)
            //     this.toggleIsLanding()
            // // handle data submission (POST)
            // console.log('logged in!')
            // if (!this.token) {
            //     this.toggleToken()
            //     console.log('token -> ', this.token)
            //     localStorage.setItem('token', true)
            // }
            // if (this.token)
            //     this.$router.push({name: 'home'}) //redirect back home page -> user logged in!

            // tests
            this.login()

        },
        getSession() {
            fetch("http://web-01.whosadevnow.tech/api/getsession", {
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
        // async getCSRF() {
            // let res = await fetch('http://web-01.whosadevnow.tech/api/v1/getcsrf')
            // // const data = await res.json()
            // console.log('csrf: ', res.headers.get('x-csrftoken'))
            // this.csrf = res.headers.get('x-csrftoken')
            // // let ses = await fetch('http://web-01.whosadevnow.tech/api/v1/getsession')
            // // let sesdata = await ses.json()
            // // console.log('session: ', sesdata)

            fetch("http://web-01.whosadevnow.tech/api/getcsrf", {
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
        // async login(data) {
        //     await this.getCSRF()
        //     // console.log('this: ', this.csrf)
        //     data.append('csrf_token', this.csrf)
        //     let res = await fetch('http://web-01.whosadevnow.tech/api/v1/customers/login', {
        //         method: 'POST',
        //         headers: {'X-CSRFToken': this.csrf},
        //         body: data,
        //     })
        //     console.log(...data)
        //     const result = await res.json()
        //     console.log('login res:', result)
        // }
        login() {
            fetch("http://web-01.whosadevnow.tech/api/login", {
                method: "POST",
                headers: {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.csrfToken
                },
                credentials: "include",
                body: JSON.stringify({ username: this.userName, password: this.password }),
                })
                .then((res) => res.json())
                .then((data) => {
                console.log(data, 'login -> ', data.login);
                if (data.login == true) {
                    isAuthenticated = true;
                }
                })
                .catch((err) => {
                console.log(err);
                });
        },
        whoami() {
            fetch("http://web-01.whosadevnow.tech/api/data", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                credentials: "include",
                })
                .then((res) => res.json())
                .then((data) => {
                console.log(data);
                alert(`Welcome, ${data.username}!`);
                })
                .catch((err) => {
                console.log(err);
                });
        },

        logout() {
            fetch("http://web-01.whosadevnow.tech/api/logout", {
                credentials: "include",
                })
                .then(() => {
                isAuthenticated = false;
                })
                .catch((err) => {
                console.log(err);
                });
        },
    },
    // tests
    
    
}
</script>

<template>
    <div class="flex flex-col items-center justify-center min-h-screen h-full bg-gray-50">
        <form @submit.prevent="handleSubmit" name="form" class="flex flex-col items-center space-y-2 pt-16 pb-32 px-16 border rounded-md shadow-sm">
            <span class="pb-16 text-lg">Welcome to <b>Servet</b></span>
            <div class="w-full flex items-center space-x-4">
                <span class="min-w-sm w-full text-md capitalize">User name:<b>*</b></span>
                <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100
                    focus:ring-0 focus:border-slate-600 valid:bg-blue-50" type="text" required v-model="userName" :class="errorMsg && 'highlight'">
            </div>
            <div class="w-full flex items-center space-x-4">
                <span class="min-w-sm w-full text-md capitalize">Password:<b>*</b></span>
                <input class="min-w-[468px] w-full border border-slate-400 rounded-sm bg-gray-100 focus:ring-0
                    focus:border-slate-600 valid:bg-blue-50" type="password" required v-model="password" :class="errorMsg && 'highlight'">
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
import { mapGetters, mapMutations, mapActions, mapState } from 'vuex';
export default {
    data() {
        return {
            userName: '',
            password: '',
            // csrf: '',
            csrfToken: '',
            isAuthenticated: false,
            errorMsg: '',
        }
    },
    computed: {
        ...mapState(['isLanding', 'isAuthorized']),
        ...mapGetters(['servicesLoaded']),
    },
    mounted() {
        this.getSession()
    },
    methods: {
        ...mapMutations(['toggleIsLanding', 'setCsrfToken', 'toggleIsAuthorized', 'setLoggedInUser']),
        ...mapActions(['fetchServices']),
        handleSubmit() {
          console.log('isAuth: ', this.isAuthenticated, this.isAuthorized)
            if (!this.isAuthenticated) {
              let data = {username: this.userName}
              data['password'] = this.password
              this.login(JSON.stringify(data))
            }
            else {
                this.toggleIsLanding() // make it false so the navbar shows
                if (!this.isAuthorized)
                    this.toggleIsAuthorized()
                // redirect to home page
                this.$router.push({name: 'home'})
            }
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
                                // this.setCsrfToken(this.csrfToken)

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
                    // set global csrfToken
                    this.setCsrfToken(this.csrfToken)
                    // console.log(csrfToken);
                    })
                    .catch((err) => {
                    console.log(err);
                    });

        },
        login(data) {
          console.log(data)
            fetch("http://localhost:5000/api/v1/login", {
                method: "POST",
                headers: {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.csrfToken
                },
                credentials: "include",
                body: data,
                })
                .then((res) => res.json())
                .then((data) => {
                console.log(data, 'login -> ', data.login);
                if (data.login == true) {
                    this.isAuthenticated = true;
                    // set global csrfToken
                    this.setCsrfToken(this.csrfToken)
                    // set user_info (loggedInUser)
                    let user={'user_id': data.user_id, 'user_type': data.user_type}
                    this.setLoggedInUser(user)
                    this.toggleIsLanding()
                    // check if services have been fetched, fetch if not (e.g when a user chooses to login from lansing page)
                    if (!this.servicesLoaded) {
                        // I'm thinking use localStorage to store a user's prev search parameters (country, location, service_categories) - key: customer_id
                        let country_id = 1 // Kenya (2 = Nigeria)
                        const queryStr = '?country=' + country_id + '&service_category=2'
                        this.fetchServices(queryStr)
                    }   
                    console.log('isLoaded: ', this.servicesLoaded)
                    // redirect to home page
                    this.$router.push({name: 'home'})
                    // set authToken in localStorage
                    localStorage.setItem('authToken', true)
                } else {
                    this.errorMsg = data.message
                    console.log('errorMsg!')
                }
                })
                .catch((err) => {
                console.log('error: ', err);
                });
        },
        logout() {
            fetch("http://localhost:5000/api/logout", {
                credentials: "include",
                })
                .then(() => {
                    this.isAuthenticated = false;
                })
                .catch((err) => {
                console.log(err);
                });
        },
    },
    // tests
    
    
}
</script>
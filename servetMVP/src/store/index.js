import { createStore } from 'vuex'
import services from './services'

const store = createStore({
    modules: {
        services,
    },
    state: {
        token: false,
        isLanding: true,
        activeUser: '',
        isCustomer: true,
        isAdmin: false, // assuming that this' the only way an institution could be signed in
        showService: false,
        counties: [],
        csrfToken: '',
        isAuthorized: false,
    },
    getters: {

    },
    actions: {

    },
    mutations: {
        setActiveUser(state, value) {
            state.activeUser = value
            console.log('activeUser: ', state.activeUser)
            if (state.activeUser === 'customer' && !state.isCustomer)
            {
                state.isCustomer = !state.isCustomer
                if (state.isAdmin)
                    state.isAdmin = !state.isAdmin
            }
            else if (state.activeUser === 'provider' && state.isCustomer) {
                state.isCustomer = !state.isCustomer
                if (state.isAdmin)
                    state.isAdmin = !state.isAdmin
            }
            else if (state.activeUser === 'admin' && state.isCustomer)
            {
                state.isCustomer = !state.isCustomer
                if (!state.isAdmin)
                    state.isAdmin = !state.isAdmin
            }
        },
        toggleIsLanding(state) {
            state.isLanding = !state.isLanding
            console.log(state.isLanding)
        },
        toggleShowService(state) {
            state.showService = !state.showService
            if (state.showService)
                this.dispatch('fetchService', 2) // call the action (fetchService)
        },
        toggleToken(state) {
            state.token = !state.token
        },
        // testing axios
        setCounties(state, counties) {
            state.counties.push(...counties)
            console.log('counties: ', state.counties)
        },
        setCsrfToken(state, value) {
            state.csrfToken = value;
            state.isAuthorized =  true
        },
        async handleLogout(state) {
            let res;
            if (state.activeUser === 'provider') {
                res = await fetch('http://localhost:5000/api/v1/serviceProviders/logout')
                let data = await res.json()
                console.log('provider logout: ', data)
            }
            else {
                res = await fetch('http://localhost:5000/api/v1/customers/logout', {
                    headers: {
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        "Content-Type": "application/json",
                        "X-CSRFToken": state.csrfToken
                    },
                    credentials: "include",
                })
                let data = await res.json()
                console.log('customer logout: ', data)
            }
        }
    }
})

export default store;
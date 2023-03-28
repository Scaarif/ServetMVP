import { createStore } from 'vuex'
import services from './services'

const store = createStore({
    modules: {
        services,
    },
    state: {
        isLanding: true,
        activeUser: '',
        isCustomer: true,
        isAdmin: false, // assuming that this' the only way an institution could be signed in
        showService: false,
        counties: [],
        csrfToken: '',
        isAuthorized: false,
        location: 'CBD, Nairobi', // default
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
        toggleShowService(state, service_id, csrf='', provider_id) {
            // pass in the service's id to use to fetch the {id}'s details
            state.showService = !state.showService
            if (state.showService)
                this.dispatch('fetchService', service_id, csrf='', provider_id) // call the action (fetchService)
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
        toggleIsAuthorized(state) {
            state.isAuthorized = true
        },
        async handleLogout(state) {
            let res;
            let url = state.activeUser === 'provider' ? 'http://localhost:5000/api/v1/serviceProviders/logout' : 'http://localhost:5000/api/v1/customers/logout'
            res = await fetch(url, {
                    headers: {
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        "Content-Type": "application/json",
                        "X-CSRFToken": state.csrfToken
                    },
                    credentials: "include",
                })
                let data = await res.json()
                let message = state.activeUser === 'provider' ? 'provider logout' : 'customer logout'
                console.log(message, data)
            // set isAuthorized to false
            state.isAuthorized = false
            // remove auth from localStorage
            localStorage.removeItem('authToken')
        },
        setSelectedLocation(state, value) {
            state.location = value
            console.log(state.location)
        }
    }
})

export default store;
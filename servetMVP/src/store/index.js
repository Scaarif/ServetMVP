import { createStore } from 'vuex'
import services from './services'
import httpClient from '../httpClient'
import config from '../config'

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
        currentService_id: '',
        counties: [],
        csrfToken: '',
        isAuthorized: false,
        loggedInUser: null,
        location: ['Nairobi', 'CBD'], // default
        locations: {'locations': []},
        states: {'states': []},
        countries: {'nigeria': 2, 'kenya': 1},
        categories: null,

        provider_shopping: false,
    },
    getters: {

    },
    actions: {
        async getCategories({commit}) {
            const res = await httpClient.loggedOutGet(config.DEFAULT + '/serviceCategories')
            // console.log(res.data)
            if (res.data.length && res.status === 200)
                commit('setCategories', res.data)
        },
        async fetchLocations({commit}, payload) {
            // default = kenya(1), nairobi(5)
            console.log('state_id: ', payload[1])
            let country_id = payload[0]
            let state_id = payload[1]
            let url = config.DEFAULT + '/countries/' + country_id + '/states/' + state_id + '/locations'
            const res = await httpClient.loggedOutGet(url)
            // console.log('locations: ', res)
            // commit 'setLocations' if successfully
            if (res.status === 200)
                commit('setLocations', res.data)
        },
        async fetchStates({commit}, country_id=1) {
            // default = kenya
            let url = config.DEFAULT + '/countries/' + country_id + '/states'
            const res = await httpClient.loggedOutGet(url)
            console.log('states: ', res.data)
            // commit 'setStates' if successfully
            if (res.status === 200)
                commit('setStates', res.data)
        }
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
            state.currentService_id = service_id
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
        setLoggedInUser(state, payload) {
            console.log(payload) // should be an object: user_id and type(customer or provider for now)
            state.loggedInUser = payload
        },
        async handleLogout(state) {
            let res;
            let url = state.activeUser === 'provider' ? 'http://web-01.whosadevnow.tech/api/v1/serviceProviders/logout' : 'http://web-01.whosadevnow.tech/api/v1/customers/logout'
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
        },
        setCategories(state, payload) {
            state.categories = payload // should be a list (array) of objects (id & name)
            console.log('state.categories: ', state.categories, state.categories[0].id)
        },
        toggleProviderShopping(state) {
            state.provider_shopping = !state.provider_shopping
            console.log('provider_shopping: ', state.provider_shopping)
        },
        setLocations(state, payload) {
            state.locations = payload
            console.log('locations: ', state.locations)
        },
        setStates(state, payload) {
            state.states = payload
            console.log('states: ', state.states)
        }
    }
})

export default store;
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
        counties: []
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
        }
    }
})

export default store;
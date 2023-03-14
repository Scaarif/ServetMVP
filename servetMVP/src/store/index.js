import { createStore } from 'vuex'

const store = createStore({
    state: {
        token: false,
        // token: true,
        activeUser: '',
        isCustomer: true,
        isAdmin: false, // assuming that this' the only way an institution could be signed in
        showDrafts: false,
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
            else if (state.activeUser === 'doctor' && state.isCustomer) {
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
        toggleShowDrafts(state) {
            state.showDrafts = !state.showDrafts
        },
    }
})

export default store;
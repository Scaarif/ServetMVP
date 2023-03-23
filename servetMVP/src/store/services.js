import httpClient from "../httpClient";
import config from "../config";


const state = {
    services: [],
    loaded: false,
}
const getters = {
    getServices(state) {
        return state.services // is an empty list === null? NOPE!!!
    },
    servicesLoaded(state) {
        console.log('loaded: ', state.loaded)
        return state.loaded
    },
}
const actions = {
    // get services based on location and category
    async fetchServices({commit}, payload) {
        const res = await httpClient.loggedOutGet(config.SERVICES + payload)
        console.log(res)
        // commit setServices if res is successful
        if (res.data.length && res.status === 200)
            commit('setServices', res.data)
        commit('setLoaded', true)
    }
}
const mutations = {
    // set services value (based on location and category) -> we need an API that doesn't require category
    setServices(state, payload) {
        // extend the services array with response
        state.services.push(...payload)
        console.log('state.services: ',state.services)
    },
    setLoaded(state, loaded) {
        state.loaded = loaded
    }

}

export default {
    state, getters, actions, mutations
}
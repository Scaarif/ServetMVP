import httpClient from "../httpClient";
import config from "../config";


const state = {
    services: [], //an array of objects (dicts)
    loaded: false,
    service: null, // an individual service
}
const getters = {
    getServices(state) {
        return state.services // is an empty list === null? NOPE!!!
    },
    getService(state) {
        // console.log(state.service)
        return state.service
    },
    servicesLoaded(state) {
        console.log('loaded: ', state.loaded)
        return state.loaded
    },
}
const actions = {
    // get services based on location and category: returns [description, provider(first & last) name, image_uri, rating(num), service_id(sps_id)])
    async fetchServices({commit}, payload) {
        const res = await httpClient.loggedOutGet(config.SERVICES + payload)
        console.log(res.data)
        // commit setServices if res is successful
        if (res.data.length && res.status === 200)
            commit('setServices', res.data)
        commit('setLoaded', true)
    },
    // get details about a particular service (reviews, rating, etc)
    async fetchService({commit}, service_id) {
        let url = config.SERVICES + '/' + service_id
        // console.log(url)
        const res = await httpClient.loggedOutGet(url)
        console.log('service: ',res)
        // commit setService if res
        if (res.status === 200)
            commit('setService', res.data)
    }
}
const mutations = {
    // set services value (based on location and category) -> we need an API that doesn't require category
    setServices(state, payload) {
        // extend the services array with response
        state.services.push(...payload)
        console.log('state.services: ', state.services, 'keys: ', Object.keys(state.services))
    },
    setService(state, payload) {
        // set service to response value (from API call)
        state.service = payload
        // console.log('state.service: ',state.service)
    },
    setLoaded(state, loaded) {
        state.loaded = loaded
    }

}

export default {
    state, getters, actions, mutations
}
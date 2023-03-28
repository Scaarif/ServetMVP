import httpClient from "../httpClient";
import config from "../config";
import axios from 'axios'

const state = {
    csrfToken: '',
    isAuthorized: false,
}
const getters = {
    getCsrf(state) {
        return state.csrfToken
    },
}
const actions = {
    async getSession() {
        let res = await axios.get(config.DEFAULT)
    }

}
const mutations = {
    setCsrf(state, token) {
        state.csrfToken = token
    }
}

export default {
    state, getters, actions, mutations
}

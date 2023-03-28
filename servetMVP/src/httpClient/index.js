import axios from 'axios'
import store from '../store/index'

// define general CRUD operations
async function loggedOutGet(url) {
    let response;
    try {
        response = await axios.get(url)
    } catch (error) {
        console.log(error)
        response = error
    }
    return response
}
async function postWithToken(url, payload, csrfToken) {
    let res;
    try {
        res = await axios.post(url, payload, {
                headers: {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                },
                // credentials: "include",
                withCredentials:true
                })
    } catch (error) {
        console.log(error)
        res = error
    }
    return res
}
// make available outside module
export default {
    loggedOutGet,
    postWithToken,
}
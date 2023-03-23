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
// make available outside module
export default {
    loggedOutGet,
}
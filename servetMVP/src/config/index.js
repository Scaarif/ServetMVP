const ENDPOINT = 'http://localhost:5000/api/v1'

// export the endpoints (eg SERVICES, LOGIN, etc)
export default {
    DEFAULT: ENDPOINT,
    SERVICES: ENDPOINT.concat('/services'),
    CUSTOMERS: ENDPOINT.concat('/customers/'),
    PROVIDERS: ENDPOINT.concat('/serviceProviders/'),
}
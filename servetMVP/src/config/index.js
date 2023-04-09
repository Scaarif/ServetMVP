const ENDPOINT = 'http://web-01.whosadevnow.tech/api/v1'

// export the endpoints (eg SERVICES, LOGIN, etc)
export default {
    DEFAULT: ENDPOINT,
    SERVICES: ENDPOINT.concat('/services'),
    CUSTOMERS: ENDPOINT.concat('/customers/'),
    PROVIDERS: ENDPOINT.concat('/serviceProviders/'),
}
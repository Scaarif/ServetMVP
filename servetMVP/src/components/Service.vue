<template>
    <div class="flex flex-col items-center shadow-lg w-full px-8 py-8 pb-32">
        <!-- Service Modal Header -->
        <span class="text-[24px] text-slate-900 font-medium text-center mb-2">Some Service</span>
        <span class="border border-slate-700 w-full"></span>
        <!-- Service Details Body -->
        <div class="flex justify-between items-center w-full px-4 py-2">
            <div class="w-1/3 flex flex-col space-y-2">
                <span class="text-lg font-medium mb-4">Service Details</span>
                <div class="flex space-x-4 items-center" v-for="value, idx in details" :key="idx">
                    <span class="w-1/3 text-md capitalize">{{ Object.keys(value)[0] }}:</span>
                    <span class="text-md capitalize">{{ Object.values(value)[0] }}</span>
                </div>
                <div class="flex space-x-4 items-center">
                    <span class="w-1/3 text-md">Rating:</span>
                    <span class="flex">
                        <svg v-for="idx in rating" :key="idx" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M7.73037 5.41502C8.21193 4.2145 8.45271 3.61425 8.84389 3.53105C8.94675 3.50918 9.05306 3.50918 9.15592 3.53105C9.5471 3.61425 9.78788 4.2145 10.2694 5.41502C10.5433 6.09773 10.6802 6.43909 10.9364 6.67126C11.0083 6.73638 11.0863 6.79438 11.1694 6.84444C11.4655 7.02293 11.8352 7.05603 12.5745 7.12225C13.8261 7.23433 14.4518 7.29038 14.6429 7.64719C14.6825 7.72108 14.7094 7.80109 14.7226 7.88389C14.7859 8.28366 14.3259 8.70221 13.4058 9.5393L13.1503 9.77175C12.7201 10.1631 12.505 10.3588 12.3806 10.603C12.306 10.7495 12.256 10.9072 12.2325 11.07C12.1934 11.3412 12.2564 11.6251 12.3824 12.1928L12.4274 12.3957C12.6533 13.4138 12.7662 13.9229 12.6252 14.1731C12.4986 14.3979 12.2653 14.5418 12.0076 14.5541C11.7207 14.5678 11.3165 14.2384 10.508 13.5796C9.97533 13.1456 9.70901 12.9285 9.41335 12.8438C9.14316 12.7663 8.85664 12.7663 8.58646 12.8438C8.2908 12.9285 8.02447 13.1456 7.49182 13.5796C6.68333 14.2384 6.27909 14.5678 5.9922 14.5541C5.7345 14.5418 5.50122 14.3979 5.37457 14.1731C5.23357 13.9229 5.34652 13.4138 5.57242 12.3957L5.61743 12.1928C5.74339 11.6251 5.80637 11.3412 5.76729 11.07C5.74384 10.9072 5.69381 10.7495 5.61918 10.603C5.49478 10.3588 5.2797 10.1631 4.84954 9.77175L4.59403 9.5393C3.67394 8.70221 3.2139 8.28366 3.27725 7.88389C3.29037 7.80109 3.31728 7.72108 3.35686 7.64719C3.54796 7.29038 4.17374 7.23433 5.42532 7.12225C6.16465 7.05603 6.53432 7.02293 6.83045 6.84444C6.91351 6.79438 6.99152 6.73638 7.06339 6.67126C7.3196 6.43909 7.45652 6.09773 7.73037 5.41502Z" fill="#222222" stroke="#222222" stroke-width="2"/>
                            </svg>
                            <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M7.60777 4.97077C8.19773 3.50002 8.4927 2.76465 8.99995 2.76465C9.50719 2.76465 9.80217 3.50002 10.3921 4.97077L10.4196 5.03926C10.7529 5.87016 10.9195 6.28561 11.2592 6.53813C11.5988 6.79064 12.0447 6.83057 12.9363 6.91043L13.0975 6.92487C14.5569 7.05556 15.2866 7.12091 15.4427 7.58515C15.5989 8.04939 15.057 8.5424 13.9732 9.52841L13.6115 9.85749C13.0628 10.3566 12.7885 10.6062 12.6607 10.9333C12.6368 10.9943 12.617 11.0568 12.6013 11.1204C12.5173 11.4614 12.5976 11.8235 12.7583 12.5476L12.8083 12.773C13.1035 14.1037 13.2511 14.7691 12.9934 15.0561C12.8971 15.1633 12.7719 15.2406 12.6328 15.2785C12.2607 15.38 11.7323 14.9495 10.6756 14.0884C9.98172 13.523 9.63478 13.2403 9.23646 13.1767C9.07978 13.1517 8.92012 13.1517 8.76344 13.1767C8.36511 13.2403 8.01817 13.523 7.32429 14.0884C6.26758 14.9495 5.73922 15.38 5.36707 15.2785C5.22801 15.2406 5.10283 15.1633 5.00651 15.0561C4.74875 14.7691 4.89638 14.1037 5.19163 12.773L5.24164 12.5476C5.4023 11.8235 5.48262 11.4614 5.39858 11.1204C5.38291 11.0568 5.36308 10.9943 5.33923 10.9333C5.21137 10.6062 4.93706 10.3566 4.38843 9.85749L4.02672 9.52841C2.94293 8.5424 2.40104 8.04939 2.55718 7.58515C2.71331 7.12091 3.44299 7.05556 4.90235 6.92487L5.06355 6.91043C5.95524 6.83057 6.40109 6.79064 6.74072 6.53813C7.08036 6.28561 7.24701 5.87016 7.5803 5.03926L7.60777 4.97077Z" fill="#7E869E" fill-opacity="0.25" stroke="#222222" stroke-width="1.4"/>
                            </svg>
                    </span>
                </div>
            </div>
            <div class="flex flex-col space-y-2 items-center">
                <span class="text-lg font-medium mb-4">Service Provider Details</span>
                <img src="../assets/scaarif_a_young_kenyan_tomboy_full-body_portrait_light_skinned__0a68fc1a-c258-4865-a6fb-33c81878f822.png" alt=""
                    class="w-16 h-16 rounded-full"
                >
                <span class="text-md capitalize py-2">jane doe</span>
                <router-link v-if="!token" :to="{name: 'login'}" class="text-md capitalize py-2 px-8 bg-[#F3ECD1] transition-all hover:bg-[#E9D89D] cursor-pointer"
                >contact service provider</router-link>
                <span v-else class="text-md capitalize py-2 px-8 bg-[#F3ECD1] transition-all hover:bg-[#E9D89D] cursor-pointer">+254 700 000000</span>
            </div>
        </div>
        <!-- Service Description -->
        <div class="self-start flex flex-col w-full mb-4">
            <span class="text-lg font-medium mb-2">Service Description</span>
            <span class="text-md px-4">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim ligula dolor, eget mattis dolor ultricies elementum.
            </span>
        </div>
        <!-- Call to action (if logged in): Review Service -->
        <form v-if="token" @submit.prevent="handleRateService" class="w-full flex flex-col items-center space-y-2 border-y border-slate-600 my-4 py-4">
            <div class="self-start flex space-x-4 items-center ml-4">
                <span class="text-md">Rating:</span>
                <span class="flex">
                    <svg v-for="idx in rating" :key="idx" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M7.60777 4.97077C8.19773 3.50002 8.4927 2.76465 8.99995 2.76465C9.50719 2.76465 9.80217 3.50002 10.3921 4.97077L10.4196 5.03926C10.7529 5.87016 10.9195 6.28561 11.2592 6.53813C11.5988 6.79064 12.0447 6.83057 12.9363 6.91043L13.0975 6.92487C14.5569 7.05556 15.2866 7.12091 15.4427 7.58515C15.5989 8.04939 15.057 8.5424 13.9732 9.52841L13.6115 9.85749C13.0628 10.3566 12.7885 10.6062 12.6607 10.9333C12.6368 10.9943 12.617 11.0568 12.6013 11.1204C12.5173 11.4614 12.5976 11.8235 12.7583 12.5476L12.8083 12.773C13.1035 14.1037 13.2511 14.7691 12.9934 15.0561C12.8971 15.1633 12.7719 15.2406 12.6328 15.2785C12.2607 15.38 11.7323 14.9495 10.6756 14.0884C9.98172 13.523 9.63478 13.2403 9.23646 13.1767C9.07978 13.1517 8.92012 13.1517 8.76344 13.1767C8.36511 13.2403 8.01817 13.523 7.32429 14.0884C6.26758 14.9495 5.73922 15.38 5.36707 15.2785C5.22801 15.2406 5.10283 15.1633 5.00651 15.0561C4.74875 14.7691 4.89638 14.1037 5.19163 12.773L5.24164 12.5476C5.4023 11.8235 5.48262 11.4614 5.39858 11.1204C5.38291 11.0568 5.36308 10.9943 5.33923 10.9333C5.21137 10.6062 4.93706 10.3566 4.38843 9.85749L4.02672 9.52841C2.94293 8.5424 2.40104 8.04939 2.55718 7.58515C2.71331 7.12091 3.44299 7.05556 4.90235 6.92487L5.06355 6.91043C5.95524 6.83057 6.40109 6.79064 6.74072 6.53813C7.08036 6.28561 7.24701 5.87016 7.5803 5.03926L7.60777 4.97077Z" fill="#7E869E" fill-opacity="0.25" stroke="#222222" stroke-width="1.4"/>
                        </svg>
                    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M7.60777 4.97077C8.19773 3.50002 8.4927 2.76465 8.99995 2.76465C9.50719 2.76465 9.80217 3.50002 10.3921 4.97077L10.4196 5.03926C10.7529 5.87016 10.9195 6.28561 11.2592 6.53813C11.5988 6.79064 12.0447 6.83057 12.9363 6.91043L13.0975 6.92487C14.5569 7.05556 15.2866 7.12091 15.4427 7.58515C15.5989 8.04939 15.057 8.5424 13.9732 9.52841L13.6115 9.85749C13.0628 10.3566 12.7885 10.6062 12.6607 10.9333C12.6368 10.9943 12.617 11.0568 12.6013 11.1204C12.5173 11.4614 12.5976 11.8235 12.7583 12.5476L12.8083 12.773C13.1035 14.1037 13.2511 14.7691 12.9934 15.0561C12.8971 15.1633 12.7719 15.2406 12.6328 15.2785C12.2607 15.38 11.7323 14.9495 10.6756 14.0884C9.98172 13.523 9.63478 13.2403 9.23646 13.1767C9.07978 13.1517 8.92012 13.1517 8.76344 13.1767C8.36511 13.2403 8.01817 13.523 7.32429 14.0884C6.26758 14.9495 5.73922 15.38 5.36707 15.2785C5.22801 15.2406 5.10283 15.1633 5.00651 15.0561C4.74875 14.7691 4.89638 14.1037 5.19163 12.773L5.24164 12.5476C5.4023 11.8235 5.48262 11.4614 5.39858 11.1204C5.38291 11.0568 5.36308 10.9943 5.33923 10.9333C5.21137 10.6062 4.93706 10.3566 4.38843 9.85749L4.02672 9.52841C2.94293 8.5424 2.40104 8.04939 2.55718 7.58515C2.71331 7.12091 3.44299 7.05556 4.90235 6.92487L5.06355 6.91043C5.95524 6.83057 6.40109 6.79064 6.74072 6.53813C7.08036 6.28561 7.24701 5.87016 7.5803 5.03926L7.60777 4.97077Z" fill="#7E869E" fill-opacity="0.25" stroke="#222222" stroke-width="1.4"/>
                    </svg>
                </span>
            </div>
            <div class="self-start flex space-x-2 items-center pb-8">
                <textarea class="self-start ml-4 rounded-sm border-slate-300 focus:ring-0 focus:border-slate-400 bg-gray-100 text-slate-700"
                    name="comment" id="" cols="60" rows="4" v-model="comment">
                </textarea>
                <button class=" self-end text-md capitalize py-2 px-12 bg-[#F3ECD1] rounded-sm
                    cursor-pointer -ml-80 transition-all hover:bg-[#E9D89D]"
                >Submit Review</button>
            </div>         
        </form>
        <!-- Customer Testimonials -->
        <div class="self-start flex flex-col w-full relative">
            <span class="text-lg font-medium mb-4">Customer Testimonials</span>
            <span class="absolute top-1 left-48" @click="toggleShowTestimonials">
                <svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M18.5 9L12.5 15L6.5 9" stroke="black" stroke-width="2"/>
                </svg>
            </span>
            <!-- testimonials -->
            <div v-show="showTestimonials || !token" class="flex flex-wrap items-center space-y-2 mb-4 px-4">
                <!-- testimonial -->
                <div class="flex flex-col space-y-4 p-4 border w-full mr-2 md:max-w-1/2 rounded-sm" v-for="name, idx in customers" :key="idx">
                    <div class="flex space-x-4 items-center">
                        <span class="text-md">Rating:</span>
                        <span class="flex">
                            <svg v-for="idx in rating" :key="idx" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M7.73037 5.41502C8.21193 4.2145 8.45271 3.61425 8.84389 3.53105C8.94675 3.50918 9.05306 3.50918 9.15592 3.53105C9.5471 3.61425 9.78788 4.2145 10.2694 5.41502C10.5433 6.09773 10.6802 6.43909 10.9364 6.67126C11.0083 6.73638 11.0863 6.79438 11.1694 6.84444C11.4655 7.02293 11.8352 7.05603 12.5745 7.12225C13.8261 7.23433 14.4518 7.29038 14.6429 7.64719C14.6825 7.72108 14.7094 7.80109 14.7226 7.88389C14.7859 8.28366 14.3259 8.70221 13.4058 9.5393L13.1503 9.77175C12.7201 10.1631 12.505 10.3588 12.3806 10.603C12.306 10.7495 12.256 10.9072 12.2325 11.07C12.1934 11.3412 12.2564 11.6251 12.3824 12.1928L12.4274 12.3957C12.6533 13.4138 12.7662 13.9229 12.6252 14.1731C12.4986 14.3979 12.2653 14.5418 12.0076 14.5541C11.7207 14.5678 11.3165 14.2384 10.508 13.5796C9.97533 13.1456 9.70901 12.9285 9.41335 12.8438C9.14316 12.7663 8.85664 12.7663 8.58646 12.8438C8.2908 12.9285 8.02447 13.1456 7.49182 13.5796C6.68333 14.2384 6.27909 14.5678 5.9922 14.5541C5.7345 14.5418 5.50122 14.3979 5.37457 14.1731C5.23357 13.9229 5.34652 13.4138 5.57242 12.3957L5.61743 12.1928C5.74339 11.6251 5.80637 11.3412 5.76729 11.07C5.74384 10.9072 5.69381 10.7495 5.61918 10.603C5.49478 10.3588 5.2797 10.1631 4.84954 9.77175L4.59403 9.5393C3.67394 8.70221 3.2139 8.28366 3.27725 7.88389C3.29037 7.80109 3.31728 7.72108 3.35686 7.64719C3.54796 7.29038 4.17374 7.23433 5.42532 7.12225C6.16465 7.05603 6.53432 7.02293 6.83045 6.84444C6.91351 6.79438 6.99152 6.73638 7.06339 6.67126C7.3196 6.43909 7.45652 6.09773 7.73037 5.41502Z" fill="#222222" stroke="#222222" stroke-width="2"/>
                                </svg>
                                <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M7.60777 4.97077C8.19773 3.50002 8.4927 2.76465 8.99995 2.76465C9.50719 2.76465 9.80217 3.50002 10.3921 4.97077L10.4196 5.03926C10.7529 5.87016 10.9195 6.28561 11.2592 6.53813C11.5988 6.79064 12.0447 6.83057 12.9363 6.91043L13.0975 6.92487C14.5569 7.05556 15.2866 7.12091 15.4427 7.58515C15.5989 8.04939 15.057 8.5424 13.9732 9.52841L13.6115 9.85749C13.0628 10.3566 12.7885 10.6062 12.6607 10.9333C12.6368 10.9943 12.617 11.0568 12.6013 11.1204C12.5173 11.4614 12.5976 11.8235 12.7583 12.5476L12.8083 12.773C13.1035 14.1037 13.2511 14.7691 12.9934 15.0561C12.8971 15.1633 12.7719 15.2406 12.6328 15.2785C12.2607 15.38 11.7323 14.9495 10.6756 14.0884C9.98172 13.523 9.63478 13.2403 9.23646 13.1767C9.07978 13.1517 8.92012 13.1517 8.76344 13.1767C8.36511 13.2403 8.01817 13.523 7.32429 14.0884C6.26758 14.9495 5.73922 15.38 5.36707 15.2785C5.22801 15.2406 5.10283 15.1633 5.00651 15.0561C4.74875 14.7691 4.89638 14.1037 5.19163 12.773L5.24164 12.5476C5.4023 11.8235 5.48262 11.4614 5.39858 11.1204C5.38291 11.0568 5.36308 10.9943 5.33923 10.9333C5.21137 10.6062 4.93706 10.3566 4.38843 9.85749L4.02672 9.52841C2.94293 8.5424 2.40104 8.04939 2.55718 7.58515C2.71331 7.12091 3.44299 7.05556 4.90235 6.92487L5.06355 6.91043C5.95524 6.83057 6.40109 6.79064 6.74072 6.53813C7.08036 6.28561 7.24701 5.87016 7.5803 5.03926L7.60777 4.97077Z" fill="#7E869E" fill-opacity="0.25" stroke="#222222" stroke-width="1.4"/>
                                </svg>
                        </span>
                    </div>
                    <span class="text-md text-slate-700">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim ligula dolor, eget mattis dolor ultricies elementum.
                    </span>
                    <span class="self-end text-md font-medium text-slate-800">{{ name }}</span>
                </div>
                 <!-- see more -->
                 <div class="w-full flex flex-col">
                    <span class="self-end text-slate-600 text-md font-medium border-b border-transparent p-2
                        mr-4 transition-all hover:border-slate-800 cursor-pointer">
                        see more ...
                    </span>
                </div>
            </div>
        </div>
        <!-- Call to action (rate the service) -->
        <div class="w-full flex justify-between items-center mt-8">
            <span v-if="!token" class="text-md capitalize py-2 px-12 bg-[#F3ECD1] transition-all hover:bg-[#E9D89D]
                cursor-pointer"
                @click="handleRateService"
            >Rate the service</span>
            <span v-else class=""></span>
            <span class="text-md capitalize py-2 px-12 border rounded-sm transition-all hover:bg-[#F3ECD1]
                cursor-pointer"
                @click="toggleShowService"
            >Go back</span>
        </div>
    </div>
</template>
<script>
import { mapState, mapMutations } from 'vuex';
export default {
    data() {
       return {
        rating: [1, 2, 3, 4],
        details: [{'location': 'CBD, Nairobi'}, {'price': '$25'}, {'available now': 'yes'}],
        showTestimonials: false,
        customers: ['Lucy Johns', 'Bradley G'],
        comment: '',
        stars: '',
       }
    },
    computed: {
        ...mapState(['showService', 'token']),
    },
    methods: {
        ...mapMutations(['toggleShowService']),
        toggleShowTestimonials() {
            // fold the testimonials if token (user logged in), they can unfold it - or simply rate the service and move on...
            this.showTestimonials = !this.showTestimonials
        },
        handleRateService() {
            if (this.token) {
                console.log('submitting your review') // submit review (POST)
                console.log(this.comment)
            }
            else
                this.$router.push({name: 'login'}) // user not logged in, redirect to login page
        }
    }
}
</script>
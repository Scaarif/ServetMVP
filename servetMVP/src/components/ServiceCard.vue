<template>
    <div class="flex flex-col items-center pb-8 space-y-4 border border-slate-300 rounded-md mb-4 mr-2 max-w-sm w-full cursor-pointer">
        <!-- Service Provider (avatar & name) -->
        <div class="w-full flex flex-col items-center space-y-2 bg-gray-200 rounded-t-md pb-2">
            <img src="../assets/scaarif_a_young_kenyan_tomboy_full-body_portrait_light_skinned__0a68fc1a-c258-4865-a6fb-33c81878f822.png" alt="avatar"
                class="mt-4 w-16 h-16 rounded-full overflow-hidden"
            >
            <span class="text-sm font-medium text-slate-800 capitalize transition-all hover:underline cursor-pointer">Jane Doe</span>
        </div>
        <!-- Service Details -->
        <div class="flex flex-col items-center space-y-4">
            <span class="text-md font-medium p-1 border-b border-slate-800 text-slate-900 capitalize">Some Service</span>
            <span class="text-sm text-slate-800 px-4">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim ligula dolor, eget mattis dolor ultricies elementum.
            </span>
            <!-- Rating, Location & Pricing -->
            <div class="w-full px-4 flex items-center justify-between">
                <!-- Rating -->
                <div class="flex flex-col space-y-1 relative">
                    <!-- stars -->
                    <div class="peer flex space-x-0 items-center">
                            <svg v-for="idx in rating" :key="idx" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M7.73037 5.41502C8.21193 4.2145 8.45271 3.61425 8.84389 3.53105C8.94675 3.50918 9.05306 3.50918 9.15592 3.53105C9.5471 3.61425 9.78788 4.2145 10.2694 5.41502C10.5433 6.09773 10.6802 6.43909 10.9364 6.67126C11.0083 6.73638 11.0863 6.79438 11.1694 6.84444C11.4655 7.02293 11.8352 7.05603 12.5745 7.12225C13.8261 7.23433 14.4518 7.29038 14.6429 7.64719C14.6825 7.72108 14.7094 7.80109 14.7226 7.88389C14.7859 8.28366 14.3259 8.70221 13.4058 9.5393L13.1503 9.77175C12.7201 10.1631 12.505 10.3588 12.3806 10.603C12.306 10.7495 12.256 10.9072 12.2325 11.07C12.1934 11.3412 12.2564 11.6251 12.3824 12.1928L12.4274 12.3957C12.6533 13.4138 12.7662 13.9229 12.6252 14.1731C12.4986 14.3979 12.2653 14.5418 12.0076 14.5541C11.7207 14.5678 11.3165 14.2384 10.508 13.5796C9.97533 13.1456 9.70901 12.9285 9.41335 12.8438C9.14316 12.7663 8.85664 12.7663 8.58646 12.8438C8.2908 12.9285 8.02447 13.1456 7.49182 13.5796C6.68333 14.2384 6.27909 14.5678 5.9922 14.5541C5.7345 14.5418 5.50122 14.3979 5.37457 14.1731C5.23357 13.9229 5.34652 13.4138 5.57242 12.3957L5.61743 12.1928C5.74339 11.6251 5.80637 11.3412 5.76729 11.07C5.74384 10.9072 5.69381 10.7495 5.61918 10.603C5.49478 10.3588 5.2797 10.1631 4.84954 9.77175L4.59403 9.5393C3.67394 8.70221 3.2139 8.28366 3.27725 7.88389C3.29037 7.80109 3.31728 7.72108 3.35686 7.64719C3.54796 7.29038 4.17374 7.23433 5.42532 7.12225C6.16465 7.05603 6.53432 7.02293 6.83045 6.84444C6.91351 6.79438 6.99152 6.73638 7.06339 6.67126C7.3196 6.43909 7.45652 6.09773 7.73037 5.41502Z" fill="#222222" stroke="#222222" stroke-width="2"/>
                            </svg>
                            <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M7.60777 4.97077C8.19773 3.50002 8.4927 2.76465 8.99995 2.76465C9.50719 2.76465 9.80217 3.50002 10.3921 4.97077L10.4196 5.03926C10.7529 5.87016 10.9195 6.28561 11.2592 6.53813C11.5988 6.79064 12.0447 6.83057 12.9363 6.91043L13.0975 6.92487C14.5569 7.05556 15.2866 7.12091 15.4427 7.58515C15.5989 8.04939 15.057 8.5424 13.9732 9.52841L13.6115 9.85749C13.0628 10.3566 12.7885 10.6062 12.6607 10.9333C12.6368 10.9943 12.617 11.0568 12.6013 11.1204C12.5173 11.4614 12.5976 11.8235 12.7583 12.5476L12.8083 12.773C13.1035 14.1037 13.2511 14.7691 12.9934 15.0561C12.8971 15.1633 12.7719 15.2406 12.6328 15.2785C12.2607 15.38 11.7323 14.9495 10.6756 14.0884C9.98172 13.523 9.63478 13.2403 9.23646 13.1767C9.07978 13.1517 8.92012 13.1517 8.76344 13.1767C8.36511 13.2403 8.01817 13.523 7.32429 14.0884C6.26758 14.9495 5.73922 15.38 5.36707 15.2785C5.22801 15.2406 5.10283 15.1633 5.00651 15.0561C4.74875 14.7691 4.89638 14.1037 5.19163 12.773L5.24164 12.5476C5.4023 11.8235 5.48262 11.4614 5.39858 11.1204C5.38291 11.0568 5.36308 10.9943 5.33923 10.9333C5.21137 10.6062 4.93706 10.3566 4.38843 9.85749L4.02672 9.52841C2.94293 8.5424 2.40104 8.04939 2.55718 7.58515C2.71331 7.12091 3.44299 7.05556 4.90235 6.92487L5.06355 6.91043C5.95524 6.83057 6.40109 6.79064 6.74072 6.53813C7.08036 6.28561 7.24701 5.87016 7.5803 5.03926L7.60777 4.97077Z" fill="#7E869E" fill-opacity="0.25" stroke="#222222" stroke-width="1.4"/>
                            </svg>
                    </div>
                    <span class="hidden absolute top-4 left-2 transition-all peer-hover:block text-sm text-slate-500">Rating</span>
                </div>
                 <!-- Location -->
                 <div class="flex flex-col space-y-1 relative">
                    <div class="peer flex space-x-2 items-center">
                        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M9.39767 13.3008C10.6216 12.6488 14.25 10.4075 14.25 6.75C14.25 3.85051 11.8995 1.5 9 1.5C6.10051 1.5 3.75 3.85051 3.75 6.75C3.75 10.4075 7.37836 12.6488 8.60232 13.3008C8.85373 13.4348 9.14627 13.4348 9.39767 13.3008ZM9 9C10.2426 9 11.25 7.99264 11.25 6.75C11.25 5.50736 10.2426 4.5 9 4.5C7.75736 4.5 6.75 5.50736 6.75 6.75C6.75 7.99264 7.75736 9 9 9Z" fill="#222222"/>
                            <path d="M13.5466 12.375C14.0074 12.717 14.25 13.105 14.25 13.5C14.25 13.895 14.0074 14.283 13.5466 14.625C13.0859 14.967 12.4231 15.2511 11.625 15.4486C10.8269 15.646 9.92157 15.75 9 15.75C8.07843 15.75 7.1731 15.646 6.375 15.4486C5.5769 15.2511 4.91415 14.967 4.45337 14.625C3.99258 14.283 3.75 13.895 3.75 13.5C3.75 13.105 3.99258 12.717 4.45337 12.375" stroke="#222222" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                        <span class="text-sm text-slate-800">CBD, Nairobi</span>
                    </div>
                    <span class="hidden absolute top-4 left-2 transition-all peer-hover:block text-sm text-slate-500">Location</span>
                </div>
                <!-- Pricing -->
                <div class="flex flex-col space-y-1 relative">
                    <div class="peer flex space-x-2 items-center">
                        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="2.25" y="4.5" width="13.5" height="9" rx="2" stroke="#222222" stroke-width="2"/>
                            <path d="M4.5 6.75L6 6.75" stroke="#222222" stroke-width="2" stroke-linecap="round"/>
                            <path d="M12 11.25H13.5" stroke="#222222" stroke-width="2" stroke-linecap="round"/>
                            <circle cx="9" cy="9" r="1.25" stroke="#222222" stroke-width="2"/>
                        </svg>
                        <span class="text-sm text-slate-800">Negotiable</span>
                    </div>
                    <span class="hidden absolute top-4 left-2 transition-all peer-hover:block text-sm text-slate-500">Pricing</span>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
       return {
        rating: [1, 2, 3, 4]
       }
    }
}
</script>
<template>
    <div class="absolute -top-4 bg-gray-50 h-full w-full flex flex-col space-y-16 p-4 z-10">
        <span class="self-end mr-8 px-8 py-2 rounded-sm text-sm font-medium bg-[#F3ECD1]
            transition-all hover:bg-[#E9D89D] cursor-pointer capitalize" @click="toggle"
        >Go back</span>
        <!-- Action Modal -->
        <form @submit.prevent="handleSubmit"
            class="w-full flex flex-col space-y-2 border self-center md:max-w-xl flex px-4 py-32 rounded">
            <div class="flex flex-col pb-16 items-center">
                <span v-if="id" class="border-b border-slate-600 py-2 px-8 text-lg font-medium capitalize"
                >Edit {{ service.serviceCategory_name }}</span>
                <span v-else @click="checkServiceId" class="border-b border-slate-600 py-2 px-8 text-lg font-medium capitalize"
                >Create a new service</span>
            </div>
              <!-- service category -->
            <div class="flex space-x-2 w-full items-center">
                <span class="w-1/3 text-md capitalize">service category</span>
                <select class="border rounded-sm w-full border-slate-300 ring-0 focus:ring-0 focus:border-slate-400 text-md
                    capitalize bg-gray-100"
                    v-model="category"
                    @change="setCategory"
                >
                    <option v-for="category in categories" :key="category.id" :value="category.id" class="bg-gray-50"
                    >{{ category.name }}</option>
                </select>   
            </div>
            <!-- service location -->
            <div class="flex space-x-2 w-full items-center">
                <span class="w-1/3 text-md capitalize">service location</span>
                <select class="border rounded-sm w-full border-slate-300 ring-0 focus:ring-0 focus:border-slate-400 text-md
                    capitalize bg-gray-100">
                    <!-- location data for selection options -->
                    <option value="Nairobi" class="bg-gray-50">Nairobi</option>
                    <option value="Lagos" class="bg-gray-50">Lagos</option>
                </select>   
            </div>
             <!-- service description -->
             <div class="flex space-x-2 w-full items-center">
                <span class="w-1/3 text-md capitalize">description</span>
                <input class="border h-16 rounded-sm w-full border-slate-300 ring-0 focus:ring-0 focus:border-slate-400 text-md
                    capitalize bg-gray-100 py-2 text-slate-600" type="text" v-model="description" :class="error && 'highlight'"> 
            </div>
            <div class="flex space-x-2 w-full items-center pt-16">
                <div class="flex justify-between w-full items-center">
                    <input type="submit" @click="setDo('cancel')" value="cancel"
                        class="border border-[#F3ECD1] rounded-sm transition-all hover:bg-[#E9D89D] px-10 py-2 text-md capitalize">
                    <input type="submit" @click="setDo('save')" value="save"
                        class="rounded-sm bg-[#F3ECD1] transition-all hover:bg-[#E9D89D] px-12 py-2 text-md capitalize">
                </div>                 
            </div>

        </form>
    </div>
</template>
<script>
import { mapActions, mapState } from 'vuex'

export default {
    props: ['toggle', 'id', 'setServiceId', 'service', 'reload'],
    data() {
        return {
            do:'',
            // serviceName: 'some service',
            description: '',
            category: '',
            error: '',
        }
    },
    computed: {
        ...mapState(['csrfToken', 'categories', 'loggedInUser'])
    },
    created() {
        this.getCategories() // fetch service categories & set default category
        if (!this.id) {
            this.category = this.categories[0].id
        }
        else {
            this.category = this.service.serviceCategory_id
            this.description = this.service.description
        }
    },
    methods: {
        ...mapActions(['getCategories']),
        setCategory(){
            console.log('selected category: ', this.category)
        },
        setDo(val) {
            this.do = val
            console.log(this.do)
        },
        handleSubmit() {
            console.log(this.do + '-ing')
            // reset/clear serviceId field
            this.setServiceId('')
            // wait a second then (return to home page) - How?
            if (!this.id && !this.description && this.do === 'save') {
                this.error = true
                console.log('service description missing')
                return;
            } else {
                this.toggle()
            }
            console.log(this.description, this.csrfToken)
            let data = {'service_description': this.description};
            data['service_category'] = this.category

            if (this.do === 'save'){
                let provider_id = this.loggedInUser.user_id
                let url = "http://web-01.whosadevnow.tech/api/v1/serviceProviders/" + provider_id + "/services/"
                url += this.id ? this.id + '/edit' : 'create'
                console.log(url)
                fetch(url, {
                method: "POST",
                headers: {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.csrfToken
                },
                credentials: "include",
                body: JSON.stringify(data),
                })
                .then((res) => res.json())
                .then((data) => {
                console.log('created a post: ', data);
                // re-load myServices if serviceAdded & toggle that state back to false:
                if (!this.id) {
                    this.reload() // new service created
                    console.log('serviceAdded')
                }
                })
                .catch((err) => {
                console.log('error: ', err);
                });
            }
        },
        checkServiceId() {
            console.log('clicked ->', this.id)
        }
    }
}
</script>
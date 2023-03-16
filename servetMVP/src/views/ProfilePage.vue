<template>
  <div class="flex flex-col w-full border pb-4">
      <!-- Avatar and name -->
      <div class="w-full flex flex-col justify-center items-center space-y-2 py-2">
          <img src="../assets/scaarif_a_young_kenyan_tomboy_full-body_portrait_light_skinned__0a68fc1a-c258-4865-a6fb-33c81878f822.png"
          alt="" class="w-16 h-16 rounded-full">
          <span class="text-md text-lg font-medium text-slate-600">Jane Doe</span>
      </div>
      <!-- Details (contacts, location and social media links) -->
      <div class="md:max-w-md w-full flex flex-col self-center items-center">
          <div v-for="val, idx in items" :key="idx" class="w-full flex space-x-4 border py-2 px-4">
            <span class="w-1/3 capitalize border-r font-medium text-slate-800">{{ Object.keys(val)[0] }}:</span>
            <select v-if="Object.values(val)[0] === 'links'" 
              name="" id="" class="capitalize py-0 pl-0 hover:text-slate-600 cursor-pointer border-none ring-0 focus:ring-0 focus:border-none bg-gray-50">
              <!-- should be links to these sites (<a></a>) -->
              <option value="fb">facebook</option>
              <option value="ig">instagram</option>
              <option value="tk">tiktok</option>
            </select>
            <span v-else class="capitalize hover:text-slate-600 cursor-pointer">{{ Object.values(val)[0] }}</span>
          </div>
      </div>
      <router-link :to="{name: 'home'}" class="text-md capitalize py-2 px-12 rounded-sm bg-[#F3ECD1] transition-all
        hover:bg-[#E9D89D] cursor-pointer self-end mr-8 mt-8"
      >Go back</router-link>
  </div>
</template>
<script>

export default {
    data() {
      return {
        items: [
          {'mobile number': '+254 700 000000'},
          {'whats app no': '+254 700 000000'},
          {'location': 'CBD, Nairobi'},
          {'social media': 'links'},
        ]
      }
    }
}
</script>
import { createRouter, createWebHistory } from 'vue-router'
import DefaultLayout from '../components/DefaultLayout.vue'
import LoginLayout from '../components/LoginLayout.vue'
import Landing from '../views/Landing.vue'
import TimelineView from '../views/TimelineView.vue'
import ProfilePage from '../views/ProfilePage.vue'
import Services from '../views/Services.vue'
import PlayGround from '../views/PlayGround.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '/',
          name: 'home',
          component: TimelineView
        },
        {
          path: '/landing',
          name: 'landing',
          component: Landing
        },
        {
          path: '/profile',
          name: 'profile',
          component: ProfilePage
        },
        {
          path: '/services',
          name: 'services',
          component: Services
        },
        {
          path: '/play',
          name: 'play',
          component: PlayGround
        },
      ]
    },
    {
      path: '/login', //or some other layout
      name: 'login',
      component: LoginLayout,
    }
  ]
})

export default router

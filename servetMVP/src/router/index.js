import { createRouter, createWebHistory } from 'vue-router'
import DefaultLayout from '../components/DefaultLayout.vue'
import LoginLayout from '../components/LoginLayout.vue'
import Landing from '../views/Landing.vue'
import TimelineView from '../views/TimelineView.vue'
import ProfilePage from '../views/ProfilePage.vue'
import Services from '../views/Services.vue'

import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
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
          path: '/login',
          name: 'login',
          component: Login
        },
        {
          path: '/signup',
          name: 'signup',
         component: SignUp
        },
        {
          path: '/play',
          name: 'play',
          component: PlayGround
        },
      ]
    },
    {
      path: '/user', //or some other layout
      component: LoginLayout,
      children: [
        
      ]
    }
  ]  
})

// guard routes
router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/signup', '/services', '/play', '/landing']
  const authRequired = !publicPages.includes(to.path);
  const token = localStorage.getItem('token');
  console.log('token: ', token)

  //if unauthorized, redirect to login
  if (authRequired && !token) {
    next('/landing')
  } else {
    next()
  }
})

export default router

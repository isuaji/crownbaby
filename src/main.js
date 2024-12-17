import { createRouter, createWebHistory } from 'vue-router'
import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [{
    path: '/',
    name: 'land',
    component: () => import('./components/LandView.vue')
  }, {
    path: '/calendar',
    name: 'calendar',
    component: () => import('./components/CalendarView.vue')
  }]
})

const app = createApp(App)
app.use(router)
app.mount('#app')
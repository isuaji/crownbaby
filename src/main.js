import { createRouter, createWebHistory } from 'vue-router'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import './assets/main.css'

const router = createRouter({
  history: createWebHistory(),
  routes: [{
    path: '/',
    name: 'land',
    component: () => import('./components/LandView.vue')
  }, {
    path: '/calendar/:uid',
    name: 'calendar',
    component: () => import('./components/CalendarView.vue')
  }]
})

const app = createApp(App)
const pinia = createPinia()
app.use(router)
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.mount('#app')

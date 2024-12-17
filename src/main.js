import './assets/main.css';
import { createRouter, createWebHistory } from 'vue-router';
import { createApp } from 'vue';
import App from './App.vue';
import Land from './components/LandView.vue';
import Calendar from './components/CalendarView.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [{
        name: 'Land',
        path: '/', 
        component: Land
    },{
        name: 'Calendar',
        path: '/calendar',
        component: Calendar
    }]
});

const app = createApp(App);
    app.use(router);
    app.mount('#app');
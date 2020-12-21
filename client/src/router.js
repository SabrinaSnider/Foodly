import Vue from 'vue';
import VueRouter from 'vue-router';
import Dashboard from './views/Dashboard.vue'
import List from './views/List.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
    },
    {
      path: '/list/:id',
      name: 'List',
      component: List,
    }
  ],
});

import Vue from 'vue';
import VueRouter from 'vue-router';
import List from './views/List.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/list/:storeName',
      name: 'List',
      component: List,
    }
  ],
});

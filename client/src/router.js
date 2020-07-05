import Vue from 'vue';
import VueRouter from 'vue-router';
import ListView from './views/ListView.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/list/:storeName',
      name: 'ListView',
      component: ListView,
    }
  ],
});

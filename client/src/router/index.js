import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home.vue';
import New from '../components/New.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/new',
      name: 'New',
      component: New,
    },
  ],
});

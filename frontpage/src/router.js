import Vue from "vue";
import Router from "vue-router";
import { authMixin } from './mixins/authMixin';
import VueAxios from 'vue-axios'
import axios from 'axios';

Vue.use(Router);
Vue.use(VueAxios,axios);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/home'
    },
    {
      path: "/home",
      name: "home",
      component: () => import("./components/Home.vue")
    },
    {
      path: "/create",
      name: "create",
      component: () => import("./components/Create.vue")
    },
    {
      path: "/edit/:id",
      name: "edit",
      component: () => import("./components/Edit.vue")
    },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/Index.vue"),
      beforeEnter: (to, from, next) => {authMixin.methods.checkToken("google", next)}
      
    },
  ]
});

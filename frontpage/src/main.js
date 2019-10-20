import Vue from 'vue';
import App from './App';
import router from './router';
import VueRouter from 'vue-router';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import * as VeeValidate from 'vee-validate';
import VueResource from 'vue-resource'
import VueAuthenticate from 'vue-authenticate'
import VueAxios from 'vue-axios'
import axios from 'axios';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(VeeValidate);
Vue.use(VueResource);

/* eslint-disable no-new */

var options = {
  namespace: 'vuejs__'
};
Vue.use(VueRouter);
Vue.use(VueAxios, axios)
Vue.use(VueAuthenticate, {
  providers: {
    google: {
      clientId: '76241932517-io5aulmoch4snc3iss89ejr8rs9kdgc2.apps.googleusercontent.com',
      redirectUri: 'http://localhost:8080/',
      url: 'http://localhost:8000/api/login/social/token_user/google/',
    }
  }
});
//const router = new VueRouter({
 // mode: 'history',s
//});
new Vue({
  el: '#app',
  router,
  render: h => h(App),
});

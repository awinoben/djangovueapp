import Vue from 'vue';
import App from './App';
import router from './router';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
//import VeeValidate from "vee-validate";
//import * as VueThreejs from 'vue-threejs';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

import * as VeeValidate from 'vee-validate';

Vue.use(VeeValidate);
//Vue.use(VueThreejs)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App),
});

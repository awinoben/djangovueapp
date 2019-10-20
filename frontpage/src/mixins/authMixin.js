import VueAxios from 'vue-axios'
import axios from 'axios';
import Vue from 'vue';
import VueResource from 'vue-resource'


Vue.use(VueAxios,axios);
Vue.use(VueResource);

export const authMixin = {
    methods: {
        checkToken: function(provider, redirect){
            axios.post("http://localhost:8000/api/check/", {"token": localStorage.getItem("vue-authenticate.vueauth_token")}).then((response) => {
                    var path = (response.data.status)? true : "/";
                    redirect({ path: path});
                }).catch((error) => {
            });
        },
        authenticate: function(provider) {
            this.$auth.authenticate('google').then(function (response) {
                if(response.data.email === ""){
                   window.location = "/index";
                }
            }).catch(function(error) {
                console.log(error);
            });
        }
    }
}
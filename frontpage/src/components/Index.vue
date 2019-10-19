<template>
    <div class="pt-5">
<table class="table table-striped table-hover">
  <thead>
    <tr>
      <th>#</th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Date of Birth</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="client of clients" v-bind:key="client.patient_id">
      <th></th>
      <th>{{client.first_name}}</th>
      <td>{{client.last_name}}</td>
      <td>{{client.dob}}</td>
      <td>{{client.gender}}</td>
    </tr>
  </tbody>
</table>
        <p  v-if="clients.length == 0">No clients</p>
    </div>
</template>
<script>
import axios from 'axios';
import {APIService} from '../http/APIService';
//const API_URL = 'http://localhost:8000';
const apiService = new APIService();
export default {
    data() {
        return {
            clients: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        //deleteClient: function(clnt) {
            //if (confirm('Delete ' + clnt.first_name)) {
                //axios.delete(`http://127.0.0.1:8000/api/clients/${clnt.patient_id}`)
                    //.then( response => {
                       // this.all();
                   // });
            //}
        //},
    deleteClient(client){
      console.log("deleting client: " + JSON.stringify(client))
      apiService.deleteClient(client).then((r)=>{
        console.log(r);
        if(r.status === 204)
        {
          alert("Client deleted");
          this.$router.go()

        }
      })
    },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/clients/')
                .then( response => {
                    this.clients = response.data
                });
        }
    },
}
</script>
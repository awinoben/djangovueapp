<template>

        <div id="container" class="container">

            <div class="row">

                <div class="col-sm-8 offset-sm-2">
                <div class="alert alert-success" v-show="showCreateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Record successfully created!</strong>
                </div>
                <div class="alert alert-success" v-show="showUpdateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Record successfully updated!</strong>
                </div>

                <div class="alert alert-warning" v-show="showError"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Error!</strong>
                </div>                
                    <h1>Create a Record</h1>
                    <div class="info-form">
                      <form>
                        <div class="form-group">
                <label for="name">First Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="client.first_name"
                    required="required"
                    name="first_name"
                    placeholder="Enter first name">
            </div>
            <div class="form-group">
                <span><label for="name">Last Name</label></span>
                <span><input
                    type="text"
                    class="form-control"
                    id="last_name"
                    v-model="client.last_name"
                   
                    name="last_name"
                    placeholder="Enter last name"></span>
            </div>
            <div class="form-group">
                <span><label for="name">Other Names</label></span>
                <span><input
                    type="text"
                    class="form-control"
                    id="other_names"
                    v-model="client.other_names"
                  
                    name="other_names"
                    placeholder="Enter other name"></span>
            </div>
            <div class="form-group">
                <span><label for="name">Filled</label></span>
                <span><input
                    type="text"
                    class="form-control"
                    id="filled"
                    v-model="client.filled"
                  
                    name="filled"
                    placeholder="Enter N/A.."></span>
            </div>
            <div class="form-group">
                <label for="phone">Id/Passport Number</label>
                <input
                    type="number"
                    name="id_number"
                    
                    class="form-control"
                    id="id_number"
                    v-model="client.id_number"
                    placeholder="Enter Id Number">
            </div>
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input
                    type="number"
                    name="phone_number"
                   
                    class="form-control"
                    id="phone_number"
                    v-model="client.phone_number"
                    placeholder="Enter Phone Number">
            </div>
            <div class="form-group">
                <label for="income">Race</label>
                <select
                    name="race"
                    class="form-control"
                   
                    id="race"
                    v-model="client.race" >
                    <option value="African">African</option>
                    <option value="White">White</option>
                </select>
            </div>
            <div class="form-group">
                <label for="income">Gender</label>
                <select
                    name="gender"
                    class="form-control"
               
                    id="gender"
                    v-model="client.gender" >
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>
            </div>
            <div class="form-group">
                <span><label for="name">Date of Birth</label></span>
                <span><input
                    type="date"
                    class="form-control"
                    id="dob"
                    v-model="client.dob"
                 
                    name="dob"
                    placeholder="Enter other name"></span>
            </div>
            <div class="form-group">
                <span><label for="name">Occupation</label></span>
                <span><input
                    type="text"
                    class="form-control"
                    id="occupation"
                    v-model="client.occupation"
                    
                    name="occupation"
                    placeholder="Enter occupation"></span>
            </div>
            <div class="form-group">
                <label for="income">Income</label>
                <select
                    name="income"
                    class="form-control"
                   
                    id="income"
                    v-model="client.income" >
                    <option value="10000-20000">10000-20000</option>
                    <option value="30000-40000">30000-40000</option>
                </select>
            </div>
            <div class="form-group">
                <label for="income">Education</label>
                <select
                    name="education"
                    class="form-control"
                
                    id="education"
                    v-model="client.education" >
                    <option value="College/University">College/University</option>
                    <option value="High School">High School</option>
                </select>
            </div>
                      </form>
                       <button class="btn btn-primary" v-if="!this.client.pk" @click="createClient()" ><span v-if="!creating">Create</span><span v-if="creating">Creating... Please wait </span></button>
                       <button class="btn btn-primary" v-if="this.client.pk" @click="updateClient()" ><span v-if="!updating">Update</span><span v-if="updating">Updating... Please wait </span></button>
                       <button class="btn btn-primary"  @click="newClient()" >New..</button>

                    </div>
                </div>
            </div>
        </div>

</template>
<script>
import {APIService} from '../http/APIService';

const apiService = new APIService();

export default {
  name: 'ClientCreate',
  components: {
  },
  data() {
    return {
      showCreateMessage: false,
      showUpdateMessage: false,
      showError: false,
      client: {},
      clients: '',
      creating: false,
      updating: false
    };
  }, 
  methods: {
    hideMessage(){
      this.showCreateMessage = false;
      this.showUpdateMessage = false;
      this.showError = false;
    },
    createClient(){
      this.creating = true;
      apiService.createClient(this.client).then((result)=>{
          if(result.status === 201){
            this.client = result.data;
            this.showCreateMessage = true;
          }
          this.creating = false;          
      },(error)=>{
        this.showError = true;
        this.creating = false;
      });
    },
    updateClient(){
      this.updating = true;
     apiService.updateClient(this.client).then((result)=>{
          if(result.status === 200){
            this.showUpdateMessage = true;
          }

      },(error)=>{
        this.showError = true;
        this.updating = false;
      });
    },
    newClient(){
      this.client = {};
    }

  },
  mounted() {

    if(this.$route.params.pk){
        apiService.getClient(this.$route.params.pk).then((client)=>{
        this.client = client;
      })
    }
  },
}
</script>
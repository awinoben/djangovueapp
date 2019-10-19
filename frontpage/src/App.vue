<template>
<div>
<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mr-auto">

          <li class="nav-item">
          <router-link class="btn btn-sm btn-outline-primary" to="/index">Home</router-link>
          </li>
          <li class="nav-item">
          <router-link class="btn btn-sm btn-outline-warning" to="/index">Records</router-link>
          </li>
          <li class="nav-item">
          <router-link to="/create" class="btn btn-sm btn-outline-success">New Record</router-link>
          </li>

        </ul>
          <a href="http://localhost:8000/admin/"  class="btn btn-info btn-margin">Admin</a>

      </div>
    </nav>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <router-view />
      </div>
    </div>
  </div>
  </div>
</template>

<style>
@import './assets/bootstrap-4.0.0/dist/css/bootstrap.min.css';
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
body {
  min-height: 75rem;
  padding-top: 4.5rem;
}
.nav-item{
  padding:1px;
  margin-left: 5px;
}
</style>

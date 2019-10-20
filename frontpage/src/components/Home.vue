<template>
    <main role="main">
      <div class="jumbotron">
        <h1>Django-Vue-App</h1>
        <p class="lead">This application uses Django and Django REST Framework for backend, Vue for the frontend and oAuth2 authentication</p>
      </div>

    <h4>
      <a class="btn btn-primary" @click="authenticate('google')">Log In</a>
    </h4>
    </main>
</template>
<script>
 import { authMixin } from '../mixins/authMixin'

 export default {
    mixins: [ authMixin ],
}
</script>
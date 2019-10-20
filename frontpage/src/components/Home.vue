<template>
    <main role="main">
      <div class="jumbotron">
        <h1>Django-Vue-App</h1>
        <p class="lead">This application uses Django and Django REST Framework for backend, Vue for the frontend and oaAuth2 for handling user's authentication</p>
        <a class="btn btn-lg btn-primary" href="" role="button">View tutorial</a>
      </div>

    <h4 v-if="!authenticated">
      You are not logged in! Please <a class="btn btn-primary" @click="authenticate('google')">Log In</a> to continue.
    </h4>
    </main>
</template>
<script>
 import { authMixin } from '../mixins/authMixin'

 export default {
    mixins: [ authMixin ],
}
</script>
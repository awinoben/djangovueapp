<template>
  <div class="spinner">
    <img src="../assets/logo.png" alt="loading..."/>
  </div>
</template>
<script>
  export default {
    name: 'callback',
    props: ['auth'],
    data () {
      this.auth.handleAuthentication()
      return {}
    }
  }
</script>
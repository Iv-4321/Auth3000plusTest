<template>
  <div class="nav-bar">
    <nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">
      <div class="container mw-0 px-3">
        <a class="navbar-brand" href="/">
        <img src="../assets/brand-name.png" width="" height="27" class="d-inline-block align-top" alt="" loading="lazy">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
            <li class="" v-if="accessToken!=null"><router-link :to = "{ name:'logout' }">Logout</router-link></li>
            <li class="" v-if="accessToken!=null"><router-link :to = "{ name:'posts' }">Home</router-link></li>
            <li class="" v-if="accessToken!=null"><router-link :to = "{ name:'upload' }">Upload book</router-link></li>
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit"><router-link :to = "{ name:'logout' }">Login</router-link></button>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form>

          </ul>
        </div>

      </div>
    </nav>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    name: 'Navbar',
    computed: mapState(['accessToken'])
  }
</script>

<style scoped>
    a {
      color:#000;
  }
</style>
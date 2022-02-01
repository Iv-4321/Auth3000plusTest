<template>
  <div id="app">
    <NavBar></NavBar>
    <router-view/>
  </div>
</template>

<script>
import NavBar from './components/Navbar'


export default {
  name: 'App',

  components: {
    NavBar
  },
}
</script>

<style>
  body {
    margin: 0;
    padding: 0;
    background-color:#f8f8f8!important;
  }
</style>

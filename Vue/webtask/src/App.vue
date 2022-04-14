<template>
  <div id="app">
    <router-link to="/">HomePage</router-link>
    <router-link to="/ComparePage">ComparePage</router-link>
    <router-view :key="$route.path"></router-view>

     <v-app id="inspire">

     </v-app>

  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

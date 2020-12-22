<template>
  <v-app>
    <v-app-bar app clipped-left color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <h1 id="app-title" v-on:click="openDashboard">FOODLY</h1>
    </v-app-bar>

    <v-navigation-drawer app clipped v-model="drawer">
      <v-list dense> </v-list>
    </v-navigation-drawer>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import router from './router';

export default {
  name: 'app',
  data() {
    return { drawer: 'open' };
  },
  methods: {
    openDashboard: function openDashboard() {
      router.push('/dashboard');
    },
  },
};
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,600;0,700;0,800;1,300;1,400;1,600;1,700;1,800&display=swap');
@import './scss/colors';

* {
  font-family: 'Open Sans', sans-serif;
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}

#app-title {
  color: white;
  cursor: pointer;
}
</style>

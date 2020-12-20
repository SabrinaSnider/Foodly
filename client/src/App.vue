<template>
  <div id="app">
    <Navbar v-bind:isLoggedIn="false"></Navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/Navbar';

export default {
  name: 'app',
  components: {
    Navbar,
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

#app {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  min-height: 100vh;
  background-color: white;
}

.page {
  flex-grow: 1;
}
</style>

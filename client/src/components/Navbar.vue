<template>
  <nav id="nabar">
    <h1>FOODLY</h1>

    <a v-if="isLoggedIn">Log Out</a>
    <a class="bordered" v-else>Log In</a>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: ['isLoggedIn']
}
</script>

<style scoped lang="scss">
@import '../scss/colors';

nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 10px 60px;
  background-color: $green;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  align-items: center;

  // Shadow
  -webkit-box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75);
  -moz-box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75);
  box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75);
}

h1 {
  display: inline;
  font-weight: 700;
  font-size: 1.6rem;
  color: $offWhite;
}

a {
  background-color: transparent;
  color: $offWhite;
  font-size: 1.2rem;
  height: fit-content;
  padding: 3px 20px;
  vertical-align: middle;
  font-weight: 600;
  cursor: pointer;
}

a.bordered {
  border-radius: 3px;
  border: 2px solid $offWhite;
}

a.bordered:hover {
  background-color: $offWhite;
  color: $green;
}
</style>

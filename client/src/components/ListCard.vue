<template>
  <v-card elevation="2" class="mx-auto" max-width="400">
    <v-img
      src="https://i1.wp.com/www.eatthis.com/wp-content/uploads/2019/05/grocery-cart-in-isle-blurred-background.jpg?fit=1200%2C800&ssl=1"
      height="200px"
    ></v-img>

    <v-card-title>
      List name here
    </v-card-title>

    <v-card-subtitle>
      Raw list view here
    </v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  name: 'ListCard',
  props: ['list'],
};
</script>

<style scoped lang="scss">
@import '../scss/colors';
</style>

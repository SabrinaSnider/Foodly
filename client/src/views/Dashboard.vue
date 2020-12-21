<template>
  <v-container class="pa-12">
    <ListCard></ListCard>
  </v-container>
</template>

<script>
import ListCard from '../components/ListCard';

export default {
  name: 'Dashboard',
  components: { ListCard },
};
</script>

<style scoped lang="scss">
@import '../scss/colors';
</style>

<template>
  <v-container pa-4 fluid>
    <v-layout>
      <v-flex align-center justify-start row>
        <ListCard
          v-for="groceryList in groceryLists"
          :key="groceryList.id"
          v-bind:groceryList="groceryList"
        ></ListCard>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ListCard from '../components/ListCard';
import { getLists } from '../utils/serverUtils';

export default {
  name: 'Dashboard',
  components: { ListCard },
  data() {
    return { groceryLists: [] };
  },
  async mounted() {
    const response = await getLists();
    this.groceryLists = response.data;
    console.log(this.groceryLists);
  },
};
</script>

<style scoped lang="scss">
@import '../scss/colors';
</style>

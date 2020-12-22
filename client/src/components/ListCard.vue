<template>
  <v-card class="ma-4" elevation="2" width="300px" v-on:click="open">
    <v-card-title class="card-title">
      {{ groceryList.name }}
      <v-btn
        icon
        small
        v-on:click.stop
        v-on:click="deleteGroceryList(groceryList.id)"
      >
        <img type="image" class="delete-list-icon" src="/delete.svg" />
      </v-btn>
    </v-card-title>

    <v-card-subtitle>
      <p v-if="groceryList.products.length == 1">
        {{ groceryList.products.length }} item
      </p>
      <p v-else>{{ groceryList.products.length }} items</p>
    </v-card-subtitle>
  </v-card>
</template>

<script>
import { getList } from '../utils/serverUtils';
import router from '../router';
import { deleteList } from '../utils/serverUtils';

export default {
  name: 'ListCard',
  props: ['groceryList'],
  data() {
    return this.groceryList;
  },
  async mounted() {
    const response = await getList(this.$route.params.id);
    this.groceryList = response.data;
  },
  methods: {
    open: function open() {
      router.push(`/lists/${this.groceryList.id}`);
    },
    deleteGroceryList: async function deleteGroceryList(listId) {
      await deleteList(listId);
    },
  },
};
</script>

<style scoped lang="scss">
@import '../scss/colors';

p {
  padding: 0px;
}

.card-title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.delete-list-icon {
  height: 20px;
  width: 20px;
  padding: 3px;
}
</style>

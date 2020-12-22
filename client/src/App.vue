<template>
  <v-app>
    <v-app-bar app clipped-left color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <h1 id="app-title" v-on:click="openDashboard">FOODLY</h1>
    </v-app-bar>

    <v-navigation-drawer app clipped v-model="drawer">
      <v-list dense>
        <v-subheader>GROCERY LISTS</v-subheader>
        <v-list-item-group v-model="selectedItem" color="primary">
          <v-list-item
            v-for="groceryList in groceryLists"
            :key="groceryList.id"
          >
            <v-list-item-content>
              <v-list-item-title
                v-on:click="openList(groceryList.id)"
                v-text="groceryList.name"
              ></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import router from './router';
import { getLists } from './utils/serverUtils';

export default {
  name: 'app',
  data() {
    return { drawer: 'open', groceryLists: [] };
  },
  async mounted() {
    const response = await getLists();
    this.groceryLists = response.data;
  },
  methods: {
    openDashboard: function openDashboard() {
      router.push('/dashboard');
    },
    openList: function openList(listId) {
      router.push(`/lists/${listId}`);
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

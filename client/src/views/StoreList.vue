<template>
  <div id="list-container" class="page">
    <h2 id="store-name">{{$route.params.storeName | capitalize}}</h2>
    <div id="list">
      <ul v-for="(productList, location) in data" :key="location">
        <h3>{{location}}</h3>
        <Checkbox v-for="product in productList" :key="product.id" v-bind:product="product"></Checkbox>
      </ul>
    </div>
  </div>
</template>

<script>
import Checkbox from '../components/Checkbox';
import axios from 'axios';

export default {
  name: "StoreList",
  components: {
    Checkbox
  },
  data() {
    return {
      data: {}
    }
  },
  mounted () {
    axios.get('http://localhost:5000/all')
    .then(
      response => (
        this.data = response.data
      )
    )
  }
}
</script>

<style scoped lang="scss">
@import '../scss/colors';

#list-container {
  width: 800px;
  margin: auto;
}

#store-name {
  margin: 30px 0px;
  font-size: 2rem;
}

#list {
  background-color: white;
  border: 1px solid $gray;
  border-radius: 3px;
  padding: 20px;
}
</style>

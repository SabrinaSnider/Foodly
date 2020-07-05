<template>
  <div id="list-container" class="page">
    <h2 id="store-name">{{$route.params.storeName | capitalize}} Shopping List</h2>
    <div id="list">
      <ul v-for="(productList, location) in data" :key="location">
        <h3>{{location}}</h3>
        <Checkbox v-for="product in productList" :key="product.id" v-bind:product="product"></Checkbox>
      </ul>
      <div id="add-item">
        <img id="add-item-icon" src="/plus.svg">
        <input id="add-item-input" type="text" name="productName">
      </div>
    </div>
  </div>
</template>

<script>
import Checkbox from '../components/Checkbox';
import { getAllData } from '../listData'

export default {
  name: "ListView",
  components: {
    Checkbox
  },
  data() {
    return { data: {} }
  },
  mounted () {
    getAllData().then(response => this.data = response.data)
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

ul {
  margin-bottom: 20px;
}

#list {
  background-color: white;
  border: 1px solid $gray;
  border-radius: 3px;
  padding: 20px;
}

#add-item {
  display: flex;
  flex-direction: row;
  align-items: center;
}

#add-item-icon {
  height: 15px;
  width: 15px;
  margin-right: 10px;
}

#add-item-input {
  border: 1px solid $gray;
  border-radius: 15px;
  flex-grow: 1;
  font-size: 1.2rem;
}
</style>

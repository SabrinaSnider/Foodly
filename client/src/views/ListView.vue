<template>
  <div id="list-container" class="page">
    <h2 id="store-name">{{$route.params.storeName | capitalize}} Shopping List</h2>
    <div id="list">
      <ul v-for="productList in data" v-bind:id="aisle" v-bind:key="productList[0]">
        <div class="aisle-header">
          <h3>{{productList[0]}}</h3><span></span>
        </div>
        <Checkbox v-for="product in productList[1]" :key="product.id" v-bind:product="product"></Checkbox>
      </ul>
      <div id="add-item">
        <img v-on:click="add" type="image" id="add-item-icon" src="/plus.svg">
        <input id="add-item-input" type="text" name="productName" placeholder="add item">
      </div>
    </div>
  </div>
</template>

<script>
import Checkbox from '../components/Checkbox';
import { getAllData, addItem } from '../listData'

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
  },
  methods: {
    add: function add() {
      addItem(document.getElementById("add-item-input").value)
      .then(response => {
        console.log(response)
        location.reload()
      })
    }
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
  margin-top: 30px;
  padding: 10px;
  font-size: 2rem;
  font-weight: 600;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  text-align: center;
  color: white;
  background-color: $green;
}

ul {
  margin-bottom: 20px;
}

#list {
  background-color: white;
  border: 1px solid $offWhite;
  border-top: none;
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  padding: 20px;
}

.aisle-header {
  display: flex;
  flex-direction: row;
  align-items: center;

  span {
    text-align: center; 
    background-color: $gray; 
    height: .1rem;
    flex: 1;
    margin-left: 10px;
  }
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
  cursor: pointer;
}

#add-item-input {
  border: none;
  flex-grow: 1;
  font-size: 1.2rem;
  padding: 3px 10px;
}
</style>

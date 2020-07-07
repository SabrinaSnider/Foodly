<template>
  <div class="checkbox-item">
    <input type="checkbox" :id="id" v-model="obtained" v-on:click="toggle">
    <div class="checkbox-label">
      <label :for="id" v-bind:class="{'obtained': obtained}"> {{name}}</label>
      <img v-on:click="deleteCheckbox" type="image" class="delete-item-icon" src="/delete.svg">
    </div>
  </div>
</template>

<script>
import { removeItem, toggleItemObtained } from '../listData'

export default {
  name: "Checkbox",
  props: ['product'],
  data() {
    return {
      id: this.product.id,
      name: this.product.name,
      location: this.product.publixLocation,
      section: this.product.publixSection,
      obtained: this.product.obtained,
    }  
  },
  methods: {
    deleteCheckbox: function() { 
      removeItem(this.id)
      .then(response => {
        console.log(response)
        location.reload()
      })
    },
    toggle: function() {
      toggleItemObtained(this.id)
    }
  }
}
</script>

<style scoped lang="scss">
@import '../scss/colors';

input[type="checkbox"] {
  height: 15px;
  width: 15px;
}

.checkbox-item {
  font-size: 1.2rem;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.checkbox-label {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  flex-grow: 1;
  padding-left: 5px;
}

.obtained {
  color: $gray;
  text-decoration: line-through;
}

.delete-item-icon {
  height: 15px;
  width: 15px;
  margin-left: 20px;
  cursor: pointer;
}
</style>

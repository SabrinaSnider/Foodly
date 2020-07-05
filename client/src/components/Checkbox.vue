<template>
  <div class="checkbox-item">
    <input type="checkbox" :id="id" :required="obtained ? true : false">
    <div class="checkbox-label">
      <label :for="id"> {{name}}</label>
      <label v-if="section" :for="id"> {{section}}</label>
    </div>
  </div>
</template>

<script>
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

</style>

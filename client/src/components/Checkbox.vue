<template>
  <div class="checkboxItem">
    <input type="checkbox" :id="id" :required="obtained ? true : false">
    <label :for="id"> {{name}}</label><br>
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
      obtained: this.product.obtained,
    }  
  },
}
</script>

<style scoped lang="scss">
@import '../scss/colors';

.checkboxItem {
  font-size: 1.2rem;
}

</style>

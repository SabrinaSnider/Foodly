<template>
  <div id="list-container" class="page">
    <h2 id="store-name">{{$route.params.storeName | capitalize}}</h2>
    <div id="list">
      item
    </div>
  </div>
</template>

<script>
export default {
  name: "StoreList"
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
  border: 2px solid $gray;
  border-radius: 5px;
  padding: 20px;
}

</style>

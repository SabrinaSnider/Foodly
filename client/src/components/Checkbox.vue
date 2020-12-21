<template>
  <div class="checkbox-item">
    <input
      type="checkbox"
      :id="productId"
      v-model="obtained"
      v-on:click="toggleCheckbox"
    />
    <div class="checkbox-label">
      <label :for="productId" v-bind:class="{ obtained: obtained }">
        {{ name }}</label
      >
      <img
        v-on:click="deleteCheckbox"
        type="image"
        class="delete-item-icon"
        src="/delete.svg"
      />
    </div>
  </div>
</template>

<script>
import { deleteProduct, toggleProduct } from '../listData';

export default {
  name: 'Checkbox',
  props: ['product', 'listId'],
  data() {
    return {
      productId: this.product.id,
      name: this.product.name,
      location: this.product.publixLocation,
      section: this.product.publixSection,
      obtained: this.product.obtained,
    };
  },
  methods: {
    deleteCheckbox: async function() {
      await deleteProduct(this.listId, this.productId);
      location.reload();
    },
    toggleCheckbox: async function() {
      await toggleProduct(this.listId, this.productId);
    },
  },
};
</script>

<style scoped lang="scss">
@import '../scss/colors';

input[type='checkbox'] {
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
  height: 30px;
  width: 30px;
  padding: 5px;
  border-radius: 50%;
  margin-left: 20px;
  cursor: pointer;
}

.delete-item-icon:hover {
  background-color: $offWhite;
}
</style>

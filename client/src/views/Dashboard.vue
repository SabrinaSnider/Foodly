<template>
  <div>
    hello world
    <ListCard></ListCard>
  </div>
</template>

<script>
import ListCard from '../components/ListCard';

export default {
  name: 'Dashboard',
  components: { ListCard },
};
</script>

<style scoped lang="scss">
@import '../scss/colors';
</style>

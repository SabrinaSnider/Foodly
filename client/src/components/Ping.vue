<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data () {
    return {
      msg: 'no data response'
    }
  },
  mounted () {
    axios.get('http://localhost:5000/ping')
    .then(
      response => (this.msg = response.data)
    )
  }
};
</script>

<style scoped lang="scss">
@import '../scss/colors';

p {
  color: $orangeRed;
}

</style>

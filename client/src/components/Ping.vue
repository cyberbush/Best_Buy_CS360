<template>
  <div class="container">
    <h2>Ping</h2>
    <button type="button" class="btn btn-primary">{{ msg }}</button>
    <br>
    <a href="/"><u>Go back to Home</u></a>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },    
  },
  created() {
    this.getMessage();
  },
};
</script>

<template>
  <div>
    <a-button type="primary" shape="circle" size="small" @click="finshTask">
      √
    </a-button>
  </div>
</template>

<script>

import reqwest from 'reqwest';
export default {
  props: ['taskID', 'currentstatus'],
  methods: {
    finshTask () {
      const axios = require('axios');
      axios.post('http://192.168.0.29:5350/finshtask', {
        formdata: this.taskID,
      })
        .then((response) => {
          console.log(response);
          reqwest({
            url: 'http://192.168.0.29:5350/selecttask',
            type: 'json',
            method: 'get',
            data: { status: this.currentstatus },
            contentType: 'application/json',
            success: res => {
              console.log(res);
              this.$emit('updateTask', res.results)
            },
          });

        })
        .catch(function (error) {
          console.log(error);
        });
    }
  }
}
</script>
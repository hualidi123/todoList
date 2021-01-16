<template>
  <div>
    <a-range-picker
      v-decorator="[
        'dateTime',
        {
          rules: [{ required: true, message: 'Please choose the dateTime' }],
        },
      ]"
      style="width: 100%;"
      :get-popup-container="(trigger) => trigger.parentNode"
      :show-time="{ format: 'HH:mm' }"
      format="YYYY-MM-DD HH:mm"
      :placeholder="['啥时候开始', '啥时候结束']"
      @change="onChange"
      @ok="onOk"
    />
  </div>
</template>
<script>
export default {
  methods: {
    onChange (value, dateString) {
      console.log('Selected Time: ', value);
      console.log('Formatted Selected Time: ', dateString);
    },
    onOk (value) {
      console.log('onOk: ', value);
    },
  },
};
</script>

<template>
  <div>
    <a-button type="primary" @click="showDrawer">
      <a-icon type="plus" /> Add list
    </a-button>
    <a-drawer
      title="Create a new account"
      :width="720"
      :visible="visible"
      :body-style="{ paddingBottom: '80px' }"
      @close="onClose"
    >
      <a-form :form="form" layout="vertical" hide-required-mark>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="What">
              <a-input
                v-decorator="[
                  'name',
                  {
                    rules: [{ required: true, message: '什么事' }],
                  },
                ]"
                placeholder="什么事"
              />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="Level">
              <a-select
                v-decorator="[
                  'level',
                  {
                    rules: [{ required: true, message: '多重要？' }],
                  },
                ]"
                placeholder="多重要？"
              >
                <a-select-option value="level1">
                  小事
                </a-select-option>
                <a-select-option value="level2">
                  一般
                </a-select-option>
                <a-select-option value="level3">
                  大事
                </a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="Helper">
              <a-input
                v-decorator="[
                  'helper',
                  {
                    rules: [{ required: false, message: '帮帮我' }],
                  },
                ]"
                placeholder="帮帮我"
              />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="begintime-  endtime">
              <a-range-picker
                v-decorator="[
                  'dateTime',
                  {
                    rules: [
                      { required: true, message: 'Please choose the dateTime' },
                    ],
                  },
                ]"
                style="width: 100%;"
                :get-popup-container="(trigger) => trigger.parentNode"
                :show-time="{ format: 'HH:mm' }"
                format="YYYY-MM-DD HH:mm"
                :placeholder="['啥时候开始', '啥时候结束']"
              />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="24">
            <a-form-item label="Notice">
              <a-textarea
                v-decorator="[
                  'notice',
                  {
                    rules: [{ required: false }],
                  },
                ]"
                :rows="4"
                placeholder="有什么需要备注的吗？"
              />
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
      <div
        :style="{
          position: 'absolute',
          right: 0,
          bottom: 0,
          width: '100%',
          borderTop: '1px solid #e9e9e9',
          padding: '10px 16px',
          background: '#fff',
          textAlign: 'right',
          zIndex: 1,
        }"
      >
        <a-button :style="{ marginRight: '8px' }" @click="onClose">
          Cancel
        </a-button>
        <a-button type="primary" @click="handleSubmit">
          Submit
        </a-button>
      </div>
    </a-drawer>
  </div>
</template>
<script>
import reqwest from 'reqwest';

export default {
  props: ['currentstatus'],
  data () {
    return {
      form: this.$form.createForm(this),
      visible: false,
      pretask: []
    };
  },
  methods: {
    showDrawer () {
      this.visible = true;
    },
    onClose () {
      console.log(this.form)
      this.visible = false;
    },
    handleSubmit (e) {
      const axios = require('axios');
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
          this.visible = false;
          axios.post('http://192.168.0.29:5350/inserttask', {
            formdata: values,
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
                  this.$emit('updateData', res.results)
                },
              });
            })
            .catch(function (error) {
              console.log(error);
            });
        }
      });
    },
  },
};
</script>

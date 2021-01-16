<template>
  <a-layout id="components-layout-demo-fixed">
    <a-layout-header :style="{ position: 'fixed', zIndex: 1, width: '100%' }">
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :default-selected-keys="['2']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item
          v-for="(item, index) in mainlist"
          :key="index"
          @click="
            currentitem = item;
            currentindex = index;
          "
        >
          {{ item }}
        </a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content :style="{ padding: '0 50px', marginTop: '64px' }">
      <a-breadcrumb :style="{ margin: '16px 0' }">
        <a-breadcrumb-item>{{ currentitem }}</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ background: '#fff', padding: '24px', minHeight: '380px' }">
        <component
          v-if="currentindex === 0"
          :is="currentcomponent"
          @updateData="updateData"
          :currentstatus="(currentindex + 1)"
        ></component>
        <component
          v-if="currentindex === 0 || currentindex === 1 || currentindex === 2"
          :is="tasklist"
          :key="currentindex"
          :data="data"
          @updateData="updateData"
          :currentstatus="(currentindex + 1)"
        ></component>
      </div>
    </a-layout-content>
    <a-layout-footer :style="{ textAlign: 'center' }">
      xbOnline ©2018 Created by v-Ga
    </a-layout-footer>
  </a-layout>
</template>

<script>
import addlist from './addlist'
import cardlist from './cardcom'
import tasklist from './tasklist'

export default {
  data () {
    return {
      currentitem: "计划书",
      currentcomponent: "addlist",
      currentindex: "",
      tasklist: "tasklist",
      data: []
    }
  },
  props: ['mainlist'],
  components: { addlist, cardlist, tasklist },
  methods: {
    updateData (data) {
      this.data = data
    }
  }
}
</script>

<style>
#components-layout-demo-fixed .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
}
</style>

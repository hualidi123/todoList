<template>
  <div
    class="demo-infinite-container"
    :infinite-scroll-disabled="busy"
    :infinite-scroll-distance="10"
  >
    <a-list :data-source="data">
      <a-list-item
        slot="renderItem"
        slot-scope="item"
        v-infinite-scroll="handleInfiniteOnLoad"
      >
        <a-list-item-meta :description="item.notice">
          <a slot="title">{{ item.name }}</a>
          <a-avatar slot="avatar" src="" />
        </a-list-item-meta>
        <div>
          <tagcom
            v-if="item.level == 'level1'"
            :color="'#87d068'"
            :content="'小事'"
          ></tagcom>
          <tagcom
            v-else-if="item.level == 'level2'"
            :color="'#00FFFF'"
            :content="'正事'"
          ></tagcom>
          <tagcom
            v-else-if="item.level == 'level3'"
            :color="'#FF4500'"
            :content="'大事'"
          ></tagcom>
        </div>
        <div>
          <tagcom :color="'#008c8c'" :content="item.helper"></tagcom>
        </div>
        <div>
          <tagcom
            :color="'#7FFF00'"
            :content="new Date(item.begintime * 1000).toLocaleString()"
          ></tagcom>
        </div>
        <div>
          <tagcom
            :color="'#CD2626'"
            :content="new Date(item.endtime * 1000).toLocaleString()"
          ></tagcom>
        </div>
        <div>
          <buttoncom
            v-if="currentstatus == 2"
            :taskID="item.id"
            :currentstatus="currentstatus"
            @updateTask="updateTask"
          ></buttoncom>
        </div>
      </a-list-item>
      <div v-if="loading && !busy" class="demo-loading-container">
        <a-spin />
      </div>
    </a-list>
  </div>
</template>
<script>
import tagcom from './tagcom';
import buttoncom from './buttoncom'
import reqwest from 'reqwest';
import infiniteScroll from 'vue-infinite-scroll';
const fakeDataUrl = 'http://192.168.0.29:5350/selecttask';
export default {
  props: ['currentstatus', 'data'],
  components: { tagcom, buttoncom },
  directives: { infiniteScroll },
  data () {
    return {
      loading: false,
      busy: false,
    };
  },
  created () {
    this.fetchData(res => {
      console.log(res)
      this.$emit('updateData', res.results)
    });
  },
  methods: {
    fetchData (callback) {
      reqwest({
        url: fakeDataUrl,
        type: 'json',
        method: 'get',
        data: { status: this.currentstatus },
        contentType: 'application/json',
        success: res => {
          callback(res);
        },
      });
    },
    handleInfiniteOnLoad () {
      const data = this.data;
      this.loading = true;
      console.log(this, data)

      if (data.lengith >= 10) {
        this.$message.warning('Infinite List loaded all');
        this.busy = true;
        this.loading = false;
        return;
      }
      this.fetchData(res => {
        console.log(res)
        // this.data = data.concat(res.results);
        this.loading = false;
      });
    },
    updateTask (resdata) {
      this.data = resdata
    }
  },
};
</script>
<style>
.demo-infinite-container {
  border: 1px solid #e8e8e8;
  border-radius: 4px;
  overflow: auto;
  padding: 8px 24px;
  height: 300px;
}
.demo-loading-container {
  position: absolute;
  bottom: 40px;
  width: 100%;
  text-align: center;
}
</style>
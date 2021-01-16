<template>
  <div id="app">
<mainhtml :mainlist="mainlist"></mainhtml>
  </div>
</template>

<script>
import mainhtml from './components/mainhtml'


export default {
  name: 'App',
  components: {
    mainhtml
  },
  data(){
   return {
     mainlist:['预定计划','进行中','已完成']

}
  }
}
</script>

<style>

</style>

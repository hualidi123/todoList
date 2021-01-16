import Vue from 'vue'
import App from './App.vue'
import { Tag, message, Avatar, Spin, DatePicker, Button, Layout, Col, Row, Breadcrumb, Menu, Drawer, Form, Icon, Input, Select, Card, List } from 'ant-design-vue';
Vue.use(DatePicker);
Vue.use(Button);
Vue.use(Layout);
Vue.use(Col);
Vue.use(Row);
Vue.use(Breadcrumb);
Vue.use(Menu);
Vue.use(Drawer);
Vue.use(Form);
Vue.use(Icon);
Vue.use(Input);
Vue.use(Select);
Vue.use(Card);
Vue.use(List);
Vue.use(Spin);
Vue.use(Avatar);
Vue.use(Tag);

Vue.prototype.$message = message
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

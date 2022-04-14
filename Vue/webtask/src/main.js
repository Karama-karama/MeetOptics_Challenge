// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import { createApp } from "vue";
import router from "./router";
import vuetify from "@/plugins/vuetify";

Vue.config.productionTip = false;
Vue.mixin({
  created: function() {
    var compare = this.$page.selected;
  }
});

export const bus = new Vue();
new Vue({
  vuetify,
  el: "#app",
  router,
  components: { App },
  template: "<App/>"
}).$mount("#app");

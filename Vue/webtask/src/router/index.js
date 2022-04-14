import Vue from "vue";
import router from "vue-router";
import HomePage from "@/components/HomePage";
import ComparePage from "@/components/ComparePage";
Vue.use(router);

export default new router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage
    },
    {
      path: "/ComparePage",
      name: "ComparePage",
      component: ComparePage
    }
  ]
});

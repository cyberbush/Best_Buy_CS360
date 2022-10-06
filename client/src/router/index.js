import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home.vue";
import Ping from "../components/Ping.vue";

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home, 
  },
  {
    path: "/ping",
    name: "Ping",
    component: Ping
  },
];

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
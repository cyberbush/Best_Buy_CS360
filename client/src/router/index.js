import Vue from "vue";
import Router from "vue-router";
import Books from "../components/Books.vue";
import Ping from "../components/Ping.vue";

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'Books',
    component: Books, 
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
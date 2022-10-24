import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home.vue";
import Ping from "../components/Ping.vue";
import Vendor from "../components/Vendor.vue";
import User from "../components/User.vue";
import Product from "../components/Product.vue";
import Services from "../components/Services.vue";

Vue.use(Router);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/ping",
    name: "Ping",
    component: Ping,
  },
  {
    path: "/vendor",
    name: "Vendor",
    component: Vendor,
  },
  {
    path: "/user",
    name: "User",
    component: User,
  },
  {
    path: "/Product",
    name: "Product",
    component: Product,
  },
  {
    path: "/Services",
    name: "Services",
    component: Services,
  },
];

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

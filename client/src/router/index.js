import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home.vue";
import Vendor from "../components/Vendor.vue";
import User from "../components/User.vue";
import Product from "../components/Product.vue";
import about from "../components/about.vue";
import help from "../components/help.vue";
import ProductMenu from "../components/ProductMenu.vue";
import Signup from "../components/Signup.vue";
import Login from "../components/Login.vue";
import Dashboard from "../components/dashboard.vue";

Vue.use(Router);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/vendor",
    name: "Vendor",
    component: Vendor,
  },
  {
    path: "/User/:id",
    name: "User",
    component: User,
  },
  {
    path: "/Product",
    name: "Product",
    component: Product,
  },
  {
    path: "/about",
    name: "about",
    component: about,
  },
  {
    path: "/help",
    name: "help",
    component: help,
  },
  {
    path: "/Product_Menu",
    name: "ProductMenu",
    component: ProductMenu,
  },
  {
    path: "/Login",
    name: "Login",
    component: Login,
  },
  {
  path: "/Signup",
  name: "Signup",
  component: Signup,
  },
  {
  path: "/Dashboard/:id",
  name: "Dashboard",
  component: Dashboard,
  },
];

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

<template>
<div id="productMenu" class="container">
    <h1> Product Menu </h1>
    <!-- <form> -->
        <div class="form-group">
            <label for="product_name">Name</label>
            <input type="text" class="form-control" id="product_name" v-model="product_name" placeholder="Enter name">
        </div>
        <div class="form-group">
            <label for="product_price">Price</label>
            <input type="text" class="form-control" id="product_price" v-model="product_price" placeholder="Enter price">
        </div>
        <div class="form-group">
            <label for="product_desc">Description</label>
            <input type="text" class="form-control" id="product_desc" v-model="product_desc" placeholder="Enter description">
        </div>
        <div class="form-group">
            <label for="product_category">Category</label>
            <input type="text" class="form-control" id="product_category" v-model="product_category" placeholder="Enter category">
        </div>
        <div class="form-group">
            <label for="product_status">Status</label>
            <input type="text" class="form-control" id="product_status" v-model="product_status" placeholder="Enter status">
        </div>
        <button class="btn btn-primary" @click="update_product(id=-1, name=product_name, price=product_price, description=product_desc, category=product_category, status=product_status, delete_=false)">Add New product</button>
    <!-- </form> -->
    <h2> Product Table </h2>
    <div id="productTable" class="productTable">
        <ul>
            <li v-for="product in products" :key="product.id"> 
            {{ product.name + " | $" + product.price + " | " + product.description + " | " + product.category + " | " + product.status }}<button class="btn btn-primary" @click="update_product(id=product.id, name='', price=0.0, description='', category='', status='', delete_=true)">Delete</button>
            </li>
        </ul>
    </div>
</div>
</template>

<script>
// import { setTimeout } from "timers";
export default {
  name: "product_comp",
  data: function() {
    return {
      product_name: "",
      product_price: "",
      product_category: "",
      product_desc: "",
      product_status: "",
      products: [
        { id: 0, name: "", price: 0.00, description: "", category: "", status: ""},
      ],
    };
  },
  mounted: function() {
    this.read_products();
  },
  computed: {
  },
  methods: {
    // all the methods will be replaced with REST API call later
    read_products: function() {
        this.axios
            .get("http://localhost:5000/products_db")
            .then(response => (this.products = response.data))
            .catch(error => { console.log(error.response) });
    },
    update_product: function( id = -1, name = "", price = 0.00, description = "", category= "", status = "", delete_ = false) 
    {
        var data = { id: id, name: name, price:price, description: description, category:category, status: status, delete: delete_ };
        this.axios
            .post("http://localhost:5000/products_db", data)
            .then(() => this.read_products())
            .catch(error => { console.log(error.response) });
        //   add a delay to make sure the backend respond
    },
    print: function(data){
        console.log(data)
    }
  }
};

</script>

<style>
.productTable {
    background-color: white;
    margin: auto;
    margin-top: 50px;
    border: 6px solid #0AF;
    padding: 50px;
    text-align: center;
}
</style>
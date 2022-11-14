<template>

  <!--
    THINGS TO FINSIH 10-21-22
  1. banner picture
  2. finish styling for demo
  3. figure out how to import from DBMS
  4. Finish nav-bar design
  5. Login system
  -->
  <body class="gradient-custom-HomePage">
      <!--Upper Nav-Bar-->
      <div class="gradient-custom-HomePage">
          <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-secondary">
            <a class="navbar-brand" href="/"> Best Buy!
            </a>
            <ul class="navbar-nav">
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Menu
                </a>
                <div class="dropdown-menu bg-primary" aria-labelledby="navbarDropdown">
                  <a class="dropdown-item text-justify" href="/">Log Out</a>
                  <a class="dropdown-item text-justify" href="/User/this.currentUser.id">Home</a>
                  <a class="dropdown-item text-justify" href="Product">Products</a>
                  <a class="dropdown-item text-justify" href="about">About</a>
                  <a class="dropdown-item text-justify" href="help">Help</a>
                </div>
              </li>
            </ul>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <form class="form-inline mx-auto my-2">
                    <input class="form-control mr-sm-1" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-dark my-2 my-sm-0" type="submit">Search</button>
                </form>
            </div>
            <p class="" v-if="currentUser!=null">Logged in as {{this.currentUser.firstName}}</p>
          </nav>
        </div>
        <!--BANNER SECTION-->
        <!--END BANNER SECTION-->
        <!--main body columns and rows-->

        <!--This area is the base for the many products that will show up, and as we add/ subtract items from the DB
        we will see it grow and shrink... doing test run with arrays at this time to make sure using base level scripts 
        in page... TJR 11/10/2022
      
        UPDATE 11/11/2022: redesign in process, linking products database to system, will have cards... looking for good ecommerse page layout
        as well =) DONT PANIC... and dont forget a towel!--> 

        <!--Main layout-->
  <main class="mt-2 pt-4">
    <h3 class="text-center"> Featured Product:</h3>
    <div class="container-fluid dark-grey-text mt-5">

      <!--Grid row-->
      <div class="row wow fadeIn border bg-white">

        <!--Grid column-->
        <div class="col-md-6 mb-4">

          <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Products/14.jpg" class="img-fluid" alt="">

        </div>
        <!--Grid column-->

        <!--Grid column-->
        <div class="col-md-6 mb-4">

          <!--Content-->
          <div class="p-4">

            <div class="mb-3">
              <a href="">
                <span class="badge purple mr-1 text-dark">Category 2</span>
              </a>
              <a href="">
                <span class="badge blue mr-1 text-dark">New</span>
              </a>
              <a href="">
                <span class="badge red mr-1 text-dark">Bestseller</span>
              </a>
            </div>

            <p class="lead">
              <span class="mr-1 text-dark">
                <del>$200</del>
              </span>
              <span class="text-dark">$100</span>
            </p>

            <p class="lead font-weight-bold text-dark">Description</p>

            <p class="text-dark">Lorem ipsum dolor sit amet consectetur adipisicing elit. Et dolor suscipit libero eos atque quia ipsa
              sint voluptatibus!
              Beatae sit assumenda asperiores iure at maxime atque repellendus maiores quia sapiente.</p>

            <form class="d-flex justify-content-left mt-12">
              <!-- Default input -->
              <button class="btn btn-primary btn-md my-5 p" type="submit">Add to cart
                <i class="fas fa-shopping-cart ml-1"></i>
              </button>

            </form>

          </div>
          <!--Content-->

        </div>
        <!--Grid column-->

      </div>
      <!--Grid row-->

      <hr>

      <!--Grid row-->
      <div class="row d-flex justify-content-center wow fadeIn">

        <!--Grid column-->
        <div class="col-md-6 text-center mb-3">

          <h4 class="my-4">More Products:</h4>
          <!--WILL UPDATE THIS FOR PROJECT DEMO. DAVID OR HOLLY CAN YOU CHECK OUT THE SCRIPT BELOW TO SEE IF THIS 
          MAKES SENSE? IT WAS NOT UPDATING, BUT THE ProductMenu.vue PAGE WAS? -->

          <div id="productTable" class="productTable text-dark bg-light">
            <ul>
                <li v-for="product in products" :key="product.id"> 
                {{ product.name + " | $" + product.price + " | " + product.description + " | " + product.category + " | " + product.status }}<button class="btn btn-primary" @click="update_product(id=product.id, name='', price=0.0, description='', category='', status='', delete_=true)">Delete</button>
                </li>
            </ul>
        </div>


        </div>
      </div>
    </div>
  </main>
  <!--Main layout-->

  <!--Footer-->
  <footer class="page-footer text-center font-small mt-4 wow fadeIn">

    <!--Copyright-->
    <div class="footer-copyright py-3">
      Product not final! CS360 Best Buy! 
      <a href="/" target="_blank">  </a>
    </div>
    <!--/.Copyright-->

  </footer>
  </body>
    


</template>

<script>
//Tracy TO-DO:
export default {
  name: 'Register',
  data() {
    return {
        show: false,
        users: [ { id: 0, firstName: "", lastName: "", email: "", password: ""}, ],
        currentUser: null,
    }
  },
  mounted: function() {
    this.read_users();
  },
  methods: {
    //USERS FUNCTIONS===========================================================
    load_user: function() {
      this.users.forEach( user => {
        if (user.id == this.$route.params.id) {
          this.currentUser = user;
        }
      })
    },
    read_users: function() {
      this.axios
        .get("http://localhost:5000/api/users")
        .then(response => {
          this.users = response.data;
          this.load_user();
        })
        .catch(error => { console.log(error.response) });
    },
    delete_user: function(id) {
      var data = {'delete': true, 'id': id };
      this.axios
        .post("http://localhost:5000/api/users", data)
        .then(response => (this.users = response.data))
        .catch(error => { console.log(error.response) });
    },
    //!USERS FUNCTIONS===========================================================
    //PRODUCT FUNCTIONS===========================================================
      //Taken from "ProductMenu.vue page"=====================
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
            .get("http://localhost:5000/api/products")
            .then(response => (this.products = response.data))
            .catch(error => { console.log(error.response) });
    },
    update_product: function( id = -1, name = "", price = 0.00, description = "", category= "", status = "", delete_ = false) 
    {
        var data = { id: id, name: name, price:price, description: description, category:category, status: status, delete: delete_ };
        this.axios
            .post("http://localhost:5000/api/products", data)
            .then(() => this.read_products())
            .catch(error => { console.log(error.response) });
        //   add a delay to make sure the backend respond
    },
    print: function(data){
        console.log(data)
    }
  }
    //!PRODUCT FUNCTIONS===========================================================
  }
};

</script>

<style>
.gradient-custom-HomePage {
  /* fallback for old browsers */
  background: #4F91FC;
  
  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(to right, #0660F3, #2458AD, #4F91FC, #7ebfef);
  
  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(to right, #0660F3, #2458AD, #4F91FC, #7ebfef);
  }
  
  @media (min-width: 768px) {
  .gradient-form {
  height: 100vh !important;
  }
  }
  @media (min-width: 769px) {
  .gradient-custom-HomePage {
  border-top-right-radius: .3rem;
  border-bottom-right-radius: .3rem;
  }
  }

  .productTable {
    background-color: white;
    margin: auto;
    margin-top: 50px;
    border: 6px solid #0AF;
    padding: 50px;
    text-align: center;
}
</style>
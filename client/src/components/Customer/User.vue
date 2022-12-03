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
    <header>
  <!-- Navbar -->
      <nav class="navbar navbar-expand-sm py-0 align-top navbar-dark bg-primary text-light border  border-5 border-dark rounded">
        <!-- Container wrapper -->
        <div class="container-fluid">
          <!-- Toggle button -->
          <button
            class="navbar-toggler"
            type="button"
            data-mdb-toggle="collapse"
            data-mdb-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <i class="fas fa-bars"></i>
          </button>

          <!-- Collapsible wrapper -->
        <div class="collapse navbar-collapse " id="navbarSupportedContent">
          <!-- Navbar brand -->
            <a class="navbar-brand d-inline-block align-top py-0" href="#">
            <img
              src="../Logo/logo_transparent.png"
              height="50"
              class="pr-3"
              alt="Best Buy! Logo"
              loading="lazy"
            />Welcome Customer!
          </a>            
            <!-- Left links -->
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" href="/Users"></a>
              </li>
            </ul>
            <!-- Left links -->
          </div>
          <!-- Collapsible wrapper -->

          <!-- Right elements -->
          <div class="d-flex align-items-center">
            <!-- Icon -->
            <a class="link-secondary me-3" href="#">
              <i class="fas fa-shopping-cart"></i>
            </a>

            <!-- Avatar -->
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle border border-dark mr-5" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                {{ currentUser.firstName }}
              </button>
              <div class="dropdown-menu bg-primary" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item bg-primary" href="#">Settings</a>
                <a class="dropdown-item bg-primary" href="#">Edit Profile</a>
                <a class="dropdown-item bg-primary" href="/">Logout!</a>
              </div>
            </div>
          </div>
          <!-- Right elements -->
        </div>
        <!-- Container wrapper -->
      </nav>
  <!-- Navbar -->

    </header>
      
        <!--BANNER SECTION-->
        <!--END BANNER SECTION-->
        <!--main body columns and rows-->

        <!--This area is the base for the many products that will show up, and as we add/ subtract items from the DB
        we will see it grow and shrink... doing test run with arrays at this time to make sure using base level scripts 
        in page... TJR 11/10/2022
      
        UPDATE 11/11/2022: redesign in process, linking products database to system, will have cards... looking for good ecommerse page layout
        as well =) DONT PANIC... and dont forget a towel!--> 

        <!--Main layout-->
  <main>
    <h3 class="text-left ml-5"> Featured Product:</h3>
    <div class="container-fluid dark-grey-text">

      <!--Grid row-->
      <div class="row wow fadeIn border bg-white">

        <!--Grid column-->
        <div class="col-md-6 mb-4">

          <img src="../Images/LG_OLED.jpg" class="img-fluid" alt="">

        </div>
        <!--Grid column-->

        <!--Grid column-->
        <div class="col-md-6 mb-4">

          <!--Content-->
          <div class="p-4">

            <div class="mb-3">
              <a href="">
                <h3 class=" text-dark font-weight-bolder">LG - 65" Class C2 Series OLED evo 4K UHD Smart webOS TV </h3>
              </a>
            </div>

            <p class="lead">
              <span class="text-dark font-weight-bolder"> $1699
              </span>
               <br>
               <br>
               <br>
              <span class="text-danger"> Dropped from: $2,099.99</span>
            </p>

            <form class="d-flex justify-content-left mt-12">
              <!-- Default input -->
              <button class="btn btn-primary btn-md my-5 p" type="submit">Bid NOW!
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
          <!--Working for david 11/28/2022 -->

          <!--
        <div id="productTable" class="productTable text-dark bg-light">
            <ul>
                <li v-for="product in products" :key="product.id"> 
                {{ product.name + " | $" + product.price + " | " + product.size + " | " + product.description + " | " + product.category + " | " + product.brand }}<button class="btn btn-primary">Bid</button>
                </li>
            </ul>
        </div>
        -->
        <section class="grid-cards">
        <div v-for="product in products" :key="product.id">
          <div class="card">
            <img
                src="https://imgur.com/SKZolYE.png"
              >
            <div class="d-flex flex-row justify-content-between mb-0 px-3">
              <small class="text-muted mt-1">PRODUCT NAME:</small>
              <h6> {{ product.name }} </h6>
            </div>
            <div class="d-flex flex-row justify-content-between mb-0 px-3">
              <small class="text-muted mt-1">PRODUCT BRAND:</small>
              <h6>{{ product.brand }}</h6>
            </div>
            <div class="d-flex flex-row justify-content-between mb-0 px-3">
              <small class="text-muted mt-1">PRICE:</small>
              <h6>&dollar; {{ product.price }}</h6>
            </div>
            <hr class="mt-2 mx-3" />
            <div class="d-flex flex-row justify-content-between px-3 pb-3">
              <div class="d-flex flex-column">
                <span class="text-muted">Description:</span>
                <small>{{ product.description }}</small>
              </div>
            </div>
            <div class="d-flex flex-row justify-content-between px-3 pb-3">
              <div class="d-flex flex-column">
                <span class="text-muted">Size Details:</span>
                <small>{{ product.size }} inch</small>
              </div>
            </div>
            <small class="text-muted key pl-3">{{ product.category }}</small>
            <div class="mx-3 mt-3 mb-2">
              <button
                type="button"
                class="btn btn-primary btn-block"
              >
                <small>BID</small>
              </button>
            </div>
          </div>
        </div>
        </section>

        </div>
      </div>
    </div>
  </main>
  <!--Main layout-->

  <!--Footer-->
  <footer class="page-footer text-center font-small mt-4 wow fadeIn">

    <!--Copyright-->
    <div class="footer-copyright py-3">
      Product not final! CS360 Best Buy! Holly Keir, David Bush, Tracy Rountree 2022 
      <a href="/" target="_blank">  </a>
    </div>
    <!--/.Copyright-->

  </footer>
  </body>
    


</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
        show: false,
        users: [ { id: 0, firstName: "", lastName: "", email: "", password: ""}, ],
        products: [ { id: 0, name: "", price: 0.00, size: 0.00, description: "", category: "", brand: ""}, ],
        currentUser: null,
    }
  },
  mounted: function() {
    this.read_users();
    this.read_products();
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
    read_products: function() {
      this.axios
        .get("http://localhost:5000/api/products")
        .then(response => (this.products = response.data))
        .catch(error => { console.log(error.response) });
    },
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
.card {
  box-shadow: 0 6px 10px 0 rgba(0, 0, 0, 0.2);
  padding: 16px;
  text-align: center;
  background-color: #f1f1f1;
}

/* Remove extra left and right margins, due to padding */
.row {margin: 0 -5px;}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}


.card::after {
  position: absolute;
  z-index: -1;
  opacity: 0;
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.card:hover {
  transform: scale(1.02, 1.02);
  -webkit-transform: scale(1.02, 1.02);
  backface-visibility: hidden;
  will-change: transform;
  box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.75) !important;
}

h3, p {
  color: black !important;
}

.card:hover::after {
  opacity: 1;
}

.card:hover .btn-outline-primary {
  color: white;
  background: #007bff;
}

.px-2 {
  padding-left: ($spacer * 0.45) !important;
  padding-right: ($spacer * 0.45) !important;
}


/* Cards */
.grid-cards {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  column-gap: 24px;
  row-gap: 36px;
  margin: 36px 36px;

}

.card p {
  color: black;
}
</style>
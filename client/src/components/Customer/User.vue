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
            />Welcome Shopper!
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
            <span id="boot-icon" class="bi bi-cart" style="font-size: 50px; color: rgb(0, 0, 0); opacity: 1; -webkit-text-stroke-width: 0px;"></span>
            <!-- Avatar -->
            <div class="btn-group dropleft">
              <button class="btn btn-secondary dropdown-toggle border border-dark mr-2 font-weight-bolder" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                {{ currentUser.firstName }}
              </button>
              <div class="dropdown-menu bg-primary border border-dark text-justified" aria-labelledby="dropdownMenuButton">
                <a type="button" class="dropdown-item bg-primary"  data-toggle="modal" data-target="#SearchModal">User Settings</a>
                <a type="button" class="dropdown-item bg-primary"  data-toggle="modal" data-target="#BidModal">View Bids!</a>
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

        <!--Main layout-->
  <main>
    <h3 class="text-left ml-5 text-light font-weight-bolder"> Featured Products:</h3>
    <!--
    <div class="container-fluid dark-grey-text">

      <div class="row wow fadeIn border bg-white">

        <div class="col-md-6 mb-4">

          <img src="../Images/LG_OLED.jpg" class="img-fluid my-4" alt="">

        </div>

        <div class="col-md-6 my-4 bg-light border border-dark">

          <div class="p-4">

            <div class="mb-3">
              <a href="">
                <h3 class=" text-dark font-weight-bolder">LG - 65" Class C2 Series OLED evo 4K UHD Smart webOS TV </h3>
              </a>
            </div>
            <div class="container ml-4">
              <p class="lead">
                <div class="container">
                  <span class="text-dark font-weight-bolder">Currently:</span>
                    <span class="text-success font-weight-bold my-2">  $1699</span>
                </div>
                <br>
                <div class="container">
                  <span class="text-dark font-weight-bolder">Was:</span>
                    <span class="text-danger font-weight-bold my-2">  $2,099.99</span>
                </div>
              </p>
              <form class="d-flex justify-content-left mt-12">
                <button class="btn btn-primary btn-md my-5 font-weight-bolder" href="#" type="submit">Bid NOW!
                  <i class="fas fa-shopping-cart ml-1"></i>
                </button>

              </form>
            </div>
              

            

          </div>

        </div>

      </div>
      -->
      <hr>
      <!-- ***Just added this for now should be updated -->
      <div class="container">
        <button type="button" class="btn btn-primary btn-block" @click="match_product(currentUser.id)">
          <h5>MATCH</h5>
        </button>
      </div>
      <!-- Here are the MATCHED Products -->
      <section v-if="matched" class="grid-cards">
        <div v-for="(product, index) in matchedProducts" :key="product.id">
            <div class="card">
              <img 
                :src="require(`../../components/product_photos/product${productTypes[product.category]}.jpg`)"
              >
            <div class="d-flex flex-row justify-content-between mb-0 px-3">
              <h4 v-if="index==0" class="text-muted mt-1">Exact Match</h4>
              <h4 v-if="index==1" class="text-muted mt-1">Best Match</h4>
              <h4 v-if="index==2" class="text-muted mt-1">Lowest Match</h4>
            </div>
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
              <button type="button" class="btn btn-primary btn-block" @click="create_bid(product.id)">
                <small>BID</small>
              </button>
            </div>
          </div>
        </div>
      </section>
      <!--Grid row-->
      <div class="row d-flex justify-content-left wow fadeIn">

        <!--Grid column-->
        <div class="col-md-6 text-left ml-5 mb-3">

          <h4 class="my-4 font-weight-bolder">More Products:</h4>

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
        <div v-for="(product, index) in paginated" :key="product.id">
            <div class="card">
              <img 
                :src="require(`../../components/product_photos/product${productTypes[product.category]}.jpg`)"
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
              <button type="button" class="btn btn-primary btn-block" @click="create_bid(product.id)">
                <small>BID</small>
              </button>
            </div>
          </div>
        </div>
        <!-- ***Just added this for now should be updated -->
        <ul class="pagination-list">
          <li>
            <a @click="prev()"> Prev </a>
          </li>
          <li>
            <span
              class="pagination-link go-to has-text-orange"
              aria-label="Goto page 1"
              >{{ currentPage }}</span
            >
          </li>
          <li>
            <a @click="next()"> Next </a>
          </li>
        </ul>
      </section>
        <!-- BID Modal -->
        <div class="modal fade gradient-custom-HomePage border border-dark" id="BidModal" tabindex="-1" role="dialog" aria-labelledby="BidModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-lg border border-dark" role="document">
            <div class="modal-content">
              <div class="modal-header bg-primary text-light">
                <h5 class="modal-title" id="exampleModalLabel">Current Bids!</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body text-center">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">BID ID:</th>
                      <th scope="col">Product Name</th>
                      <th scope="col">Product Type</th>
                      <th scope="col">Current Bid amount</th>
                      <th scope="col">Change Bid Amt</th>
                      <th scope="col">Accept Bid</th>
                      <th scope="col">Decline Bid</th>
                    </tr>
                  </thead>
                  <tbody>
                     <!-- <tr>
                        <th scope="row"> Test id </th>
                        <td>Test </td>
                        <td>Test</td>
                        <td>Test</td>
                        <td><input type="NewBid" class="form-control" id="exampleInputNewBid" aria-describedby="bidHelp" placeholder="$$"></td>
                        <td><button class="btn btn-danger">Delete Bid</button></td>
                      </tr> -->
                    <tr v-for="offer in offers" :key="offer.id">
                        <th scope="row">{{ offer.id }}</th>
                        <td>{{ offer.product.name }}</td>
                        <td>{{ offer.product.category }}</td>
                        <td>{{ offer.product.price }}</td>
                        <td><input type="NewBid" class="form-control" id="exampleInputNewBid" aria-describedby="bidHelp" placeholder="$$"></td>
                        <td><button class="btn btn-success" @click="accept_bid(offer.id)" data-dismiss="modal">Accept Bid</button></td>
                        <td><button class="btn btn-danger" @click="remove_bid(offer.id)" data-dismiss="modal">Decline Bid</button></td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="modal-footer bg-primary">
                <button type="button" class="btn btn-secondary border border-dark" data-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        <!---END BID MODAL-->
        <!-- SETTTINGS Modal -->
        <div class="modal fade gradient-custom-HomePage border border-dark" id="SearchModal" tabindex="-1" role="dialog" aria-labelledby="SearchModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content rounded-5">
              <div class="modal-header bg-primary text-light">
                <h5 class="modal-title" id="exampleModalLabel">{{ currentUser.firstName }}'s Settings</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-header font-weight-bolder">
                <h3>User Settings:</h3>
              </div>
              <div class="modal-body">
                  This is where the User Settings will go!
              </div>
              <div class="modal-header font-weight-bolder">
                <h3>Shopping Experience Settings:</h3>
              </div>
              <div class="modal-body">
                <div class="form-group align-content-center">
                  <label class="text-dark" for="inputState">Product Category</label>
                  <select id="inputState" class="form-control border border-dark" v-model="category">
                    <option selected>Choose...</option>
                    <option>Electronics</option>
                    <option>TV & Video</option>
                    <option>Home Audio & Theater</option>
                    <option>Portable Audio</option>
                    <option>Computers</option>
                    <option>Tablets</option>
                    <option>Cell Phones</option>
                    <option>Wearable Technology</option>
                    <option>Cameras, Camcorders, & Drones</option>
                    <option>Video Games</option>
                    <option>Auto Electronics</option>
                  </select>
                </div>
                <div class="form-group align-content-center">
                  <!-- <h4 class="text-dark">Low Price:</h4> -->
                  <!-- <input class="form-control form-control-sm border border-dark" type="text" placeholder="$" aria-label="$"></input> -->
                  <h4 class="text-dark">High Price:</h4>
                  <input class="form-control form-control-sm border border-dark" type="number" placeholder="$$$$$$$" aria-label="$$$$$$$" v-model="price"></input>
                  <h4 class="text-dark">Description:</h4>
                  <input class="form-control form-control-sm border border-dark" type="text" placeholder="Desctption of product you are looking for:" aria-label="Desctption of product you are looking for:" v-model="description"></input>
                  <h4 class="text-dark">Brand:</h4>
                  <input class="form-control form-control-sm border border-dark" type="text" placeholder="LG/VIZIO/PANASNIC/SONY/etc..." aria-label="LG/VIZIO/PANASNIC/SONY/etc..." v-model="brand"></input>
                  <h4 class="text-dark">Size Dimensions:</h4>
                  <input class="form-control form-control-sm border border-dark" type="number" placeholder="32 in./60 in./72 in." aria-label="32 in./60 in./72 in." v-model="size"></input>
                </div>
              </div>
              
              <div class="modal-footer bg-primary">
                <button type="button" class="btn btn-secondary border border-dark" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-success border border-dark" href="UserSearch" @click="update_user(currentUser.id)">Save Settings</button>
              </div>
            </div>
          </div>
        </div>
        <!---END SEARCH MODAL-->
        </div>
      </div>
    </div>
  </main>
  <!--Main layout-->

  <!--Footer-->
  <footer class="page-footer text-center font-small mt-4 wow fadeIn">

    <!--Copyright-->
    <div class="footer-copyright py-3 text-light">
        CS360 Best Buy! Holly Keir, David Bush, Tracy Rountree 2022 
      <a href="/" target="_blank">  </a>
    </div>
    <!--/.Copyright-->

  </footer>
  </body>
</template>

<script>
export default {
  name: 'Register',
  computed: {
    indexStart() {
      return (this.currentPage - 1) * this.pageSize;
    },
    indexEnd() {
      return this.indexStart + this.pageSize;
    },
    paginated() {
      return this.products.slice(this.indexStart, this.indexEnd);
    },
  },
  data() {
    return {
        show: false,
        currentUser: null,
        matched: false,
        users: [ { id: 0, firstName: "", lastName: "", email: "", password: ""}, ],
        products: [ { id: 0, name: "", price: 0.00, size: 0.00, description: "", category: "", brand: ""}, ],
        productTypes: {'Electronics': 0, 'TV & Video': 1, 'Home Audio & Theater': 2, 'Portable Audio': 3, 'Computers': 4, 'Tablets': 5, 'Cell Phones': 6, 'Wearable Technology': 7, 'Cameras, Camcorders, & Drones': 8, 'Video Games': 9, 'Auto Electronics': 10},
        matchedProducts: null,
        offers: [ { id: 2, penalty: 0.0, product: null, user: null, userAccept: false, vendorAccept: false, vendor: null},],
        pageSize: 21,
        currentPage: 1,
        category: false,
        brand: false,
        description: false,
        size: false,
        price: false,
      }
  },
  mounted: async function() {
    this.read_users();
    await this.sleep(1000); // add small delay
    this.read_products();
    await this.sleep(1000); // add small delay
    this.read_offers();
  },
  methods: {
    prev: function() {
      this.currentPage--;
    },
    next: function() {
      this.currentPage++;
    },
    sleep: function (ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
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
    update_user: function(id) {
      var options = {category: this.category , price: this.price, description: this.description, brand: this.brand, size: this.size};
      var data = { id: id, options: options };
      this.axios
        .post("http://localhost:5000/api/users", data)
        .then(response => (status = response.data))
        .catch(error => { console.log(error.response) });
    },
    delete_user: function(id) {
      var data = {'delete': true, 'id': id };
      this.axios
        .post("http://localhost:5000/api/users", data)
        .then(response => (status = response.data))
        .catch(error => { console.log(error.response) });
    },
    //save_user_settings: function(){

    //}
    //!USERS FUNCTIONS===========================================================
    
    //PRODUCT FUNCTIONS===========================================================
    read_products: function() {
      this.axios
        .get("http://localhost:5000/api/products")
        .then(response => (this.products = response.data))
        .catch(error => { console.log(error.response) });
    },
    find_product: function(id) {
      var product = null;
      this.axios
        .get(`http://localhost:5000/api/products?productId=${id}`)
        .then(response => (product = response.data))
        .catch(error => { console.log(error.response) });
      return product
    },
    match_product: async function(userId) {
      var data = { id: userId };
      this.axios
        .post(`http://localhost:5000/api/match`, data)
        .then(response => {
          this.matchedProducts = response.data;
          })
        .catch(error => { console.log(error.response) });
        await this.sleep(4000); // add small delay
        this.matched = true;
    },
    //!PRODUCT FUNCTIONS===========================================================

  //BIDDING FUNCTIONS================================================================
    toggle: function() {
      this.acceptDecline = !this.acceptDecline;
    },
    load_offers: function() {
      var currOffers = [];
      this.offers.forEach( offer => {
        if (offer.user.id == this.currentUser.id) {
          currOffers.push(offer);
        }
      })
      this.offers = currOffers;
    },
    read_offers: function() {
      this.axios
        .get("http://localhost:5000/api/offers")
        .then(response => {
          this.offers = response.data;
          this.load_offers();
        })
        .catch(error => { console.log(error.response) });
    },
    create_bid: function(productId) {
      var data = { userId: this.currentUser.id, productId: productId, userAccept: true };
      this.axios
        .post("http://localhost:5000/api/offers", data)
        .then(response => (status  = response.data))
        .catch(error => { console.log(error.response) });
    },
    remove_bid: function(offerId) {
      var data = { id: offerId, delete: true }
      this.axios
        .post("http://localhost:5000/api/offers", data)
        .then(response => (status  = response.data))
        .catch(error => { console.log(error.response) });
    },
    //DAVID HALLLPPPP=============================
    accept_bid: function(offerId){
      var data = { id: offerId, delete: false }
      this.axios
        .post("http://localhost:5000/api/offers", data)
        .then(response => (status  = response.data))
        .catch(error => { console.log(error.response) });
    }
  },
    //!BIDDING FUNCTIONS================================================================
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
<template>
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
                  src="../components/Logo/logo_transparent.png"
                  height="50"
                  class="pr-3"
                  alt="Best Buy! Logo"
                  loading="lazy"
                />
              </a> 
              <ul class="navbar-nav">
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      Vendor
                  </a>
                  <div class="dropdown-menu bg-primary" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item text-justify" href="/">Home </a>
                    <a class="dropdown-item text-justify" href="VendorOffers">Offers </a>
                    <a class="dropdown-item text-justify" href="vendor">Vendors </a>
                  </div>
                </li>
              </ul>           
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
                  {{ currentVendor.firstName }}
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
  <!-- Navbar -->
      
    <!--END OF NAVIGATION BAR-->

    <!--BANNER SECTION-->
    <!--END BANNER SECTION-->

    <!--Featured product section-->
    <div class="container_page rounded-5">
      <div class="row">
        <div class="col-7 text-center mx-auto container-fluid">
          <div class="row bg-primary text-lg-center font-weight-bolder">
            <h2_User>Welcome {{ currentVendor.firstName }} ! </h2_User>
          </div>
        </div>
      </div>
    </div>
    <br>
  <!-- END OF VENDOR HEADER-->
  

<!-- <div class="row">
  <div class="column">
    <div class="card">
      <h3>Card 1</h3>
      <p>Some text</p>
      <p>Some text</p>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <h3>Card 2</h3>
      <p>Some text</p>
      <p>Some text</p>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
      <h3>Card 3</h3>
      <p>Some text</p>
      <p>Some text</p>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
      <h3>Card 4</h3>
      <p>Some text</p>
      <p>Some text</p>
    </div>
  </div>
</div>

<div class="row">
  <div class="column">
    <div class="card">
      <h3>Card 1</h3>
      <p>Some text</p>
      <p>Some text</p>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <h3>Card 2</h3>
      <p>Some text</p>
      <p>Some text</p>
    </div>
  </div>
</div> -->

<section class="grid-cards">
  <!--
  <div class="card">
    <img
        src="https://imgur.com/SKZolYE.png"
      >
    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRODUCT NAME:</small>
      <h6> product.name </h6>
    </div>
    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRODUCT BRAND:</small>
      <h6>Apple</h6>
    </div>
    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRICE:</small>
      <h6>&dollar;869</h6>
    </div>
    <hr class="mt-2 mx-3" />
    <div class="d-flex flex-row justify-content-between px-3 pb-3">
      <div class="d-flex flex-column">
        <span class="text-muted">Description:</span>
        <small>This is the description of the product being offered</small>
      </div>
    </div>
    <div class="d-flex flex-row justify-content-between px-3 pb-3">
      <div class="d-flex flex-column">
        <span class="text-muted">Size Details:</span>
        <small>75 inch</small>
      </div>
    </div>
    <small class="text-muted key pl-3">Cell Phones category</small>
    <div class="mx-3 mt-3 mb-2">
      <button
        type="button"
        class="btn btn-primary btn-block"
      >
        <small>EDIT</small>
      </button>
    </div>
  </div>

  
  <div id="productTable" class="productTable text-dark bg-light">
    <ul>
      <li v-for="product in products" :key="product.id"> 
        {{ product.name + " | $" + product.price + " | " + product.size + " | " + product.description + " | " + product.category + " | " + product.brand }}
      </li>
    </ul>
  </div> 
    

  <div class="card">
    <img
        src="https://imgur.com/SKZolYE.png"
      >
    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRODUCT NAME:</small>
        <li v-for="product in products" :key="product.id"> 
          {{ product.name}}
          <h6> hi </h6>
          {{ product.id }}
        </li>            
    </div>


    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRODUCT BRAND:</small>
      <h6> apple </h6>
    </div>
    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRICE:</small>
      <h6>&dollar;869</h6>
    </div>
    <hr class="mt-2 mx-3" />
    <div class="d-flex flex-row justify-content-between px-3 pb-3">
      <div class="d-flex flex-column">
        <span class="text-muted">Description:</span>
        <small>This is the description of the product being offered</small>
      </div>
    </div>
    <div class="d-flex flex-row justify-content-between px-3 pb-3">
      <div class="d-flex flex-column">
        <span class="text-muted">Size Details:</span>
        <small>75 inch</small>
      </div>
    </div>
    <small class="text-muted key pl-3">Cell Phones category</small>
    <div class="mx-3 mt-3 mb-2">
      <button
        type="button"
        class="btn btn-primary btn-block"
      >
        <small>EDIT</small>
      </button>
    </div>
  </div>

  <div class="card">
    <img
        src="https://imgur.com/SKZolYE.png"
      >
    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRODUCT NAME:</small>
      <h6>iPhone 10</h6>
    </div>
    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRODUCT BRAND:</small>
      <h6>Apple</h6>
    </div>
    <div class="d-flex flex-row justify-content-between mb-0 px-3">
      <small class="text-muted mt-1">PRICE:</small>
      <h6>&dollar;869</h6>
    </div>
    <hr class="mt-2 mx-3" />
    <div class="d-flex flex-row justify-content-between px-3 pb-3">
      <div class="d-flex flex-column">
        <span class="text-muted">Description:</span>
        <small>This is the description of the product being offered</small>
      </div>
    </div>
    <div class="d-flex flex-row justify-content-between px-3 pb-3">
      <div class="d-flex flex-column">
        <span class="text-muted">Size Details:</span>
        <small>75 inch</small>
      </div>
    </div>
    <small class="text-muted key pl-3">Cell Phones category</small>
    <div class="mx-3 mt-3 mb-2">
      <button
        type="button"
        class="btn btn-primary btn-block"
      >
        <small>EDIT</small>
      </button>
    </div>
  </div>
  -->
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
          <small>EDIT</small>
        </button>
      </div>
    </div>
  </div>


</section>

    <div class="container_page rounded-5">
      <form>
        <h1><center>Product Regristration Form</center></h1>
        <div class="container_page rounded-5">
          <div class="row">
            <div class="col-7 text-center mx-auto container-fluid">
              <label for="inputAddress">Description</label>
              <input
                type="text"
                class="form-control"
                id="inputAddress"
                v-model="description"
                placeholder="Two packet-switched network connector"
              />

              <div class="form-row">
                <div class="form-group col-md-4">
                  <label for="inputAddress2">Name</label>
                  <input
                    type="text"
                    class="form-control"
                    id="inputAddress2"
                    v-model="name"
                    placeholder="NETGEAR"
                  />
                </div>
                <div class="form-group col-md-4">
                  <label for="inputAddress2">Product Brand</label>
                  <input
                    type="text"
                    class="form-control"
                    id="inputAddress2"
                    v-model="productBrand"
                    placeholder="NETGEAR"
                  />
                </div>
                <div class="form-group col-md-4">
                  <label for="inputAddress2">Size</label>
                  <input
                    type="text"
                    class="form-control"
                    id="inputAddress2"
                    v-model="size"
                    placeholder="75"
                  />
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputAddress2">Price</label>
                  <input
                    type="text"
                    class="form-control"
                    id="inputAddress2"
                    v-model="price"
                    placeholder="75.00"
                  />
                </div>

                <div class="form-group col-md-6">
                  <label for="inputState">Product Category</label>
                  <select id="inputState" class="form-control" v-model="category">
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
                <!--
                <div class="form-row">
                  <div>
                    <input
                      type="file"
                      id="myFile"
                      name="filename"
                      style="display: none"
                    />
                    <label for="myFile">Upload an Image</label>
                  </div>
                </div>
                -->
              </div>

              <button type="submit" class="btn btn-primary" @click="product_upload(id=-1, name=name, price=price, size=size, description=description, category=category, brand=productBrand, delete_=false)">
                Enter Product
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  </body>
</template>

<script>
export default 
{
  name: "Products",
  data() 
  {
    return {
      currentVendor: null, // Keep track of the logged in Vendor
      vendors: [ { id: 0, firstName: "", lastName: "", email: "", password: ""}, ],
      productNumber: {},
      products: [
        { id: 0, vendorId: 0, name: "", price: 0.00, size: 0.00, description: "", category: "", brand: ""},
      ],
      name: "",
      description: "",
      productBrand: "",
      size: "",
      price: "",
      category: "",
    };
  },
  mounted: function() {
    this.read_vendors();
    this.read_products();

  },
  methods: 
  {
    load_vendor: function() {
      this.vendors.forEach( vendor => {
        if (vendor.id == this.$route.params.id) {
          this.currentVendor = vendor;
        }
      })
    },
    read_vendors: function() {
      this.axios
        .get("http://localhost:5000/api/vendors")
        .then(response => {
          this.vendors = response.data;
          this.load_vendor();
        })
        .catch(error => { console.log(error.response) });
    },
    sleep: function (ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
    
    product_upload: async function (id = -1, name = "", price = 0.00, size = 0.00, description = "", category= "", brand = "", delete_ = false) {
      var data = {
        vendorId: this.currentVendor.id,
        name: name,
        description: description,
        brand: brand,
        size: size,
        price: price,
        category: category,
      };
      
      console.log(data);
      this.axios
        .post("http://localhost:5000/api/products", data)
        .then((response) => (this.productNumber = response.data))
        .catch((error) => {
          console.log(error.response);
        });
    },
    read_products: function() {
      this.axios
        .get("http://localhost:5000/api/products")
        .then(response => (this.products = response.data))
        .catch(error => { console.log(error.response) });
    },
  },
};
</script>

<style>
.card {
  box-shadow: 0 6px 10px 0 rgba(0, 0, 0, 0.2);
  padding: 16px;
  text-align: center;
  background-color: #f1f1f1;
}

@media screen and (max-width: 800px) {
  .column {
    width: 100%;
    display: block;
    margin-bottom: 30px;
  }
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
</style>
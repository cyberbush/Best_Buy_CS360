<template>
  <body class="bg-dark">
    <!--Upper Nav-Bar-->
    <div class="bg-dark">
      <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-primary">
        <a class="navbar-brand" href="/"> Best Buy! </a>
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="navbarDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Menu
            </a>
            <div
              class="dropdown-menu bg-primary"
              aria-labelledby="navbarDropdown"
            >
              <a class="dropdown-item text-justify" href="/">Home </a>
              <a class="dropdown-item text-justify" href="ProductDisplay"
                >Product Display
              </a>
              <a class="dropdown-item text-justify" href="vendor">Vendors </a>
              <a class="dropdown-item text-justify" href="about">About </a>
              <a class="dropdown-item text-justify" href="help">Help </a>
            </div>
          </li>
        </ul>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <form class="form-inline mx-auto my-2">
            <input
              class="form-control mr-sm-1"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button class="btn btn-dark my-2 my-sm-0" type="submit">
              Search
            </button>
          </form>
        </div>
        <p class="">Logged in Peoples!</p>
      </nav>
    </div>
    <!--END OF NAVIGATION BAR-->

    <!--BANNER SECTION-->
    <div class="Banner_Container">
      <img
        src="../components/Images/logo.png"
        class=""
        height="150px"
        width="100%"
        alt="Matrix picture Banner"
      />
    </div>
    <!--END BANNER SECTION-->

    <!--Featured product section-->
    <div class="container_page rounded-5">
      <div class="row">
        <div class="col-7 text-center mx-auto container-fluid">
          <div class="row bg-primary text-lg-center font-weight-bolder">
            <h2_User>Welcome ____(Vendor Name)____! </h2_User>
            <img
              src="../components/Logo/Vendor_Logo.png"
              class=""
              height="100px"
              alt="Spectrum Logo"
            />
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

  <div class="card">
  <h3>Card 2</h3>
  <p>Some text</p>
  <p>Some text</p>
  </div>

  <div class="card">
  <h3>Card 2</h3>
  <p>Some text</p>
  <p>Some text</p>
  </div>

  <div class="card">
  <h3>Card 2</h3>
  <p>Some text</p>
  <p>Some text</p>
  </div>

  <div class="card">
  <h3>Card 2</h3>
  <p>Some text </p>
  <p>Some text</p>
  </div>

  <div class="card">
  <h3>Card 2</h3>
  <p>Some text</p>
  <p>Some text</p>
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
                    placeholder="75 inches"
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
                    placeholder="75 inches"
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
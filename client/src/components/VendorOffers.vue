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
                    <a class="dropdown-item text-justify" href="/VendorOffers">Offers </a>
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
                  Vendor
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
    <!--END OF NAVIGATION BAR-->

    <!--BANNER SECTION-->
    <!--END BANNER SECTION-->

    <!--Featured product section-->
        <div class="container_page rounded-5">
            <div class="row">
                <div class="col-7 text-center mx-auto container-fluid">
                    <div class="row bg-primary text-lg-center font-weight-bolder">
                        <h2_User>Welcome ____(Vendor Name)____!  </h2_User>
                        <img src="../components/Logo/Vendor_Logo.png" class="" height="100px" alt="Spectrum Logo">
                    </div>
                </div>
            </div>
        </div>
<br>

<div class="container_page rounded-5">
  <div class="col-7 text-center mx-auto container-fluid">
    <div class="row bg-primary text-lg-center font-weight-bolder">
      <h2_User> Offers </h2_User>
    </div>
  </div>
</div>

  <div v-for="offer in offers" :key="offer.id">
    <div class="card2" >
      
        <h4 style="color:black; text-align: left; line-height: 2px;" > From: <small> {{offer.firstName + " " + offer.lastName}} </small> </h4>
        <h4 style="color:black; text-align: left; line-height: 2px;"> Product: <small> {{products.name + "(" + offer.productId + ")"}} </small> </h4>
        <h4 style="color:black; text-align: left; line-height: 2px;"> Price: <small> {{"$" + products.price}} </small> </h4>
        <h4 style="color:black; text-align: left; line-height: 2px;"> Penalty: <small> {{"$" + offer.penalty}} </small> </h4>
        <div class="ui buttons big">
          <button
            class="btn btn-success"
            @click="accept_offers(offer.id)" 
            :class="[acceptDecline ? 'active' : '']">Accept</button>
          <button
            class="btn btn-danger"
            @click="remove_offers(offer.id)"
            :class="[!acceptDecline ? 'active' : '']">Decline</button>
        </div>
    </div>
</div>


    </body>
</template>

<script>
export default {
  data() {
    return {
      // acceptDecline: true,
      show: false,
      currentUser: null,
      users: [ { id: 0, firstName: "", lastName: "", email: "", password: ""}, ],
      offers: [ { id: 2, penalty: 0.0, product: null, user: null, userAccept: false, vendorAccept: false, vendor: null},],
      products: [ { id: 0, name: "", price: 0.00, size: 0.00, description: "", category: "", brand: ""}, ],

    

    };
  },
  mounted: function() {
    this.read_offers();
  },
  methods: {
    toggle() {
      this.acceptDecline = !this.acceptDecline;
    },
    
    read_offers: function() {
      this.axios
        .get("http://localhost:5000/api/offers")
        .then(response => (this.offers = response.data))
        .catch(error => { console.log(error.response) });
    },
    remove_offers: function(id) {
      var data = { id: id, delete: true }
      this.axios
        .post("http://localhost:5000/api/offers", data)
        .then(response => (status  = response.data))
        .catch(error => { console.log(error.response) });
    },
    accept_offers: function(id){
      var data = {id: id, vendorAccept: true}
      this.axios 
        .post("http://localhost:5000/api/offers", data)
        .then(response => (status  = response.data))
        .catch(error => { console.log(error.response) });
    }
  },
};



</script>

<style>
    .card2 {
      box-shadow: 0 6px 10px 0 rgba(0, 0, 0, 0.2);
      background-color: #f1f1f1;
      border:none;
      text-align: center;
      padding: 20px, 20px;
      padding-top: 30px;
      width: 860px;
      height: 270px;
      margin: 10px auto;
    }

    .card2::after {
      position: absolute;
      z-index: -1;
      opacity: 0;
      -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
      transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
    }

    .card2:hover {


      transform: scale(1.02, 1.02);
      -webkit-transform: scale(1.02, 1.02);
      backface-visibility: hidden; 
      will-change: transform;
      box-shadow: 0 1rem 3rem rgba(0,0,0,.75) !important;
    }

    .card2:hover::after {
      opacity: 1;
    }

    .card2:hover .btn-outline-primary{
      color:white;
      background:#007bff;
    }

    .px-2 {
      padding-left: ($spacer * .45) !important;
      padding-right: ($spacer * .45) !important;
    }

    .collapsible {
      background-color: #777;
      color: white;
      cursor: pointer;
      padding: 18px;
      width: 100%;
      border: none;
      text-align: left;
      outline: none;
      font-size: 15px;
    }

    .active, .collapsible:hover {
      background-color: #555;
    }

    .content {
      adding: 0 18px;
      display: none;
      overflow: hidden;
      background-color: #f1f1f1;
    }   

    #myDIV {
      width: 500px;
      height: 500px;
      background-color: lightblue;
    }

    .grid {
  display: grid;
  grid-template-columns: 1fr;
  column-gap: 24px;
  row-gap: 24px;
  margin: 36px 36px;

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
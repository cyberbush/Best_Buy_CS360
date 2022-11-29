<template>
    <body class="bg-dark">
    <!--Upper Nav-Bar-->
    <div class="bg-dark">
        <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-primary ">
        <a class="navbar-brand" href="/"> Best Buy!</a>
            <ul class="navbar-nav">
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Menu
                </a>
                <div class="dropdown-menu bg-primary" aria-labelledby="navbarDropdown">
                  <a class="dropdown-item text-justify" href="/">Home </a>
                  <a class="dropdown-item text-justify" href="ProductDisplay">Product Display </a>
                  <a class="dropdown-item text-justify" href="vendor">Vendors </a>
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
            <p class="">Logged in Peoples!</p>
        </nav>
    </div>
    <!--END OF NAVIGATION BAR-->

    <!--BANNER SECTION-->
    <div class="Banner_Container">
        <img src="../components/Images/logo.png" class="" height="150px" width="100%" alt="Matrix picture Banner">
    </div>
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

  <div v-for="offer in offers" :key="offer.id">
    <div class="card2" >
      
        <h2 style="color:black; line-height: 20px;" > Offer: From {{offer.vendorId}} </h2>
        <h4 style="color:black; text-align: left; line-height: 2px;"> Penalty: <small> {{"$" + offer.penalty}} </small> </h4>
        <h4 style="color:black; text-align: left; line-height: 2px;"> Product ID: <small> {{offer.productId}} </small> </h4>
        <div class="ui buttons big">
          <button
            class="btn btn-success"
            @click="toggle"
            :class="[acceptDecline ? 'active' : '']">Accept</button>
          <button
            class="btn btn-danger"
            @click="toggle"
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
      offers: [ { id: 2, penalty: 0.0, productId: 1, userId: 1, userAccept: false, vendorAccept: false, vendorId: 1}, ],
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
      height: 250px;
      margin: 0 auto;
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

</style>
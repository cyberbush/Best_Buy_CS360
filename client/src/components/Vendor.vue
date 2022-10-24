<template>
    <body class="bg-dark">
      <!--Upper Nav-Bar-->
      <div class="bg-dark">
          <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-primary ">
            <a class="navbar-brand" href="/"> Best Buy!
            </a>
            <ul class="navbar-nav">
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Menu
                </a>
                <div class="dropdown-menu bg-primary" aria-labelledby="navbarDropdown">
                  <a class="dropdown-item text-justify" href="/">Home</a>
                  <a class="dropdown-item text-justify" href="user">Customers</a>
                  <a class="dropdown-item text-justify" href="vendor">Vendors</a>
                  <a class="dropdown-item text-justify" href="Product">Products</a>
                  <a class="dropdown-item text-justify" href="Services">Services</a>
                  <a class="dropdown-item text-justify" href="All_In_One">All-In-One Packages</a>
                  <a class="dropdown-item text-justify" href="Wishlist">Wishlist</a>
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
        <div class="container_page rounded-5">
          <div class="row">
            <div class="col-7 text-center mx-auto container-fluid">
              <div class="row bg-primary text-lg-center font-weight-bolder">
                <h2_User> Products: </h2_User>
              </div>
                <div class="row"> 
                <div class="col-7 text-center mx-auto container-fluid">
                <div class="row bg-primary text-lg-center font-weight-bolder">
                  <div class="card mb-3" style="max-width: 540px;">
                    <div class="row g-0">
                    <div class="col-md-2">
                      <br>
                      <i style='font-size:24px' class='fas'>&#xf109;</i>
                    </div>
                      <div class="col-md-6">
                          <br>
                          <h5 class="card-title">Package 1</h5>
                          <p class="card-text"><small class="text-muted">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</small></p>
                          <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                        
                      </div>
                      <div class="col-md-4">
                          <br>
                          <h5 class="card-title">Package 1</h5>
                          <p class="card-text"><small class="text-muted">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</small></p>
                          <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                        
                      </div>
                    </div>
                  </div>
                </div>
                </div> </div>
            </div>
          </div>
        </div>

    </body>
</template>

<script>

</script>
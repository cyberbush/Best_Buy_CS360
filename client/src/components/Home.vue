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
                      Home
                  </a>
                  <div class="dropdown-menu bg-primary" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item text-justify" href="/">Home</a>
                    <a class="dropdown-item text-justify" href="user">Customers</a>
                    <a class="dropdown-item text-justify" href="vendor">Vendors</a>
                    <a class="dropdown-item text-justify" href="Product">Products</a>
                    <!-- <a class="dropdown-item text-justify" href="Services">Services</a> -->
                    <!-- <a class="dropdown-item text-justify" href="All_In_One">All-In-One Packages</a> -->
                    <!-- <a class="dropdown-item text-justify" href="Wishlist">Wishlist</a> -->
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
          <!--BANNER SECTION-->
          <div class="Banner_Container">
            <img src="../components/Images/logo.png" class="" height="150px" width="100%" alt="Matrix picture Banner">
          </div>
          <!--END BANNER SECTION-->
          <!--main body columns and rows-->
            <div id="home">
                <h1>Home Page</h1>
                <a href="/Product_Menu"><u>Go to Product Menu Example</u></a>
                <a href="/vendor"><u>Go to Vendor</u></a>
                <a href="/user"><u>Go to User</u></a>
            </div>
    </body>
</template>

<style>
.gradient-custom-HomePage {
  /* fallback for old browsers */
  background: #4F91FC;
  
  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(to right, #0660F3, #2458AD, #4F91FC, #C5D7F3);
  
  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(to right, #0660F3, #2458AD, #4F91FC, #C5D7F3);
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

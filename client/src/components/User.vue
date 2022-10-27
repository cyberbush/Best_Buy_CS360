<template>

  <!--
    THINGS TO FINSIH 10-21-22
  1. banner picture
  2. finish styling for demo
  3. figure out how to import from DBMS
  4. Finish nav-bar design
  5. Login system
  -->
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
                  <!-- <a class="dropdown-item text-justify" href="Product">Products</a>
                  <a class="dropdown-item text-justify" href="Services">Services</a>
                  <a class="dropdown-item text-justify" href="All_In_One">All-In-One Packages</a>
                  <a class="dropdown-item text-justify" href="Wishlist">Wishlist</a> -->
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
        <div class="container_page rounded-5">
          <div class="row">
            <!--Featured product section-->
            <div class="col-7 text-center mx-auto container-fluid">
              <div class="row bg-primary text-lg-center font-weight-bolder">
                <h2_User>Featured Product!</h2_User>
              </div>
              <div class="row">
                <div class="container_user align-content-center">
                  <div class="card bg-light border border-primary rounded-5" style="width:auto">
                    <img class="card-img-top" src="../components/Logo/logo.png" alt="Card image">
                    <div class="card-body text-center ">
                      <h4 class="card-title text-dark font-weight-bold">Product #1326</h4>
                      <p class="card-text text-dark">This is a product, it is this thingy.</p>
                      <p class="display-5 my-4 text-primary fw-bold">$1000.99/mo</p>
                      <!--Add link to cart database here!-->
                      <button type="button" class="btn btn-primary btn-lg">
                        <span class="glyphicon glyphicon-shopping-cart">
                        </span>
                        <b> Add to Cart </b>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!--Based on your cart section-->
            <div class="col-3 text-center mx-auto ">
              <div class="row bg-primary">
                <h2_User>Based on your cart, you may be interested in:</h2_User>
              </div>
              <div class="row">
                <div class="container_user">
                  <div class="card bg-light border border-primary rounded-5" style="width:auto">
                    <img class="card-img-top" src="../components/Logo/logo.png" alt="Card image">
                    <div class="card-body text-center ">
                      <h4 class="card-title text-dark fw-bold">Product #235346526</h4>
                      <p class="card-text text-dark">This is a product, it is this thingy.</p>
                      <p class="display-5 my-4 text-primary fw-bold">$1550.99/mo</p>
                      <!--Add link to cart database here!-->
                      <button type="button" class="btn btn-primary btn-lg">
                        <span class="glyphicon glyphicon-shopping-cart">
                        </span>
                        <b> Add to Cart </b>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="container_user">
                  <div class="card bg-light border border-primary rounded-5" style="width:auto">
                    <img class="card-img-top" src="../components/Logo/logo.png" alt="Card image">
                    <div class="card-body text-center ">
                      <h4 class="card-title text-dark fw-bold">Product #2342346</h4>
                      <p class="card-text text-dark">This is a product, it is this thingy.</p>
                      <p class="display-5 my-4 text-primary fw-bold">$1.99/mo</p>
                      <!--Add link to cart database here!-->
                      <button type="button" class="btn btn-primary btn-lg">
                        <span class="glyphicon glyphicon-shopping-cart">
                        </span>
                        <b> Add to Cart </b>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="container_user">
                  <div class="card bg-light border border-primary rounded-5" style="width:auto">
                    <img class="card-img-top" src="../components/Logo/logo.png" alt="Card image">
                    <div class="card-body text-center ">
                      <h4 class="card-title text-dark fw-bold">Product #13226</h4>
                      <p class="card-text text-dark">This is a product, it is this thingy.</p>
                      <p class="display-5 my-4 text-primary fw-bold">$1000.99/mo</p>
                      <!--Add link to cart database here!-->
                      <button type="button" class="btn btn-primary btn-lg">
                        <span class="glyphicon glyphicon-shopping-cart">
                        </span>
                        <b> Add to Cart </b>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <br>
          <br>
          <br>
          <!--Your Cart-->
          <div class="col text-center mx-auto">
            <div class="row bg-primary mx-auto">
              <h2_User>Your Cart:</h2_User>
            </div>
            <div class="row mx-auto  ">
              <p>Hello world</p>
            </div>
          </div>
        </div>
  </body>
    


</template>

<script>
 export default {
    data: () => ({
      show: false,
    }),
  }
</script>

<style>

</style>
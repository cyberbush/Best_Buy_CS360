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
          <nav class="navbar navbar-expand-lg navbar-light bg-primary">
              <a class="navbar-brand" href="#">
                <img src="https://mdbcdn.b-cdn.net/img/logo/mdb-transaprent-noshadows.webp" height="20" alt="MDB Logo"
                  loading="lazy" />
              </a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                  <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarNavDarkDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      <i class="bi bi-menu-button"></i>
                    </a>
                    <div class="dropdown-menu bg-dark text-light" aria-labelledby="navbarNavDarkDropdown">
                      <a class="dropdown-item" href="/">Home</a>
                      <a class="dropdown-item" href="/Product">Products</a>
                      <a class="dropdown-item" href="Services">Services</a>
                      <a class="dropdown-item" href="#">All-In-One Packages</a>
                      <a class="dropdown-item" href="#">wishlist</a>
                      <a class="dropdown-item" href="#">About</a>
                      <a class="dropdown-item" href="#">Help</a>
                    </div>
                  </li>
                </ul>
                <form class="form-inline my-2 my-lg-0">
                  <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                  <button class="btn btn-outline-light my-2 my-sm-0 bg-secondary" type="submit">Search</button>
                </form>
              </div>
          </nav>
        </div>
        <!--BANNER SECTION-->
        <div class="container_banner">
          <p>Welcome to the User Page!</p>
          
        </div>
        <!--END BANNER SECTION-->
        <br>
        <br>
        <br>
        <br>
        <br>
        <!--main body columns and rows-->
        <div class="container_page">
          <div class="row ">
            <!--Featured product section-->
            <div class="col-7 text-center mx-auto border border-primary container-fluid">
              <div class="row bg-primary Text-lg-center">
                <h2>Featured Product!</h2>
              </div>
              <div class="row border border-danger container-fluid">
                <div class="container_user">
                  <div class="card bg-dark" style="width:100%">
                    <img class="card-img-top" src="img_avatar1.png" alt="Card image">
                    <div class="card-body">
                      <h4 class="card-title">Product Name</h4>
                      <p class="card-text">Product description</p>
                      <!--Add link to cart database here!-->
                      <a href="#" class="btn btn-primary text-sm-center">Add to cart!</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!--Based on your cart section-->
            <div class="col-3 text-center border mx-auto border-primary">
              <div class="row bg-primary">
                <h2>Based on your cart, you may be interested in:</h2>
              </div>
              <div class="row border border-danger">
                <div class="container_user">
                  <div class="card" style="width:400px">
                    <img class="card-img-top" src="img_avatar1.png" alt="Card image">
                    <div class="card-body">
                      <h4 class="card-title">John Doe</h4>
                      <p class="card-text">Some example text.</p>
                      <!--Add link to cart database here!-->
                      <a href="#" class="btn btn-primary">Add to cart!</a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row border border-danger">
                <div class="container_user">
                  <div class="card" style="width:400px">
                    <img class="card-img-top" src="img_avatar1.png" alt="Card image">
                    <div class="card-body">
                      <h4 class="card-title">John Doe</h4>
                      <p class="card-text">Some example text.</p>
                      <!--Add link to cart database here!-->
                      <a href="#" class="btn btn-primary">Add to cart!</a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row border border-danger">
                <div class="container_user">
                  <div class="card" style="width:400px">
                    <img class="card-img-top" src="img_avatar1.png" alt="Card image">
                    <div class="card-body">
                      <h4 class="card-title">John Doe</h4>
                      <p class="card-text">Some example text.</p>
                      <!--Add link to cart database here!-->
                      <a href="#" class="btn btn-primary">Add to cart!</a>
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
              <h2>Your Cart:</h2>
            </div>
            <div class="row border border-danger mx-auto  ">
              <p>Hello world</p>
            </div>
          </div>
        </div>
  </body>
    


</template>

<script>

</script>

<style>

</style>
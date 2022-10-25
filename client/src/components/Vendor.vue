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
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-laptop" viewBox="0 0 16 16">
                        <path d="M13.5 3a.5.5 0 0 1 .5.5V11H2V3.5a.5.5 0 0 1 .5-.5h11zm-11-1A1.5 1.5 0 0 0 1 3.5V12h14V3.5A1.5 1.5 0 0 0 13.5 2h-11zM0 12.5h16a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 12.5z"/>
                      </svg>
                    </div>
                      <div class="col-md-7">
                          <br>
                          <h5 class="card-title">300 Mbps Internet</h5>
                          <p class="card-text"><small class="text-muted">No data caps and no Contract</small></p>
                          <p class="card-text"><small class="text-muted">So much</small></p>
                        
                      </div>
                      <div class="col-md-2">
                          <br>
                          <h5 class="card-title">$40</h5>
                        
                      </div>
                    </div>
                  </div>
                </div>
                </div> </div>
            </div>
<div class="container-fluid" style="background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);">
    <div class="container p-5">
      <div class="row">
        <div class="col-lg-4 col-md-12 mb-4">
          <div class="card h-100 shadow-lg">
            <div class="card-body">
              <div class="text-center p-3">
                <h5 class="card-title">Basic</h5>
                <small>Individual</small>
                <br><br>
                <span class="h2">$8</span>/month
                <br><br>
              </div>
              <p class="card-text"><small class="text-muted">Some quick example text to build on the card title and make up the bulk of the card's content.</small></p>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> No intitial sign up fee</li>
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> Set your own text limits</li>
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> AutoPay</li>
            </ul>
            <div class="card-body text-center">
              <button class="btn btn-outline-primary btn-lg" style="border-radius:30px">Select</button>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-12 mb-4">
          <div class="card h-100 shadow-lg">
            <div class="card-body">
              <div class="text-center p-3">
                <h5 class="card-title">Standard</h5>
                <small>Small Business</small>
                <br><br>
                <span class="h2">$20</span>/month 
                <br><br>
              </div>
              <p class="card-text"><small class="text-muted">Some quick example text to build on the card title and make up the bulk of the card's content.</small></p>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> No contracts</li>
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> Enhanced Security for all devices </li>
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> No added taxes or fees</li>
            </ul>
            <div class="card-body text-center">
              <button class="btn btn-outline-primary btn-lg" style="border-radius:30px">Select</button>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-12 mb-4">
          <div class="card h-100 shadow-lg">
            <div class="card-body">
              <div class="text-center p-3">
                <h5 class="card-title">Premium</h5>
                <small>Large Companies</small>
                <br><br>
                <span class="h2">$40</span>/month
                <br><br>
              </div>
              <p class="card-text"><small class="text-muted">Some quick example text to build on the card title and make up the bulk of the card's content.</small></p>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> Unlimited Text and Talk</li>
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> Easy add devices</li>
              <li class="list-group-item"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
              </svg> No fee increases</li>
            </ul>
            <div class="card-body text-center">
              <button class="btn btn-outline-primary btn-lg" style="border-radius:30px">Select</button>
            </div>
          </div>
        </div>
      </div>    
    </div>
  </div>

  </div>
</div>

<form>
<div class="container_page rounded-5">
  <div class="row">
  <div class="col-7 text-center mx-auto container-fluid">
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="inputEmail4">Product Name</label>
          <input type="email" class="form-control" id="inputEmail4" placeholder="High-speed Internet Router">
        </div>
        <div class="form-group col-md-6">
          <label for="inputPassword4">Product Number</label>
          <input type="password" class="form-control" id="inputPassword4" placeholder="N00907678">
        </div>
      </div>
      <div class="form-group">
        <label for="inputAddress">Description</label>
        <input type="text" class="form-control" id="inputAddress" placeholder="Two packet-switched network connector">
      </div>
      <div class="form-group">
        <label for="inputAddress2">Product Brand</label>
        <input type="text" class="form-control" id="inputAddress2" placeholder="NETGEAR">
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="inputCity">City</label>
          <input type="text" class="form-control" id="inputCity">
        </div>
        <div class="form-group col-md-4">
          <label for="inputState">Product Category</label>
          <select id="inputState" class="form-control">
            <option selected>Choose...</option>
            <option>...</option>
          </select>
        </div>
        <div class="form-group col-md-2">
          <label for="inputZip">Price</label>
          <input type="text" class="form-control" id="inputZip">
        </div>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="gridCheck">
          <label class="form-check-label" for="gridCheck">
            Check me out
          </label>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Sign in</button>
    </div>
  </div>
  </div>
</form>

</body>
</template>

<script>

</script>

<style>
    .card {
      border:none;
      padding: 10px 50px;
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
      box-shadow: 0 1rem 3rem rgba(0,0,0,.75) !important;
    }

    .card:hover::after {
      opacity: 1;
    }

    .card:hover .btn-outline-primary{
      color:white;
      background:#007bff;
    }

    .px-2 {
      padding-left: ($spacer * .45) !important;
      padding-right: ($spacer * .45) !important;
    }

</style>
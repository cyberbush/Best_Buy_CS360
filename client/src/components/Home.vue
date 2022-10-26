<template>
    <body class="bg-dark">
          <!--main body columns and rows-->
            <section class="h-100 gradient-form" style="background-color: #4F91FC;">
              <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                  <div class="col-xl-10">
                    <div class="card rounded-3 text-black">
                      <div class="row g-0">
                        <div class="col-lg-6">
                          <div class="card-body p-md-5 mx-md-4">
            
                            <div class="text-center">
                              <img src="../components/Logo/logo_transparent.png"
                                style="width: 185px;" alt="logo">
                              <h4 class="mt-1 mb-5 pb-1">Welcome to Best Buy Tech-Service!</h4>
                            </div>
            
                            <form>
                              <p>Please login to your account</p>
            
                              <div class="form-outline mb-4">
                                <input type="email" id="form2Example11" class="form-control"
                                  placeholder="Phone number or email address" />
                                <label class="form-label" for="form2Example11">Username</label>
                              </div>
            
                              <div class="form-outline mb-4">
                                <input type="password" id="form2Example22" class="form-control" />
                                <label class="form-label" for="form2Example22">Password</label>
                              </div>
            
                              <div class="text-center pt-1 mb-5 pb-1">
                                <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="button">Log
                                  in</button>
                                <a class="text-muted" href="#!">Forgot password?</a>
                              </div>
            
                              <div class="d-flex align-items-center justify-content-center pb-4">
                                <p class="mb-0 me-2">Don't have an account?</p>
                                <button type="button" class="btn btn-outline-primary">Create new</button>
                              </div>
            
                            </form>
            
                          </div>
                        </div>
                        <div class="col-lg-6 d-flex align-items-center gradient-custom-HomePage">
                          <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                            <h4 class="mb-4">Welcome to Best Buy! But we are not the big yellow tag you know...</h4>
                            <p class="small mb-0">We are here to make your home technology easy to purchase, for a price that you want, and a plan that you want!
                              With just a few clicks, you can have the setup of your dreams headed your way, for the price of your dreams! 
                            </p>
                            <p>We cannot way to help you on the path of your dreams! Lets get started!</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </section>
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

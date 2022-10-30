<template>
  <body class=" h-100 gradient-custom-HomePage">
    <!--main body columns and rows-->
    <section class="h-100 gradient-form ">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-xxl">
            <div class="card rounded-3" style="background-color:#A9A9A9">
              <div class="row g-0">
                <div class="col-lg-6">
                  <div class="card-body p-md-5 mx-md-4">
    
                    <div class="text-center">
                      <img src="../components/Logo/logo_transparent.png"
                        style="width: 185px;" alt="logo">
                      <h2_home class="mt-1 mb-5 pb-1">Welcome!</h2_home>
                    </div>
                        <br>
                    <form>
                      <h_sub>Please login to your account</h_sub>
    
                      <div class="form-outline mb-4">
                        <input type="email" id="form2Example11" class="form-control"
                          placeholder="Phone number or email address" />
                        <h_sub class="form-label" for="form2Example11">Username</h_sub>
                      </div>
    
                      <div class="form-outline mb-4">
                        <input type="password" id="form2Example22" class="form-control" placeholder="**********" />
                        <h_sub class="" for="form2Example22">Password</h_sub>
                      </div>
    
                      <div class="text-center pt-1 mb-5 pb-1">
                        <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="button" onclick="../components/User.vue">Log
                          in</button>
                        <a class="h_text text-dark" href="#!">Forgot password?</a>
                      </div>
    
                      <div class="d-flex align-items-center justify-content-center pb-8">
                        <p class="mb-0 text-dark text-center mb-3">Don't have an account?</p>
                        <button type="button" class="btn btn-primary" onclick="location.href='Signup'">Create New Account</button>
                      </div>
    
                    </form>
    
                  </div>
                </div>
                <div class="col-lg-6 d-flex align-items-center gradient-custom-HomePage">
                  <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                    <h2_Home-Secondary class="">Begin living your tech dreams!</h2_Home-Secondary>
                    <br>
                    <br>
                    <h_sub class="small mb-0">This software is here to support your dreams! We can help you decide on a best fit for your
                      current lifestyle, and help taylor a perfect, at-home- tech and service package deal in order to meet your needs and help you
                    fulfill your dreams! Login or Signup today! </h_sub>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
      <!--<div id="home">
          <h1>Home Page</h1>
          <a href="/Product_Menu"><u>Go to Product Menu Example</u></a>
          <a href="/vendor"><u>Go to Vendor</u></a>
          <a href="/user"><u>Go to User</u></a>
      </div>-->
    </body>
</template>

<style>
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

  .homepage_login{
    background: whitesmoke;
    
  }
  
</style>

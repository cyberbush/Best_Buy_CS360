<template>
    <body class="gradient-custom-HomePage">
        <!--main body columns and rows-->
            <div class="container py-5 border border-dangerss">
              <div class="row d-flex justify-content-center align-items-center h-100 border border-warning">
                <div class="col-xxl">
                  <div class="card rounded-3" style="background-color:#A9A9A9">
                    <div class="row g-0">
                    <div class="card-body p-md-5 mx-md-4">
                        <div class="text-center border border-success">
                        <img src="../components/Logo/logo_transparent.png"
                            style="width: 185px;" alt="logo">
                        <h2 id="h2_home" class="mt-1 mb-5 pb-1">Welcome!</h2>
                        </div>
                        <br>
                        <div class="container">
                            <h_sub>Please login to your account</h_sub>
                            <div class="mx-auto my-4 text-center">
                                <button class="btn btn-primary mx-4 text-center">
                                    <a href="/LoginVendor">Vendor</a>
                                </button>
                                <button class="btn btn-primary mx-4 text-center">
                                    <a href="/Login">User</a>
                                </button>
                            </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        </div>  
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
</style>
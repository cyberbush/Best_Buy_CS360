<template>
    <section class="vh-100 bg-image" style="background-color:#0660F3;">
      <div class="mask d-flex align-items-center h-100 gradient-custom-Signup0">
        <div class="container h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-9 col-lg-7 col-xl-6">
              <div class="card" style="border-radius: 15px;">
                <div class="card-body p-5">
                  <label class="text-uppercase text-center mb-5 text-dark">Create an account</label>
    
                  <form @submit="submit_data" class="text-center">
    
                    <div class="form-outline mb-2 mt-2">
                      <input type="text" id="form3Example1cg" class="form-control form-control " v-model="first_name" placeholder="First Name" />
                      <label class="form-label text-dark" for="form3Example1cg" placeholder="First name">First Name</label>
                    </div>
                    <div class="form-outline mb-2 mt-2">
                      <input type="text" id="form3Example1cg" class="form-control form-control" v-model="last_name" placeholder="Last Name" />
                      <label class="form-label text-dark" for="form3Example1cg" placeholder="First and Last Name">Last Name</label>
                    </div>
    
                    <div class="form-outline mb-2 amt-2">
                      <input type="email" id="form3Example3cg" class="form-control form-control" v-model="email" placeholder="Email"/>
                      <label class="form-label text-dark" for="form3Example3cg">Your Email</label>
                    </div>
    
                    <div class="form-outline mb-2 mt-2">
                      <input type="password" id="form3Example4cg" class="form-control form-control" v-model="password" placeholder="Password"/>
                      <label class="form-label text-dark" for="form3Example4cg">Password</label>
                    </div>
    
                    <div class="form-outline mb-2 mt-2">
                      <input type="password" id="form3Example4cdg" class="form-control form-control" v-model="password_confirm" placeholder="Confirm Password" />
                      <label class="form-label text-dark" for="form3Example4cdg">Repeat your password</label>
                    </div>
                    <div class="form-check d-flex justify-content-center mb-3">
                      
                      <label class="form-check-label text-dark mb-2" for="">
                        I am associated with a service company: <a href="help" class="text-body"></a>
                      </label>
                      <br>
                      <input class="form-check-input mb-2" type="checkbox" value="" id="form2Example3cg" />
                    </div>
    
                    <div class="d-flex justify-content-center mb-3">
                      <button type="button" class="btn btn-success btn-block btn-lg gradient-custom-Signup1 text-light">Register</button>
                    </div>
    
                    <p class="text-center text-muted mt-2 mb-3">Have already an account? <a href="/"
                        class="fw-bold text-body"><u>Login here</u></a></p>
    
                  </form>
    
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
</template>
<style>
.gradient-custom-Signup0 {
    /* fallback for old browsers */
    background: #0660F3;
    
    /* Chrome 10-25, Safari 5.1-6 */
    background: -webkit-linear-gradient(to right, #0660F3, #2458AD, #4F91FC, #C5D7F3);
    
    /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    background: linear-gradient(to right, #0660F3, #2458AD, #4F91FC, #C5D7F3)
    }
    .gradient-custom-Signup1 {
    /* fallback for old browsers */
    background: #0660F3;
    
    /* Chrome 10-25, Safari 5.1-6 */
    background: -webkit-linear-gradient(to right, #0660F3, #2458AD, #4F91FC, #C5D7F3);
    
    /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    background: linear-gradient(to right, #0660F3, #2458AD, #4F91FC, #C5D7F3)
    }

</style>

<script>
export default {
  name: 'Register',
  data() {
    return{
      first_name:'',
      last_name:'',
      email:'',
      password:'',
      password_confirm:'',
    }
  },
  methods:{
    submit_data(){
      const data ={
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        password: password,
        password_confirm:password_confirm,
    };
      console.log(data)
    }
  }
};
</script>
<template>
    <section class="vh-100 bg-image" style="background-color:#0660F3;">
      <div class="mask d-flex align-items-center h-100 gradient-custom-Signup0">
        <div class="container h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-9 col-lg-7 col-xl-6">
              <div class="card" style="border-radius: 15px;">
                <div class="card-body p-5">
                  <label class="text-uppercase text-center mb-5 text-dark">Create an account</label>
    
                  <form id="registerForm" class="text-center">
    
                    <div class="form-outline mb-2 mt-2">
                      <label class="form-label text-dark" for="form3Example1cg" placeholder="First name">First Name</label>
                      <input type="text" id="form3Example1cg" class="form-control form-control " v-model="firstName" placeholder="First Name" />
                    </div>
                    <div class="form-outline mb-2 mt-2">
                      <label class="form-label text-dark" for="form3Example1cg" placeholder="First and Last Name">Last Name</label>
                      <input type="text" id="form3Example1cg" class="form-control form-control" v-model="lastName" placeholder="Last Name" />
                    </div>
    
                    <div class="form-outline mb-2 amt-2">
                      <label class="form-label text-dark" for="form3Example3cg">Your Email</label>
                      <input type="email" id="form3Example3cg" class="form-control form-control" v-model="email" placeholder="Email"/>
                    </div>
    
                    <div class="form-outline mb-2 mt-2">
                      <label class="form-label text-dark" for="form3Example4cg">Password</label>
                      <input type="password" id="form3Example4cg" class="form-control form-control" v-model="password" placeholder="Password"/>
                    </div>
    
                    <div class="form-outline mb-2 mt-2">
                      <label class="form-label text-dark" for="form3Example4cdg">Repeat your password</label>
                      <input type="password" id="form3Example4cdg" class="form-control form-control" v-model="password_confirm" placeholder="Confirm Password" />
                    </div>
                    <div class="form-check d-flex justify-content-center mb-3">
                      
                      <label class="form-check-label text-dark mb-2" for="">
                        I am associated with a service company: <a href="help" class="text-body"></a>
                      </label>
                      <br>
                      <input class="form-check-input mb-2" type="checkbox" value="" id="form2Example3cg" />
                    </div>
                  </form>

                    <div class="d-flex justify-content-center mb-3">
                      <button type="button" @click=submit_user() class="btn btn-success btn-block btn-lg gradient-custom-Signup1 text-light">Register</button>
                    </div>
    
                    <p class="text-center text-muted mt-2 mb-3">Have already an account? <a href="/"
                        class="fw-bold text-body"><u>Login here</u></a></p>    
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      firstName:'',
      lastName:'',
      email:'',
      password:'',
      password_confirm:'',
    }
  },
  methods:{
    sleep: function(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    submit_user: async function(){
      var data ={ firstName: this.firstName, lastName: this.lastName, email: this.email, password: this.password };
      console.log(data);
      this.axios
        .post("http://localhost:5000/api/signup", data)
        .then(response => console.log(response.data))
        .catch(error => { console.log(error.response) });
      // add small delay
      await this.sleep(2000);
      location.href = '/'; // Redirect to login
    },
  }
};
</script>

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
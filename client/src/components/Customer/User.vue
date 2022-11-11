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
                  <a class="dropdown-item text-justify" href="/">Log Out</a>
                  <a class="dropdown-item text-justify" href="/User/this.currentUser.id">Home</a>
                  <a class="dropdown-item text-justify" href="Product">Products</a>
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
            <p class="" v-if="currentUser!=null">Logged in as {{this.currentUser.firstName}}</p>
          </nav>
        </div>
        <!--BANNER SECTION-->
        <div class="Banner_Container">
          <img src="../Logo/Vendor_Logo.png" class="" height="150px" width="100%" alt="Matrix picture Banner">
        </div>
        <!--END BANNER SECTION-->
        <!--main body columns and rows-->

        <!--This area is the base for the many products that will show up, and as we add/ subtract items from the DB
        we will see it grow and shrink... doing test run with arrays at this time to make sure using base level scripts 
        in page... TJR 11/10/2022
      
        UPDATE 11/11/2022: redesign in process, linking products database to system, will have cards... looking for good ecommerse page layout
        as well =) DONT PANIC... and dont forget a towel!--> 

        <div class="container">
          <section class="mx-auto my-5" style="max-width: 23rem;">
            <div class="card">
              <div class="bg-image hover-overlay ripple" data-mdb-ripple-color="light">
                <img src="https://mdbootstrap.com/img/Photos/Horizontal/Food/8-col/img (5).jpg" class="img-fluid" />
                <a href="#!">
                  <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
                </a>
              </div>
              <div class="card-body">
                <p class="card-title font-weight-bold text-dark"><a>Product name</a></p>
                <ul class="list-unstyled list-inline mb-0">
                  <li class="list-inline-item me-0">
                    <i class="fas fa-star text-warning fa-xs"> </i>
                  </li>
                  <li class="list-inline-item me-0">
                    <i class="fas fa-star text-warning fa-xs"></i>
                  </li>
                  <li class="list-inline-item me-0">
                    <i class="fas fa-star text-warning fa-xs"></i>
                  </li>
                  <li class="list-inline-item me-0">
                    <i class="fas fa-star text-warning fa-xs"></i>
                  </li>
                  <li class="list-inline-item">
                    <i class="fas fa-star-half-alt text-warning fa-xs"></i>
                  </li>
                  <li class="list-inline-item">
                    <p class="text-muted">4.5 (413)</p>
                  </li>
                </ul>
                <p class="mb-2 text-dark">product price</p>
                <p class="card-text text-dark">
                  THIS IS BEING WORKED ON! TEST TEST TEST!!! - TJR 11/11/2022
                </p>
                <hr class="my-4" />
                <p class="lead"><strong>Tonight's availability</strong></p>
                <ul class="list-unstyled list-inline d-flex justify-content-between">
                  <li class="list-inline-item me-0">
                    <div class="chip me-0">5:30PM</div>
                  </li>
                  <li class="list-inline-item me-0">
                    <div class="chip bg-secondary text-white me-0">7:30PM</div>
                  </li>
                  <li class="list-inline-item me-0">
                    <div class="chip me-0">8:00PM</div>
                  </li>
                  <li class="list-inline-item me-0">
                    <div class="chip me-0">9:00PM</div>
                  </li>
                </ul>
                <a href="#!" class="btn btn-link link-secondary p-md-1 mb-0">Button</a>
              </div>
            </div>
            
          </section>
        </div>
  </body>
    


</template>

<script>
//Tracy TO-DO:
//-link products page - 11/11/2022
export default {
  name: 'Register',
  data() {
    return {
        show: false,
        users: [ { id: 0, firstName: "", lastName: "", email: "", password: ""}, ],
        currentUser: null,
    }
  },
  mounted: function() {
    this.read_users();
  },
  methods: {
    load_user: function() {
      this.users.forEach( user => {
        if (user.id == this.$route.params.id) {
          this.currentUser = user;
        }
      })
    },
    read_users: function() {
      this.axios
        .get("http://localhost:5000/api/users")
        .then(response => {
          this.users = response.data;
          this.load_user();
        })
        .catch(error => { console.log(error.response) });
    },
    delete_user: function(id) {
      var data = {'delete': true, 'id': id };
      this.axios
        .post("http://localhost:5000/api/users", data)
        .then(response => (this.users = response.data))
        .catch(error => { console.log(error.response) });
    },
  }
};
</script>

<style>

</style>
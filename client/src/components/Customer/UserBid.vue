<template>
<body class="gradient-custom-HomePage">
    <header>
  <!-- Navbar -->
      <nav class="navbar navbar-expand-sm py-0 align-top navbar-dark bg-primary text-light border  border-5 border-dark rounded">
        <!-- Container wrapper -->
        <div class="container-fluid">
          <!-- Toggle button -->
          <button
            class="navbar-toggler"
            type="button"
            data-mdb-toggle="collapse"
            data-mdb-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <i class="fas fa-bars"></i>
          </button>

          <!-- Collapsible wrapper -->
        <div class="collapse navbar-collapse " id="navbarSupportedContent">
          <!-- Navbar brand -->
            <a class="navbar-brand d-inline-block align-top py-0" href="#">
            <img
              src="../Logo/logo_transparent.png"
              height="50"
              class="pr-3"
              alt="Best Buy! Logo"
              loading="lazy"
            />Welcome to UserBids!
          </a>            
            <!-- Left links -->
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" href="/Users"></a>
              </li>
            </ul>
            <!-- Left links -->
          </div>
          <!-- Collapsible wrapper -->

          <!-- Right elements -->
          <div class="d-flex align-items-center">
            <!-- Icon -->
            <a class="link-secondary me-3" href="#">
              <i class="fas fa-shopping-cart"></i>
            </a>

            <!-- Avatar -->
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle border border-dark" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                {{ currentUser.firstName }}
              </button>
              <div class="dropdown-menu bg-primary border border-dark text-justified" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item bg-primary" href="UserSearch">Search for Products!</a>
                <a class="dropdown-item bg-primary" href="UserBid">View Bids!</a>
                <a class="dropdown-item bg-primary" href="/">Logout!</a>
              </div>
            </div>
          </div>
          <!-- Right elements -->
        </div>
        <!-- Container wrapper -->
      </nav>
  <!-- Navbar -->
    </header>
    <main>
        <h1>This is the customer bidding page</h1>
    </main>
</body>

</template>
<script>
export default {
  name: 'Register',
  data() {
    return {
        show: false,
        users: [ { id: 0, firstName: "", lastName: "", email: "", password: ""}, ],
        products: [ { id: 0, name: "", price: 0.00, size: 0.00, description: "", category: "", brand: ""}, ],
        currentUser: null,
    }
  },
  mounted: function() {
    this.read_users();
    this.read_products();
  },
  methods: {
    //USERS FUNCTIONS===========================================================
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
    //!USERS FUNCTIONS===========================================================
    
    //PRODUCT FUNCTIONS===========================================================
    read_products: function() {
      this.axios
        .get("http://localhost:5000/api/products")
        .then(response => (this.products = response.data))
        .catch(error => { console.log(error.response) });
    },
    //!PRODUCT FUNCTIONS===========================================================

  }
};
</script>
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
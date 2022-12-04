<template>
    <body class="gradient-custom-HomePage">      
        <main>
            <h1>This is the customer search page</h1>
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
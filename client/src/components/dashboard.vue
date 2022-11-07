<template>
<div id="dashboardMenu" class="container">
    <h2> User's Table </h2>
    <h2 v-if="currentUser!=null"> User is {{ currentUser.firstName }} </h2>
    <div id="userTable" class="userTable">
        <ul>
            <li v-for="user in users" :key="user.id"> 
            {{ user.firstName + " | " + user.lastName + " | " + user.email + " | " + user.password }}<button class="btn btn-primary" @click="delete_user(id=user.id)">Delete</button>
            </li>
        </ul>
      <h5><a href="/user">Go to User's Page</a></h5>
    </div>
</div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
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
.userTable {
    background-color: white;
    margin: auto;
    margin-top: 50px;
    border: 6px solid #0AF;
    padding: 50px;
    text-align: center;
}
</style>
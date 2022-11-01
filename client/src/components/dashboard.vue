<template>
<script type="text/javascript" src="Home.vue"> </script>
<div id="dashboardMenu" class="container">
    <h2> User's Table </h2>
    <div id="userTable" class="userTable">
        <ul>
            <li v-for="user in users" :key="user.id"> 
            {{ user.firstName + " | " + user.lastName + " | " + user.email + " | " + user.password }}<button class="btn btn-primary" @click="delete_user(id=user.id)">Delete</button>
            </li>
        </ul>
    <h5 href="/user">Go to User's Page</h5>
    </div>
</div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
        currentUser: {},
        users: [ { id: 0, firstnName: "", lastName: "", email: "", password: ""}, ],
    }
  },
  mounted: function() {
    this.read_users();
  },
  },
  methods:{
    read_users: function() {
      this.axios
        .get("http://localhost:5000/api/users")
        .then(response => (this.users = response.data))
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
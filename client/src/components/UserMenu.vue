<template>
<div id="UserMenu" class="container">
    <h1> User Menu </h1>
    <!-- <form> -->
        <div class="form-group">
            <label for="user_name">Name</label>
            <input type="text" class="form-control" id="user_name" v-model="user_name" placeholder="Enter name">
        </div>
        <div class="form-group">
            <label for="user_desc">Description</label>
            <input type="text" class="form-control" id="user_desc" v-model="user_desc" placeholder="Enter description">
        </div>
        <div class="form-group">
            <label for="user_status">Status</label>
            <input type="text" class="form-control" id="user_status" v-model="user_status" placeholder="Enter status">
        </div>
        <button class="btn btn-primary" @click="update_User(id=-1, name=user_name, description=user_desc, status=user_status, delete_=false)">Add New User</button>
    <!-- </form> -->
    <h2> User Table </h2>
    <div id="userTable" class="userTable">
        <ul>
            <li v-for="user in users" :key="user.id"> 
            {{ user.name + " | " + user.description + " | " + user.status }}
            <button class="btn btn-primary" @click="update_User(id=user.id, name='', description='', status='', delete_=true)">Delete</button>
            </li>
        </ul>
    </div>
</div>
</template>

<script>
import { setTimeout } from "timers";
export default {
  name: "user_comp",
  data: function() {
    return {
      user_name: "",
      user_desc: "",
      user_status: "",
      users: [
        { id: 0, name: "", description: "", status: ""},
      ],
    };
  },
  mounted: function() {
    this.read_users();
  },
  computed: {
  },
  methods: {
    // all the methods will be replaced with REST API call later
    read_users: function() {
        this.axios
            .get("http://localhost:5000/users_db")
            .then(response => (this.users = response.data))
            .catch(error => { console.log(error.response) });
    },
    update_User: function( id = -1, name = "", description = "", status = "", delete_ = false) 
    {
        var data = { id: id, name: name, description: description, status: status, delete: delete_ };
        this.axios
            .post("http://localhost:5000/users_db", data)
            .then(() => this.read_users())
            .catch(error => { console.log(error.response) });
        //   add a delay to make sure the backend respond
    },
    print: function(data){
        console.log(data)
    }
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
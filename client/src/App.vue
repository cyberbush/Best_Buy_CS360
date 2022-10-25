<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
  #app {
    margin-top: 30px;
    background-color: #343a40;
  }
  
  #app h1 {
    font-size: 60px;
    line-height: 30px;
    margin: 1em 0 .6em 0;
    font-weight: normal;
    color: white;
    font-family: 'Hammersmith One', sans-serif;
    text-shadow: 0 -1px 0 rgba(59, 48, 48, 0.4);
    position: relative;
    color: #6Cf;
  }
  
  #app h2 {
    margin: 1em 0 .6em 0;
    padding: 0 0 0 20px;
    font-weight: normal;
    color: white;
    font-family: 'Hammersmith One', sans-serif;
    text-shadow: 0 -1px 0 rgba(0,0,0,0.4);
    position: relative;
    font-size: 40px;
    line-height: 40px;
  }
  
  #app h3 {
    margin: 1em 0 .6em 0;
    padding: 0 0 0 20px;
    font-weight: normal;
    color: white;
    font-family: 'Hammersmith One', sans-serif;
    text-shadow: 0 -1px 0 rgba(0,0,0,0.4);
    position: relative;
    font-size: 30px;
    line-height: 40px;
    font-family: 'Questrial', sans-serif;
  }
  
  #app h4, #app a, #app p, #app label { 
    margin: 1em 0 .6em 0;
    padding: 0 0 0 20px;
    font-weight: normal;
    color: white;
    font-family: 'Hammersmith One', sans-serif;
    text-shadow: 0 -1px 0 rgba(0,0,0,0.4);
    position: relative;
    font-size: 25px;
    line-height: 20px;
    font-family: 'Questrial', sans-serif;
  }

  #home, .container{
    margin: auto;
    margin-top: 50px;
    width: 50%;
    border: 6px solid #0AF;
    padding: 50px;
    text-align: center;
  }

  .container button {
    padding: 15px;
    margin: 30px;
  }
  /*added by Tracy Rountree for meeting needs*/
  #app h2_User{
      margin: 1em 0 .6em 0;
      padding: 0 0 0 20px;
      font-weight: bold;
      color: white;
      font-family: 'Hammersmith One', sans-serif;
      text-shadow: 0 -1px 0 rgba(0,0,0,0.4);
      position: relative;
      font-size: 35px;
      line-height: 40px;
  }
 
</style>
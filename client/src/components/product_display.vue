<template>

<body class="h-100 gradient-custom-HomePage">
      <!--Upper Nav-Bar-->
      <div class="bg-dark">
          <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark border border-primary ">
            <a class="navbar-brand" href="/"> Best Buy!
            </a>
            <ul class="navbar-nav">
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Menu
                </a>
                <div class="dropdown-menu bg-primary" aria-labelledby="navbarDropdown">
                  <a class="dropdown-item text-justify" href="/">Home </a>
                  <a class="dropdown-item text-justify" href="vendor">Vendors </a>
                  <a class="dropdown-item text-justify" href="about">About </a>
                  <a class="dropdown-item text-justify" href="help">Help </a>
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
            <p class=""></p>
          </nav>
        </div>
        <br>
        <!--END OF NAVIGATION BAR-->

        <!--adjust column width ratios for many
        also set JS so that if there is x amount of offers, it shows, 
      otherwise dont show the offers!-->
        <div class="container-fluid d-flex justify-content-center">
          <div class="row mt-5">
            <div class="col-sm-4">
              <div class="card">
                <img src="https://imgur.com/edOjtEC.png" class="card-img-top" width="100%">
                <div class="card-body pt-0 px-0">
                  <div class="d-flex flex-row justify-content-between mb-0 px-3">
                    <small class="text-muted mt-1">STARTING AT</small>
                    <h6>&dollar;22,495&ast;</h6>
                  </div>
                  <hr class="mt-2 mx-3">
                  <div class="d-flex flex-row justify-content-between px-3 pb-4">
                    <div class="d-flex flex-column"><span class="text-muted">Fuel Efficiency</span>
                      <small class="text-muted">L/100KM&ast;</small>
                    </div>
                    <div class="d-flex flex-column"><h5 class="mb-0">8.5/7.1</h5>
                      <small class="text-muted text-right">(city/Hwy)</small>
                    </div>
                    </div>
                      <div class="d-flex flex-row justify-content-between p-3 mid">
                        <div class="d-flex flex-column"><small class="text-muted mb-1">ENGINE</small>
                          <div class="d-flex flex-row">
                            <img src="https://imgur.com/iPtsG7I.png" width="35px" height="25px">
                            <div class="d-flex flex-column ml-1">
                              <small class="ghj">1.4L MultiAir</small>
                              <small class="ghj">16V I-4 Turbo</small>
                            </div>
                          </div>
                        </div>
                        <div class="d-flex flex-column">
                          <small class="text-muted mb-2">HORSEPOWER</small>
                          <div class="d-flex flex-row">
                            <img src="https://imgur.com/J11mEBq.png">
                            <h6 class="ml-1">135 hp&ast;</h6>
                          </div>
                        </div>
                      </div>
                      <small class="text-muted key pl-3">Standard key Features</small>
                      <div class="mx-3 mt-3 mb-2">
                        <button type="button" style="background-color: #92FE9D; border: #92FE9D" class="btn btn-success btn-block">
                          <small>BUILD & PRICE</small>
                        </button>
                      </div>
                      <small class="d-flex justify-content-center text-muted">*Legal Disclaimer</small>
                    </div>
                  </div>
                </div>
                <div class="col-sm-4">
                  <div class="card">
                    <img src="https://imgur.com/SKZolYE.png" class="card-img-top" width="100%">
                      <div class="card-body pt-0 px-0">
                        <div class="d-flex flex-row justify-content-between mb-0 px-3">
                        <small class="text-muted mt-1">STARTING AT</small>
                        <h6>&dollar;22,495&ast;</h6>
                      </div>
                      <hr class="mt-2 mx-3">
                      <div class="d-flex flex-row justify-content-between px-3 pb-4">
                        <div class="d-flex flex-column"><span class="text-muted">Fuel Efficiency</span>
                          <small class="text-muted">L/100KM&ast;</small>
                        </div>
                        <div class="d-flex flex-column">
                          <h5 class="mb-0">8.5/7.1</h5>
                          <small class="text-muted text-right">(city/Hwy)</small>
                        </div>
                      </div>
                      <div class="d-flex flex-row justify-content-between p-3 mid">
                        <div class="d-flex flex-column"><small class="text-muted mb-1">ENGINE</small><div class="d-flex flex-row">
                          <img src="https://imgur.com/iPtsG7I.png" width="35px" height="25px"><div class="d-flex flex-column ml-1">
                          <small class="ghj">1.4L MultiAir</small>
                          <small small class="ghj">16V I-4 Turbo</small>
                        </div>
                      </div>
                    </div>
                    <div class="d-flex flex-column">
                      <small class="text-muted mb-2">HORSEPOWER</small>
                        <div class="d-flex flex-row">
                          <img src="https://imgur.com/J11mEBq.png">
                          <h6 class="ml-1">135 hp&ast;</h6>
                        </div>        
                      </div>
                    </div>
                      <small class="text-muted key pl-3">Standard key Features</small>
                        <div class="mx-3 mt-3 mb-2"><button type="button" style="background-color: #92FE9D; border: #92FE9D" class="btn btn-success btn-block">
                          <small>BUILD & PRICE</small>
                          </button>
                        </div>
                        <small class="d-flex justify-content-center text-muted">*Legal Disclaimer</small>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-4">
                    <div class="card">
                      <img src="https://imgur.com/SKZolYE.png" class="card-img-top" width="100%">
                        <div class="card-body pt-0 px-0">
                          <div class="d-flex flex-row justify-content-between mb-0 px-3">
                          <small class="text-muted mt-1">STARTING AT</small>
                          <h6>&dollar;22,495&ast;</h6>
                        </div>
                        <hr class="mt-2 mx-3">
                        <div class="d-flex flex-row justify-content-between px-3 pb-4">
                          <div class="d-flex flex-column"><span class="text-muted">Fuel Efficiency</span>
                            <small class="text-muted">L/100KM&ast;</small>
                          </div>
                          <div class="d-flex flex-column">
                            <h5 class="mb-0">8.5/7.1</h5>
                            <small class="text-muted text-right">(city/Hwy)</small>
                          </div>
                        </div>
                        <div class="d-flex flex-row justify-content-between p-3 mid">
                          <div class="d-flex flex-column"><small class="text-muted mb-1">ENGINE</small><div class="d-flex flex-row">
                            <img src="https://imgur.com/iPtsG7I.png" width="35px" height="25px"><div class="d-flex flex-column ml-1">
                            <small class="ghj">1.4L MultiAir</small>
                            <small small class="ghj">16V I-4 Turbo</small>
                          </div>
                        </div>
                      </div>
                      <div class="d-flex flex-column">
                        <small class="text-muted mb-2">HORSEPOWER</small>
                          <div class="d-flex flex-row">
                            <img src="https://imgur.com/J11mEBq.png">
                            <h6 class="ml-1">135 hp&ast;</h6>
                          </div>        
                        </div>
                      </div>
                        <small class="text-muted key pl-3">Standard key Features</small>
                          <div class="mx-3 mt-3 mb-2"><button type="button" style="background-color: #92FE9D; border: #92FE9D" class="btn btn-success btn-block">
                            <small>BUILD & PRICE</small>
                            </button>
                          </div>
                          <small class="d-flex justify-content-center text-muted">*Legal Disclaimer</small>
                        </div>
                      </div>
                    </div>
                  <div class="col-sm-4">
                    <div class="card">
                      <img src="https://imgur.com/gUQNKPd.png" class="card-img-top" width="100%">
                        <div class="card-body pt-0 px-0">
                          <div class="d-flex flex-row justify-content-between mb-0 px-3">
                            <small class="text-muted mt-1">STARTING AT</small>
                            <h6>&dollar;22,495&ast;</h6>
                          </div>
                          <hr class="mt-2 mx-3">
                          <div class="d-flex flex-row justify-content-between px-3 pb-4">
                            <div class="d-flex flex-column"><span class="text-muted">Fuel Efficiency</span>
                              <small class="text-muted">L/100KM&ast;</small>
                            </div>
                              <div class="d-flex flex-column"><h5 class="mb-0">8.5/7.1</h5>
                                <small class="text-muted text-right">(city/Hwy)</small>
                              </div>
                            </div>
                            <div class="d-flex flex-row justify-content-between p-3 mid">
                              <div class="d-flex flex-column"><small class="text-muted mb-1">ENGINE</small>
                                <div class="d-flex flex-row"><img src="https://imgur.com/iPtsG7I.png" width="35px" height="25px">
                                  <div class="d-flex flex-column ml-1"><small class="ghj">1.4L MultiAir</small>
                                    <small class="ghj">16V I-4 Turbo</small>
                                  </div>
                                </div>
                              </div>
                            <div class="d-flex flex-column">
                              <small class="text-muted mb-2">HORSEPOWER</small>
                              <div class="d-flex flex-row">
                                <img src="https://imgur.com/J11mEBq.png">
                                <h6 class="ml-1">135 hp&ast;</h6>
                              </div>
                            </div>
                          </div>
                        <small class="text-muted key pl-3">Standard key Features</small>
                      <div class="mx-3 mt-3 mb-2">
                        <button type="button" style="background-color: #92FE9D; border: #92FE9D" class="btn btn-success btn-block">
                          <small>BUILD & PRICE</small>
                        </button>
                      </div>
                      <small class="d-flex justify-content-center text-muted">*Legal Disclaimer</small>
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

  .homepage_login{
    background: whitesmoke;
    
  }
  
</style>

<script>
//ADD DATABASE CONNECTION HERE
export default{
  name: "App",
  data: () => {
    return{
      products: [
        {
          name: "Apple Watch",
          cost: "$499.56",
          image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1Vd_ryVhLC8nBtyZbgQ03y2_BFIrW1zcfFg&usqp=CAU",
        },
        {
          name: "Apple iPad",
          cost: "$499.56",
          image: "https://i.ebayimg.com/images/g/knYAAOSwPypaZFdH/s-l640.jpg",
        },
        {
          name: "Apple iMac",
          cost: "$499.56",
          image: "data:image/jpeg;base64,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",
        },
        {
          name: "Apple Apple SUPREME GRANDE DELUX, with Cheese, CRISPY!",
          cost: "$499.56",
          image: "data:image/png;base64,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",
        },
        {
          name: "Apple Watch",
          cost: "$499.56",
          image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1Vd_ryVhLC8nBtyZbgQ03y2_BFIrW1zcfFg&usqp=CAU",
        },
        {
          name: "Apple iPad",
          cost: "$499.56",
          image: "https://i.ebayimg.com/images/g/knYAAOSwPypaZFdH/s-l640.jpg",
        },
        {
          name: "Apple iMac",
          cost: "$499.56",
          image: "data:image/jpeg;base64,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",
        },
        {
          name: "Apple Apple SUPREME GRANDE DELUX, with Cheese, CRISPY!",
          cost: "$499.56",
          image: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAY1BMVEX///9mZmZiYmJgYGBdXV38/PxnZ2f5+fn09PTw8PBubm7l5eVaWlpycnLIyMjZ2dnQ0NCVlZWkpKR5eXmHh4eOjo7V1dW7u7u1tbXLy8utra2IiIjBwcHe3t7q6uqbm5t/f3+qumy+AAAICUlEQVR4nO2daZuzKgyGS8Bda92qtW7//1cenc68M7VKF4Oknt7fy8VTIoQQwm734cOHDx+2h+MdqzjrskZ3R9Tg9OJcX3CAxNPdFxUcsoRxYF9sUGFTuP63uk0qdIpEsL9sTKFRBQBswwrD8/X49UBq6+4VIoULY4GbUuhEt/o2pbBO+IRABpHujmFxDKZGkDEe6+4ZEpU5qa9XmOvuGg57f0YgE7XuvqGwnxtBxnxDd+cwOMzqYyzQ3TkMwvkR3MZE4yXTs+jFSA+6u7ecJpUIZImju3+LMbIbV/TKSN9/osllApl50t2/xRxcmcANOKVOJ/sImSh0d3Ax8aS3/Q//7YcwnHXWLkP49ouhLV0oen/m7QMYlVQf46XuDi6lkTkzPcnbR7sL6VLI/Ep3Bxcjt1HodPdvMZV8CN23n2aMTP4Vvr+N1oFMH99AiK2UGSkk77+nsCfjvz8Cg1B3/5bTSDcVe93dQ2A+ftgP4SZipLJdxdt7a1/MO92itXR3DoVZI4W33zJdsOcUwjZMdLfzpldDYPn7L4QXDpMKIdnAOvjNpEIRvb23/cuEQjA3Y6ED+7FC7sZvv6W/YjSGHNpwSwO4u1IIwMzY25i+IVIKA1yI4NwetuHEXGPl7UCcn+r3Pz+bwfhCdy9ewrAsy3GsZZZnOF59PFw41nVD5QDDrvdF3EZRdD5HUVwcXpv/7TqP27QLmC8GfB4EXdaWe83ugGEf4sQ1GXD4hoPpBu3eeWYwDTss0qGVUQ7m0B4bWrM12bVR5xH3p/a0IERXHh8bSzvMI9PnsviNgLbS4Rjs20TM9ws46/o//14jxzhzJa38iuzild1zu3LZvY4Ni3p2cGYtzKrbgI2TgyWNpSs6QHYVyE85fzvmm/HkZGGFRTdp4ZK2RLRWutspk302YzgkN+Zq59EjxnnTVFCusYA40TP6vuhNLNs339OrYdet+ahx3rTkqv8c99NZvXe7JiDKj43t7cvOf1HeVzugehhL8+XugXC7LIGnLWDczFmlxEaarfVA7xaquzQSqJtwvNcsFBtwVZ1whHeSDFYDzKMSgafXP0FswFQxikfdsv6iwlDDmasRmgCG7YvXtATiz6g2NYG9xAxzXTQiEsvENZgZ/Ua8bKFXhI832+x1a5nGz7BCrrZuKZMAj7E+ROtOyqse+BlvH5XrFjMJ2gD27rY0y0cPvUuDGLM507NRQL02dHww5rQi/Izpsdn0hlC0qJv8nJ4z02Lq29nyCzwa4BFumOZOWvb68BT5bFVylVULECAH2k7UvkIX+f6sIUta1gFgX9w7EnNnIMI+fSqIGSnHPvKmtlTgV8sg5rAB9kJx9zbr6uBfGdKt6BoFN2pCWl8hYtzph5KWQhf92NC6c5FuZRTcD/YS3aKuUHCAfyTldUOGn68pr86xNuge6RDJJ7UaKjj1JeayYe8Lexzdmq6ADF3gziPllKqoJXEkNdH4CpIvaO0NVdSsITaVKricQcpng06BQlIhGmgVpAeT8tmUlBmkpVBB+S9aC76KAmcOqTH8KNyAQgU1M4gpVDCGnm5RV3ys9P0Vqtg80VKowmsjpjDdukLm4u8tiCn0FdxuJ6ZQQRSDlkIVmwtp+b/VgTO+QlJRDBVna7uWlkITv9Q+rWiiinJnxHL2FCRiEEs1YQzdTB1iCjlu4uyOnFPT2yn2dTxyCd4CewdlEVsuGAuw55o7pcXXB/0of09rQRzSvpC/xJDU2cwA9ulFQytVYcDHvfpLLOtrADLcYEZMTiF2rdo9PYXMRd3rewQVQoK6T6Tmtw1wtNvNA9Tuk1woEWcbYlvEHxAT2huaChGforn3MpMuTDSJxFJMfzHRDttkT4VqxY+RZlSv0y1lDoiQNov0XNMfAOl5toroh8iGwh8lxjA6NNeLCzzFuIJBpULbJODGy4eRqFvzAxfFUo0eRe/7L7wrlkVv6MUUx4BY+DVS3AZf4y4TSO0G2y3LA3DUzdRfvGTUxM6gRkC3PKxBK2VhDEbWIq17iGMw6kM6lAcRpVIG0aKJFzjKFfaQ8CAChkB6VWp+wToXPpBdMNCeD6ZXgPYCj7Giw+TKRX2DV4WAXF7GBczjRJpFaJfum/5iURxE3HfYZQ/56kLgZrrRC0lBhJu/Ty/Aj51Ta1GrWY6dl3HvZfv14fiveNE6ahMKbnfblBRiHcxcc6I0neJXp9sNkw0ZibgvP/wSkgnxLw8hzkAlKIWeEP0Pg0ZyBnTqXqIlYqeqHrQaqHSLY2qWwl+MTPuqiF7wekSjW6CC60EjdG8yFJQXHGHoLWsKqfoHyy2tOfzoBa+naHRexDitIFBn5A0wE4Rl6PoUOfq+fpZIi4OKnKgvRcuNIQjWfJq71hBdNNeZZX5Y/2EIUFBnSMrqUXDlvswN6z7HBliZ3c9Qrfgpqt0xzfJsUAO48AfE009zi1bDCH5JfFwcMDc4l1VY9xyKNgjcZ54gL1Zb6cc89swzCDONq/Cql3aYt6kpHvo53gWSFzgG9/b8IHiX15OHDE5dReDfbcBddx286WUrexEewE1zR2ZiVhgHrsxeocM/gnmSfO5JeS6CqHhgO2cd45TNtAFuqWmO+YtX3loacJ/FJ+9RT9kJy8C/HUnwz6G2OeYKr03+2CpwFnTls16y4ZVpYv6ZYIGbKeZrowtx8jYRgvf082ZZvRhqcA5F3Mv8WjTdc6w6qPYkVhPuyzguT96ikLvhNHU4sKyZDx8+fPjw4cP/iv8AOz+Z6/h7NTsAAAAASUVORK5CYII=",
        },
      ]
    }
  }
}
</script>

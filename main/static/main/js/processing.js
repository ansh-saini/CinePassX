

  var loginBtn = document.getElementById('btn-sub');

  loginBtn.addEventListener('click', function(e) {
    e.preventDefault();
    if(localStorage.getItem('isLoggedIn') === 'true'){
      //payments pop up
      console.log(" loged in!!");
    }
      else {
        console.log("not loged in!!");
        document.getElementById('btn-login').click();
      }
  });

window.addEventListener('load', function() {
  var idToken;
  var accessToken;
  var expiresAt;

  var webAuth = new auth0.WebAuth({
    domain: 'dev-d2u-yh5s.au.auth0.com',
    clientID: 'Klq5S1GXDn8vHX00OPflK7CnFQLxZBuE',
    responseType: 'token id_token',
    scope: 'openid',
    redirectUri: window.location.href
  });

  var loginBtn = document.getElementById('btn-login');
  var logoutBtn = document.getElementById('btn-logout');

  loginBtn.addEventListener('click', function(e) {
    e.preventDefault();
        logout();
      displayButtons();
  });

  loginBtn.addEventListener('click', function(e) {
    e.preventDefault();
    if(localStorage.getItem('isLoggedIn') === 'true'){
      console.log("Logging Out");
    logout();
  }
    else{
     webAuth.authorize();
     console.log("Logging in");
   }
    displayButtons();
  });

  function handleAuthentication() {
     webAuth.parseHash(function(err, authResult) {
       if (authResult && authResult.accessToken && authResult.idToken) {
         window.location.hash = '';
         localLogin(authResult);
         loginBtn.style.display = 'none';
       } else if (err) {
         console.log(err);
         alert(
           'Error: ' + err.error + '. Check the console for further details.'
         );
       }
       displayButtons();
     });
   }

  function localLogin(authResult) {
      // Set isLoggedIn flag in localStorage
      localStorage.setItem('isLoggedIn', 'true');
      // Set the time that the access token will expire at
      expiresAt = JSON.stringify(
        authResult.expiresIn * 1000 + new Date().getTime()
      );
      displayButtons();
    }

    function renewTokens() {
      webAuth.checkSession({}, (err, authResult) => {
        if (authResult && authResult.accessToken && authResult.idToken) {
          localLogin(authResult);
        } else if (err) {
          alert(
              'Could not get a new token '  + err.error + ':' + err.error_description + '.'
          );
          logout();
        }
        displayButtons();
      });
    }

    function isAuthenticated() {
        // Check whether the current time is past the
        // Access Token's expiry time
        var expiration = parseInt(expiresAt) || 0;
        return localStorage.getItem('isLoggedIn') === 'true' && new Date().getTime() < expiration;
      }

      function logout() {
    // Remove isLoggedIn flag from localStorage
    localStorage.removeItem('isLoggedIn');
    // Remove tokens and expiry time
    accessToken = '';
    idToken = '';
    expiresAt = 0;
    displayButtons();
  }

      function displayButtons() {
        if (isAuthenticated()) { // logged in
            loginBtn.textContent  = "Log Out";
        } else {
            loginBtn.textContent  = "Log In";
        }
      }

      if (localStorage.getItem('isLoggedIn') === 'true') {
   renewTokens();
 } else {
   handleAuthentication();
 }

});

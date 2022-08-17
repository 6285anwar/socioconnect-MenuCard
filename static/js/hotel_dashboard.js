document.getElementById("facebook").addEventListener("click", function(){
  
    

  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      // The user is logged in and has authenticated your
      // app, and response.authResponse supplies
      // the user's ID, a valid access token, a signed
      // request, and the time the access token 
      // and signed request each expire.
      var uid = response.authResponse.userID;
      var accessToken = response.authResponse.accessToken;
      console.log(accessToken)
    } else if (response.status === 'not_authorized') {
      FB.login(function(response) {
        if (response.authResponse) {
         console.log('Welcome!  Fetching your information.... ');
         var accessToken = response.authResponse.accessToken;
        console.log(accessToken)
        } else {
         console.log('User cancelled login or did not fully authorize.');
        }
    });
      // The user hasn't authorized your application.  They
      // must click the Login button, or you must call FB.login
      // in response to a user gesture, to launch a login dialog.
    } else {
      FB.login(function(response) {
        if (response.authResponse) {
         console.log('Welcome!  Fetching your information.... ');
         var accessToken = response.authResponse.accessToken;
      console.log(accessToken)
        } else {
         console.log('User cancelled login or did not fully authorize.');
        }
    });
      // The user isn't logged in to Facebook. You can launch a
      // login dialog with a user gesture, but the user may have
      // to log in to Facebook before authorizing your application.
    }
   });
    
}
)
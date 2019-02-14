<html>
  <head></head>
  <body>
    <script>

    function makeApiCall() {
      var params = {
          q: "name='STemplate'"
        };
      gapi.client.load('drive', 'v2', function(){
         var request = gapi.client.drive.files.list();
         request.execute(function(resp) {
            for (var i = resp.items.length - 1; i >= 0; i--) {
               if(resp.items[i].title == 'STemplate') {
                  console.log(resp.items[i]);
                  id = resp.items[i].id;
                  console.log(id); 
                  templ = gapi.client.drive.files.copy({fileId:id}).execute(null);
                  console.log(templ);

                  break;
               }
            }
            
         });
      });
    }

  

    function initClient() {
      var API_KEY = 'AIzaSyD9r5xxQlsTASup8TzVbbClYmbfLXBFU9I';

      var CLIENT_ID = '417920485847-rd5mt3mvncf2iqv7nbbr6km2aammng70.apps.googleusercontent.com';

      //   'https://www.googleapis.com/auth/drive'
      //   'https://www.googleapis.com/auth/drive.file'
      //   'https://www.googleapis.com/auth/drive.readonly'
      //   'https://www.googleapis.com/auth/spreadsheets'
      //   'https://www.googleapis.com/auth/spreadsheets.readonly'
      var SCOPE = 'https://www.googleapis.com/auth/spreadsheets https://www.googleapis.com/auth/drive';

      gapi.client.init({
        'apiKey': API_KEY,
        'clientId': CLIENT_ID,
        'scope': SCOPE,
        'discoveryDocs': ['https://sheets.googleapis.com/$discovery/rest?version=v4'],
      }).then(function() {
        gapi.auth2.getAuthInstance().isSignedIn.listen(updateSignInStatus);
        updateSignInStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
      });
    }

    function handleClientLoad() {
      gapi.load('client:auth2', initClient);
    }

    function updateSignInStatus(isSignedIn) {
      if (isSignedIn) {
        //makeApiCall();
      }
    }

    function handleSignInClick(event) {
      gapi.auth2.getAuthInstance().signIn();
    }

    function handleSignOutClick(event) {
      gapi.auth2.getAuthInstance().signOut();
    }
    </script>
    <script async defer src="https://apis.google.com/js/api.js"
      onload="this.onload=function(){};handleClientLoad()"
      onreadystatechange="if (this.readyState === 'complete') this.onload()">
    </script>
    <button id="signin-button" onclick="handleSignInClick()">Sign in</button>
    <button id="signout-button" onclick="handleSignOutClick()">Sign out</button>
    <button id="signout-button" onclick="makeApiCall()">CreateSlide</button>
    <div style="margin-left:auto; margin-right:auto; width:960px;">
   
  </body>
</html>
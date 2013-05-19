// this needs to be a singleton because we only create one instance of
// this object, when the user logs in
define(function() {
	   var loginSingleton = function() {
	       var self = this;
	       self.pk = ko.observable();
	       self.username = ko.observable();
	       self.userFirstName = ko.observable();
	       self.userLastName = ko.observable();
	       self.name = ko.computed(function() {
					   return self.userFirstName() + " " +
					       self.userLastName();
				       });
	       // server resources; this will contain the JSON returned
	       // by calling the api root; this is where we'll be searching
	       // for urls.
	       self.resources = ko.observable();
	       self.init = function() {
		   // make a GET request to the api root to get
		   // info about the logged in user and available
		   // server resources (URIs)
		   $.ajax({
			      url: '/api/?format=json',
			      dataType: 'json',
			      success: function(response) {
				  self.pk(response["user-id"]);
				  self.username(response["user-username"]);
				  self.userFirstName(response["user-firstname"]);
				  self.userLastName(response["user-lastname"]);
				  self.resources(response);
			      },
			      error: function(jqXHR, textStatus, errorThrown) {
				  humane.log("There was an error retrieving user information. Please try refreshing the page.");
			      }
			  });
	       };
	   };
	   return new loginSingleton();
       });
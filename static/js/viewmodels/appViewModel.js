// there is always only one AppViewModel, so we need
// to make this a singleton
define(['viewmodels/loginViewModel',
	'viewmodels/s3ViewModel'],
       function(LoginViewModel, S3ViewModel) {
	   var appSingleton = function() {
	       var self = this;
	       self.login = ko.observable(LoginViewModel);
	       // this is what we'll bind to the S3 file upload template
	       self.s3 = ko.observable(new S3ViewModel());

	       // METHODS

	       // initializes the objects
	       self.init = function() {
		   self.login().init();
	       };
	   };
	   return new appSingleton();
       });
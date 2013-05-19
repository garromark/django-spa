// Defines a viewmodel for a new S3 file upload form.
define(['viewmodels/loginViewModel',
	'mimetypes'],
       function(LoginViewModel, Mimetypes) {
	   return function S3ViewModel(options) {
	       // OPTIONS:
	       // filesRe = a regular expression indicating the acceptable extensions for the
	       //           files to upload
	       // folder = the S3 folder where we're uploading said files
	       // label = the label to show in the upload template
	       var self = this;
	       // settings
	       self.settings = ko.observable($.extend({filesRe: "png", folder: "uploads", label: ""},
						      options));
	       // the action URL for th upload form
	       self.actionUrl = ko.observable();
	       // the S3 bucket where this is going
	       self.bucket = ko.observable();
	       // AWS access key
	       self.accessKey = ko.observable();
	       // policy, as computed by the backend (base64)
	       self.policy = ko.observable();
	       self.signature = ko.observable();
	       // the name of the file to upload
	       self.fileName = ko.observable();
	       // the mimetype of this object;
	       self.mimetype = ko.observable();
	       // the S3 url where the file was uploaded
	       self.s3Url = ko.observable();
	       // S3 success-action-status
	       self.successActionStatus = ko.observable();
	       // container for S3 data - this will come from the fileupload plugin
	       self.data = ko.observable();
	       // the label to use on the form
	       self.label = ko.observable();

	       // METHODS

	       // This method to be used after rendering an s3_form template.
	       self.init = function(elements) {
		   $form = undefined;
		   for (eIndex in elements) {
		       if (elements[eIndex].nodeName.toLowerCase() == "form") {
			   $form = $(elements[eIndex]);
			   break;
		       }
		   }
		   if ($form) {
		       $form.
			   fileupload({
					  autoUpload: false,
					  acceptFileTypes: self.settings().filesRe,
					  maxFileSize: 5000000, // 5MB in metric system
					  add: function(event, data) {
					      // retrieve S3 specific form inputs
					      $.ajax({
							 url: LoginViewModel.resources()["s3-form"],
							 type: "GET",
							 dataType: "json",
							 data: {"folder" : self.settings().folder},
							 async: false,
							 success: function(response) {
							     self.bucket(response["bucket"]);
							     self.accessKey(response["accessKey"]);
							     self.policy(response["policy"]);
							     self.signature(response["signature"]);
							     self.actionUrl(response["actionUrl"]);
							     self.successActionStatus(response["successActionStatus"]);
							     // this is ugly - needs to be fixed
							     $form.attr('action', self.actionUrl());
							 },
							 error: function(jqXHR, textStatus, errorThrown) {
							     humane.log("An error occurred. Please try again.");
							 }
						     });
					      if (data.files.length > 0) {
						  self.fileName(data.files[0].name);
						  // set the mimetype
						  var ext = self.fileName().split('.');
						  if (ext.length > 0) {
						      self.mimetype(Mimetypes[ext[1]]);
						  }
					      }
					      self.data(data);
					  }
				      });
		   };

	       };
	   };
       });
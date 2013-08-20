if(_baseAppViewModel === undefined)
    _baseAppViewModel = 'viewmodels/appViewModel';
require([_baseAppViewModel, 'domReady!'],
	function(avm) {
	    // setup infuser to find our templates
	    // all our knockout templates have the suffix tmpl.html
	    infuser.defaults.templateSuffix = ".tmpl.html";
	    infuser.defaults.templateUrl = "static/templates";
	    ko.applyBindings(avm);
	    avm.init();
	});
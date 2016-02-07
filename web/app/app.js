var TIMEOUT = 1000;
var RESOURCE = '//localhost:5000';

(function(app) {
	document.addEventListener('DOMContentLoaded', function() {
		appComponent = ng.core.Component({
			selector: 'smack-app',
			templateUrl: 'app/app.html',
			directives: [Meter, History],
			providers: [ng.http.HTTP_PROVIDERS]
		})
		.Class({
			constructor: function(){}
		});

		// Start the app
		ng.platform.browser.bootstrap(appComponent);
	});
})(window.app || (window.app = {}));
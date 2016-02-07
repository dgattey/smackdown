(function(app) {
	document.addEventListener('DOMContentLoaded', function() {
		appComponent = ng.core.Component({
			selector: 'smack-app',
			templateUrl: 'app/app.html',
			directives: [Meter, History]
		})
		.Class({
			constructor: function() {}
		});

		// Start the app
		ng.platform.browser.bootstrap(appComponent);
	});
})(window.app || (window.app = {}));
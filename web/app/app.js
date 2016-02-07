var TIMEOUT = 2000;
var RESOURCE = '//smackdown.herokuapp.com';

(function(app) {
	document.addEventListener('DOMContentLoaded', function() {
		appComponent = ng.core.Component({
			selector: 'smack-app',
			templateUrl: 'app/app.html',
			directives: [Meter, History, Tweets],
			providers: [ng.http.HTTP_PROVIDERS]
		})
		.Class({
			constructor: function(){
				this.live = 'Live Matchup!';
			}
		});

		// Start the app
		ng.platform.browser.bootstrap(appComponent);
	});
})(window.app || (window.app = {}));
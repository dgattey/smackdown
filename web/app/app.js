(function(app) {
	document.addEventListener('DOMContentLoaded', function() {
		appComponent = ng.core.Component({
			selector: 'smack-app',
			templateUrl: 'app/app.html',
			directives: [Meter, History],
			providers: [ng.http.HTTP_PROVIDERS]
		})
		.Class({
			constructor: [ng.http.Http, function(Http) {
				setInterval(function() {
					var text = Http.get('//localhost:5000/score')
					.map(function(res){
						return res.text();
					}).subscribe(function(result){
						console.log(result);
					});
				}, 1000);
			}]
		});

		// Start the app
		ng.platform.browser.bootstrap(appComponent);
	});
})(window.app || (window.app = {}));
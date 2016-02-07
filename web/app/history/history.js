var History =
  ng.core.Component({
    selector: 'recent-history',
    templateUrl: 'app/history/history.html'
  })
  .Class({
    constructor: [ng.http.Http, function(Http) {
		this.startPolling(Http); // starts async requests for new values
	}],

	startPolling: function(Http) {
		var self = this;
		setInterval(function() {
			var text = Http.get(RESOURCE+'/history')
			.map(function(res){return res.text();})
			.subscribe(function(value){
				console.log(value);
			});
		}, TIMEOUT);
	}
  });
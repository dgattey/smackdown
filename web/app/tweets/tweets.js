var Tweets = ng.core.Component({
	selector: 'tweets',
	templateUrl: 'app/tweets/tweets.html'
})
.Class({
	constructor: [ng.http.Http, function(Http) {
		this.getTweets(Http);
	}],

	getTweets: function(Http) {
		var self = this;
		setInterval(function() {
			Http.get(RESOURCE+'/lastTweets')
			.map(function(res){
				return Array.from(new Set(res.json()));
			})
			.subscribe(function(value){
				self.tweets = value;
			});
		}, TIMEOUT);
	}
});
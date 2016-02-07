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
		Http.get(RESOURCE+'/lastTweets')
		.map(function(res){return res.json();})
		.subscribe(function(value){
			console.log(value);
		});
	}
});
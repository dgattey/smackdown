var HEIGHT = 200;
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
			var svg = document.getElementById('svg');
			var polyline= document.getElementById('history-poly');
			var text = Http.get(RESOURCE+'/history')
			.map(function(res){
				polyline.points.clear();
				var json = res.json();
				for (var i = 0; i < json.length; i++) {
					var point = svg.createSVGPoint();
					point.x = (new Date().getTime() - (json[i].time*1000))/700;
					point.y = json[i].score * HEIGHT/100;
					polyline.points.appendItem(point);
				}

				return Array.from(json);
			})
			.subscribe(function(arr){
				self.history = arr;
			});
		}, TIMEOUT);
	}
  });
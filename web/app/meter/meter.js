var Meter = ng.core.Component({
	selector: 'recent-meter',
	template: '<h3>{{label}} {{status}}</h3><p id="left">{{teams[0]}}</p><p id="right">{{teams[1]}}</p>'
})
.Class({
	constructor: [ng.http.Http, function(Http) {
		this.startPolling(Http); // starts async requests for new values
		this.getTeamInfo(Http);
		this.teams = [];
		this.min = 0.0;
		this.max = 100.0;
		var val = 50;
		this.config = {
			texts: ['WHOA!', 'Woo!', 'Boring.', 'Well well!', 'Going DOWN!'],
			colors: ['#ff671a', '#555555', '#42acff']
		};
		this.dial = new JustGage({
			id: 'dial',
			value: val,
			min: this.min,
			max: this.max,
			hideMinMax: true,
			hideValue: true,
			pointer: true,
			levelColors: this.config.colors
		});
		this.changeValue(val);
	}],

	getTeamInfo: function(Http) {
		var self = this;
		Http.get(RESOURCE+'/info')
		.map(function(res){return res.json();})
		.subscribe(function(value){
			self.teams[0] = value.team1.desc;
			self.teams[1] = value.team2.desc;
		});
	},

	scaleValue: function(rawValue, min, max) {
		var val = rawValue - min;
		var range = max - min;
		return val/range;
	},

	startPolling: function(Http) {
		var self = this;
		setInterval(function() {
			var text = Http.get(RESOURCE+'/score')
			.map(function(res){return res.text();})
			.subscribe(function(value){
				self.changeValue(value);
			});
		}, TIMEOUT);
	},

	setStatus: function(segment) {
		if (segment == 2) this.status = 'No team has an edge.';
		else {
			var team = (segment > 2 ? this.teams[1] : this.teams[0]);
			this.status = team+' are getting smacked!';
		}
	},

	changeValue: function(value) {
		var percent = this.scaleValue(value, this.min, this.max);
		var i = Math.ceil(percent * this.config.texts.length - 1);
		if (i < 0) i = 0;

		this.dial.refresh(value);
		this.label = this.config.texts[i];
		this.setStatus(i);
	}
});
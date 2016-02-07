var Meter = ng.core.Component({
	selector: 'recent-meter',
	template: '<h3>{{label}} {{status}}</h3>'
})
.Class({
	constructor: [ng.http.Http, function(Http) {
		this.startPolling(Http); // starts async requests for new values
		this.getTeamInfo(Http);
		this.min = 0.0;
		this.max = 100.0;
		var val = 50;
		this.config = {
			texts: ['WHOA!', 'Woo!', 'Boring.', 'Well well!', 'Going DOWN!'],
			colors: ['#ff3433', '#0077ff', '#7fff90', '#0077ff', '#ff3433']
		};
		this.dial = new JustGage({
			id: 'dial',
			value: val,
			min: this.min,
			max: this.max,
			hideMinMax: true,
			hideValue: true,
			pointer: true,
			levelColors: this.config.colors,
			label: 'Live matchup!'
		});
		this.changeValue(val);
	}],

	getTeamInfo: function(Http) {
		var self = this;
		Http.get(RESOURCE+'/info')
		.map(function(res){return res.json();})
		.subscribe(function(value){
			self.teams = [];
			self.teams[0] = value[0].desc;
			self.teams[1] = value[1].desc;
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
			var team = (segment > 2 ? this.teams[0] : this.teams[1]);
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
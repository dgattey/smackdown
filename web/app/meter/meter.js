var Meter = ng.core.Component({
	selector: 'recent-meter',
	template: '<h3>{{label}} {{status}}</h3>'
})
.Class({
	scaleValue: function(rawValue, min, max) {
		var val = rawValue - min;
		var range = max - min;
		return val/range;
	},

	constructor: function() {
		this.min = -100.0
		this.max = 100.0
		var val = 50;
		this.label = 'HEHE';
		this.teams = ['Denver Broncos', 'Carolina Panthers'];
		this.config = {
			texts: ['WHOA!', 'Woo!', 'Boring.', 'Well well!', 'Going DOWN!'],
			colors: ['#ff3433', '#0077ff', '#7fff90', '#0077ff', '#ff3433']
		}
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
	},

	setStatus: function(segment) {
		if (segment == 2) this.status = 'no team has an edge.';
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
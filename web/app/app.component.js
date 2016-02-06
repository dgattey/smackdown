(function(app) {
    app.AppComponent = ng.core.Component({
        selector: 'smack-app',
        template: '<svg height="100" width="100"><circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red"/></svg>'
    })
    .Class({
        constructor: function() {}
    });
})(window.app || (window.app = {}));

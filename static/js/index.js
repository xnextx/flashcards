var React = require('react')
var ReactDOM = require('react-dom')

var Hello = React.createClass ({
    render: function() {
        return (
            <h1>
            Webpack + React + Django works!
            </h1>
        )
    }
})

ReactDOM.render(<Hello />, document.getElementById('container'))
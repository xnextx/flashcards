import React from "react";


export default React.createClass({
    render: function() {
        return (
            <div className="greeting">
                Witam, {this.props.name}!
            </div>
        );
    },
});
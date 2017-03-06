var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry: [
        './static/js/index.js',
        'webpack-dev-server/client?http://localhost:8080/', 'webpack/hot/only-dev-server',
    ],
    output: {
        path: path.resolve('./static/js/build/'),
        filename: "build.js",
        publicPath: 'http://localhost:8080/static/js/build/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name

    },

    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin(),
        new BundleTracker({filename: './webpack-stats.json'})
    ],
    devtool: 'source-map',

    module: {
        loaders: [
            {
                test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader',
                query: {
                    cacheDirectory: true,
                    presets: ['es2015', "stage-0", 'react']
                }
            }
        ]
    }

};
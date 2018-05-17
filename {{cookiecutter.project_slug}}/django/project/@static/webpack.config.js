var webpack = require("webpack");
var path = require("path");
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var BundleTracker = require("webpack-bundle-tracker");
var CopyWebpackPlugin = require('copy-webpack-plugin');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin')

/**
 * Webpack Docs:
 * - https://webpack.js.org/configuration/
 * - https://webpack.js.org/guides/migrating/ (1.x -> 2.x)
 */


var publicPath = '/static/';

var config = {
    context: path.resolve(__dirname),
    entry: {
        "js/common": "entry_points/js/index.js",
        "css/styles": "entry_points/scss/styles.scss",
        "css/ui_kit": "entry_points/scss/styles_ui_kit.scss",
    },
    output: {
        path: path.resolve(__dirname, "../static"),
        filename: "[name].js",
        publicPath: publicPath,
        chunkFilename: "[id].chunck.[ext]"
    },
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: "js/common",
            filename: "js/common.js"
        }),
        new ExtractTextPlugin({ filename: "[name].css" }),
        new webpack.ProvidePlugin({
            "fetch": "imports?this=>global!exports?global.fetch!whatwg-fetch",
            "Promise": "bluebird",
            "$": "jquery",              // bootstrap.js support
            "jQuery": "jquery",         // bootstrap.js support
        }),
        // SEE: https://github.com/kevlened/copy-webpack-plugin
        new CopyWebpackPlugin([
            // "to" scope starts in static/
            // { "from": "@copy/path/to/file.ext", "to": "desired/path/to/file.ext"},
            { "from": "@copy/taggit_autosuggest/taggit-autosuggest.css", "to": "css/taggit-autosuggest.css" },
            { "from": "@copy/taggit_autosuggest/taggit-autosuggest.js", "to": "js/jquery.autoSuggest.minified.js" },
        ]),
        // TODO: maybe pass browser sync as a flag/option
        new BrowserSyncPlugin({
            host: "localhost",
            port: 8001,
            proxy: "127.0.0.1:8000",
            files: [
                "./static/css/*.css",
                "./static/js/*.js",
                "../app/ui/templates/ui/**/*.html",
                "../app/ui_kit/templates/ui_kit/**/*.html",
                "../app/ui_kit/templates/ui_kit/**/*.html"
            ],
            reloadDelay:300,
            reloadDebounce: 500
        })
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: "css-loader"
                })
            },
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({
                    use: [{
                        loader: "css-loader"
                    }, {
                        loader: "sass-loader",
                        options: {
                            data: "$staticUrl: '" + publicPath + "';"
                        }
                    }]
                })
            },
            {
                test: /\.tsx?/,
                exclude: /node_modules/,
                use: "ts-loader"
            },
            {
                test: /\.(png|gif|jpe?g|svg)$/i,
                use: [
                    {
                        loader: "file-loader",
                        options: {
                            name: "imgs/[name].[ext]",
                        }
                    }
                ]
            },
            {
                test: /\.(woff2?|eot|ttf)(\?\S*)?$/,
                exclude: [],
                use: [
                    {
                        loader: "file-loader",
                        options: {
                            name: "fonts/[name].[ext]",
                        }
                    }
                ]
            },
            {
                test: /\.(njk|nunjucks)$/,
                exclude: /node_modules/,
                use: {
                    loader: "nunjucks-loader",
                    options: {
                        config: path.resolve(__dirname, "nunjucks.config.js")
                    }
                }
            }
        ]
    },
    devtool: "source-map",
    resolve: {
        extensions: [".webpack.js", "web.js", ".ts", ".tsx", ".js"],
        alias: {
            "webworkify": "webworkify-webpack",
            "bootstrap_scss": "bootstrap/scss",
            "chosen": "chosen-js",
            "breakpoint": "breakpoint-sass/stylesheets",
            "bourbon": "bourbon/core",
        },
        modules: ["node_modules", "js", "scss", "./"]
    }

}

if (process.env.WEBPACK_ENV == 'production') {
    config.plugins = config.plugins.concat([
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                screw_ie8: true,
                warnings: false,
                unsafe_comps: true,
                unsafe: true,
                pure_getters: true
            },
            comments: false,
            sourceMap: true
        })
    ])

    config.module.rules = config.module.rules.concat([
        {
            test: /\.(js|ts)$/,
            loader: "webpack-strip?strip[]=console.warn,strip[]=console.log"
        },
    ])
}

module.exports = config

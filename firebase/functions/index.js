const admin = require('firebase-admin');
admin.initializeApp();

exports.searchGiphy = require('./searchGiphy');
exports.setScreens = require('./setScreens');
exports.slackIncomingMessage = require('./slackIncomingMessage');

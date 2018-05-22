const admin = require('firebase-admin');
admin.initializeApp();

exports.searchGiphy = require('./searchGiphy');
exports.slackIncomingMessage = require('./slackIncomingMessage');

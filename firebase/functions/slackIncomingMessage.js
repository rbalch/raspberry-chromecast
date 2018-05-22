const functions = require('firebase-functions');


module.exports = functions.https.onRequest((req, res) => {
  return res.status(200).send('Message Received!');
});

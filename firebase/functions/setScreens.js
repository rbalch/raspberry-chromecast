const admin = require('firebase-admin');
const functions = require('firebase-functions');


module.exports = functions.https.onRequest((req, res) => {
  const db = admin.firestore();
  const dataRef = db.collection('huge_cast').doc('cast_1');

  dataRef.get()
    .then(doc => {
      return doc.data();
    })
    .then(doc => {
      const query = req.query.query || doc.value;
      const query_type = req.query.type || 'text';
      if (query !== doc.value) {
        doc = {value: query, type: query_type};
        dataRef.set(doc, {merge: true});
      }
      return doc
    })
    .then(doc => {
      return res.status(200).send(doc);
    })
    .catch((err) => {
      console.log(err);
      return res.status(500).end();
    });
});

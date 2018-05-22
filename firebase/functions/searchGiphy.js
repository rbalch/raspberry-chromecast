const admin = require('firebase-admin');
const functions = require('firebase-functions');
const GphApiClient = require('giphy-js-sdk-core');
const client = GphApiClient("kyrzItAJkKe0679M4WtNGQaoj7OK1ep6")


module.exports = functions.https.onRequest((req, res) => {
  const db = admin.firestore();
  const castRef = db.collection('giphy').doc('castScreens');

  castRef.get()
    .then(doc => {
      return doc.data()
    })
    .then(doc => {
      const searchTerm = req.query.q || doc.searchTerm;
      if (searchTerm !== doc.searchTerm) {
          castRef.set({searchTerm: searchTerm}, {merge: true})
      }
      return searchTerm
    })
    .then(searchTerm => {
      const giphyOptions = {
        "q": searchTerm,
        "limit": 40,
        "offset": Math.floor(Math.random() * 31),
        "rating": "g",
        "lang": "en",
      };

      return client.search('gifs', giphyOptions)
    })
    .then((response) => {
        const giphyUrl = response.data[Math.floor(Math.random() * response.data.length)].images.original.mp4_url;
        console.log(giphyUrl);
        return giphyUrl
    })
    .then((giphyUrl) => {
      return castRef.set({giphyUrl: giphyUrl}, {merge: true})
    })
    .then(() => {
      console.log('Write succeeded!');
      return res.status(200).send('Gif Refreshed!');
    })
    .catch((err) => {
      console.log(err);
      return res.status(500).end();
    })
});

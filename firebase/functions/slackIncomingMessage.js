const admin = require('firebase-admin');
const functions = require('firebase-functions');


module.exports = functions.https.onRequest((req, res) => {
    console.log(req.body);
    const db = admin.firestore();
    const dataRef = db.collection('huge_cast').doc('cast_1');
    res.setHeader('Content-Type', 'application/json');

    let message = req.body.text;
    let content_type = getContentType(message);

    // Update Database
    let data = {
        value: message,
        type: content_type
    };
    dataRef.set(data);

    // Response
    let text = getResponseText(content_type, req.body.user_name);
    let payload = {
        text: text
    };
    res.send(JSON.stringify(payload, null, 3));
});


function getContentType(value){
    const pattern = "(ftp|http|https):\\/\\/(\\w+:{0,1}\\w*@)?(\\S+)(:[0-9]+)?(\\/|\\/([\\w#!:.?+=&%@!\\-\\/]))?";
    const re = new RegExp(pattern);
    const imageTypes= ['jpeg', 'jpg', 'gif', 'png', 'bmp'];
    const videoTypes= ['mp4'];

    if (re.exec(value) && value.indexOf('.') > -1) {
        const ext = value.split('.').pop().toLowerCase();
        if (imageTypes.indexOf(ext) > -1) return "image";
        if (videoTypes.indexOf(ext) > -1) return "video";
    }
    return "text"
}


function getResponseText(content_type, user_name) {
    const generalArray = [
        `Good choice ${user_name}!`,
        'Do I really have to share that with everyone....fine',
        `Look at ${user_name}, causing some trouble`,
        `I'm taking credit for this.`,
        `${user_name} always has the best posts.`,
    ];

    const textArray = [
        `Is that a spelling error? Just kidding ${user_name}!`,
        `Spoken like a true word smith.`,
    ];
    const imageArray = [
        `A work of art. :)`,
        `I'm hanging this picture on the fridge.`,
    ];

    const videoArray = [
        `*Grabs Popcorn*`,
        `I couldn't find a loading animation so you some dots ........`,
    ];

    let resp = generalArray;
    if (content_type === 'text') resp = generalArray.concat(textArray);
    if (content_type === 'image') resp = generalArray.concat(imageArray);
    if (content_type === 'video') resp = generalArray.concat(videoArray);

    const i = Math.floor(Math.random()*resp.length);
    return resp[i]

}
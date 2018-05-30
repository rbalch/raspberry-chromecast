# raspberry-chromecast
Scripts for having a Raspberry Pi takeover chromecast screens

python -m http.server


# Firebase
## Login
```bash
firebase login
```
## Alias
```bash
firebase use -add
```

## Serve

### CLoud functions
```bash
firebase serve --only functions -p 5001
```

## Deploy

### Single function
```bash
firebase deploy --only functions:slackIncomingMessage
```

### Host
```bash
firebase deploy --only hosting
```
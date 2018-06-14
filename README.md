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

### Setting up local environment variables
```
firebase functions:config:set XXX.username="XXX" XXX.password="XXX"
# inside functions folder for local dev:
firebase functions:config:get > .runtimeconfig.json
```

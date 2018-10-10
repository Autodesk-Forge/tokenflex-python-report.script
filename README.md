# forge-consumption-reporting-sample

## Description

A Forge Python script used to download Autodesk consumption data. The scripts are designed to communicate with Autodesk and  the Forge Consumption Reporting API. 

[![License](http://img.shields.io/:license-mit-blue.svg)](http://opensource.org/licenses/MIT)

### Thumbnail

![Screenshot](https://github.com/mazerab/forge-consumption-reporting-sample/blob/master/docs/Python%20Script.png)

### Live Version

See [video demonstration](https://www.youtube.com/watch?v=746hxnvlQ1g)

## Setup

This samples requires Forge and respective client credentials.

### Pre-requisites

For using this sample, you need an Autodesk developer credentials. Visit the [Forge Developer Portal](https://developer.autodesk.com), sign up for an account, then [create an app](https://developer.autodesk.com/myapps/create). For this new app, use `http://localhost:3000/forge/oauth/callback` as Callback URL. Finally take note of the **Client ID** and **Client Secret**. For localhost testing:

- FORGE\_CLIENT\_ID
- FORGE\_CLIENT\_SECRET
- FORGE\_CALLBACK\_URL

### Running locally

Make sure to have [Python 2.7](https://www.python.org/downloads/release/python-278/) installed. Clone this project or download it. It's recommended to install [GitHub desktop](https://desktop.github.com). To clone it via command line, use the following (Terminal on MacOSX/Linux, Git Shell on Windows):

```
git clone https://github.com/mazerab/forge-consumption-reporting-sample
```

Launch a terminal with two tabs:

On first tab, 
- change directory to the repository you just downloaded locally
- run the command 

```
python simple_http_server.py --FORGE_CLIENT_ID=<your Forge ID> --FORGE_CLIENT_SECRET=<your Forge secret> --FORGE_CALLBACK_URL=http://localhost:3000/forge/oauth/callback
```

On second tab,
- change directory to the same repository folder
- run the command

```
python consumption_reporting.py --FORGE_CLIENT_ID=<your Forge ID> --FORGE_CLIENT_SECRET=<your Forge secret> --FORGE_CALLBACK_URL=http://localhost:3000/forge/oauth/callback
```

- when prompted to browse to authorization url, right-click ```open URL```
- sign-in to Autodesk with your Autodesk ID & grant access
- when asked if you've granted access, answer ```yes```
- go back to first tab
- copy the access token value from terminal
- go back to second tab
- when asked to input access token value, paste the value from clipboard
- you should see contract details

### Deployment

## Further Reading

### Troubleshooting

If running into errors while running the script, on the terminal shell, use the following to confirm the version of Python:

    python --version

### License

This sample is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT). Please see the [LICENSE](LICENSE) file for full details.


### Authors

Autodesk Premium Support Services

- Bastien Mazeran [@BastienMazeran](https://twitter.com/BastienMazeran)

See more at [Forge blog](https://forge.autodesk.com/blog).

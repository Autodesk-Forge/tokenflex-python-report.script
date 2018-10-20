# forge-consumption-reporting-sample

[![Build Status](https://travis-ci.org/dukedhx/tokenflex-reporting-python-script.svg?branch=master)](https://travis-ci.org/dukedhx/tokenflex-reporting-python-script)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://opensource.org/licenses/MIT)
[![pep8](https://img.shields.io/badge/code%20style-pep8-blue.svg)](https://www.python.org/dev/peps/pep-0008/)
[![codebeat badge](https://codebeat.co/badges/d9440870-9122-460b-8b9a-3d1b29d46ed2)](https://codebeat.co/projects/github-com-dukedhx-tokenflex-reporting-python-script-master)
[![Maintainability](https://api.codeclimate.com/v1/badges/4f6821a3553efcc2167d/maintainability)](https://codeclimate.com/github/dukedhx/tokenflex-reporting-python-script/maintainability)
[![gitter](https://camo.githubusercontent.com/20d7543bc8280bf8134b686c46c7b7e2c0a467fd/68747470733a2f2f6261646765732e6769747465722e696d2f67697474657248512f6769747465722e706e67)](https://gitter.im/autodesk-forge-core)

## Description

A Forge Python script used to download Autodesk consumption data. The scripts are designed to communicate with Autodesk and  the Forge Consumption Reporting API.

### Thumbnail

![Screenshot](https://github.com/mazerab/forge-consumption-reporting-sample/blob/master/docs/Python%20Script.png)

### Live Version

See [video demonstration](https://www.youtube.com/watch?v=746hxnvlQ1g)

## Setup

Clone this project or download it. It's recommended to install [GitHub desktop](https://desktop.github.com). To clone it via command line, use the following (Terminal on MacOSX/Linux, Git Shell on Windows):

```bash
git clone https://github.com/mazerab/forge-consumption-reporting-sample
```

Make sure to have [Python 2.7](https://www.python.org/downloads/release/python-278/) installed.

*Optional: Set up and use [virtualenv](https://virtualenv.pypa.io/en/stable/) to test this sample under isolated dependency environment*

Install dependencies via [pip](https://pip.pypa.io/en/stable/installing/):

```bash
pip install -r requirements.txt
```

### Pre-requisites

For using this sample, you need an Autodesk developer credentials. Visit the [Forge Developer Portal](https://developer.autodesk.com), sign up for an account, then [create an app](https://developer.autodesk.com/myapps/create) with access to **Token Flex Usage Data API**. For this new app, use `http://localhost:3000/any/path/takes/your/fancy` as Callback URL. Finally take note of the **Client ID** and **Client Secret**. For localhost testing:

- FORGE\_CLIENT\_ID
- FORGE\_CLIENT\_SECRET
- FORGE\_CALLBACK\_URL

### Running Locally

Linux/Unix:
```bash
chmod u+x start.py # Run once for executive permission
./start.py  --FORGE_CLIENT_ID=YOUR_FORGE_CLIENT_ID --FORGE_CLIENT_SECRET=YOUR_FORGE_CLIENT_SECRET --FORGE_CALLBACK_URL=YOUR_FORGE_CALLBACK_URL
```

Other Platforms:
```
python2.7 start.py --FORGE_CLIENT_ID=YOUR_FORGE_CLIENT_ID --FORGE_CLIENT_SECRET=YOUR_FORGE_CLIENT_SECRET --FORGE_CALLBACK_URL=YOUR_FORGE_CALLBACK_URL
```

### Debug Options

Optional environment variables (leave empty for default values):

- FORGE_TOKEN_URL
- FORGE_BASE_URL
- FORGE_TOKENFLEX_URL
- FORGE_AUTH_PATH

### Deployment

Since we are dealing with Python scripts, there is no deployment needed, simply copy the Python script to your local machine and run the scripts from that location.

## Further Reading

### Troubleshooting

If running into errors while running the script, on the terminal shell, use the following to confirm the version of Python:

    python --version

### License

This sample is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT). Please see the [LICENSE](LICENSE) file for full details.


### Authors

Autodesk Premium Support Services

- Bastien Mazeran [@BastienMazeran](https://twitter.com/BastienMazeran)
- Bryan Huang [LinkedIn](https://linkedin.com/in/bryan-huang-1447b862)

See more at [Forge blog](https://forge.autodesk.com/blog).

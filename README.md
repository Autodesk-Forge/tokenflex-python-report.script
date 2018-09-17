# forge-consumption-reporting-sample
A Forge sample

[![License](http://img.shields.io/:license-mit-blue.svg)](http://opensource.org/licenses/MIT)

![Screenshot](https://github.com/mazerab/forge-consumption-reporting-sample/blob/master/docs/Python%20Script.png)

## Demonstration

See [video demonstration]()

**Usage**: select 

## Architecture

The app was designed to communicate with Autodesk and respective Forge APIs. 

## Setup

This samples requires Forge and respective client credentials.

### Forge

For using this sample, you need an Autodesk developer credentials. Visit the [Forge Developer Portal](https://developer.autodesk.com), sign up for an account, then [create an app](https://developer.autodesk.com/myapps/create). For this new app, use `http://localhost:3000/forge/oauth/callback` as Callback URL. Finally take note of the **Client ID** and **Client Secret**. For localhost testing:

- FORGE\_CLIENT\_ID
- FORGE\_CLIENT\_SECRET
- FORGE\_CALLBACK\_URL

## Running locally

Make sure to have [NodeJS](https://nodejs.org) installed. Clone this project or download it. It's recommended to install [GitHub desktop](https://desktop.github.com). To clone it via command line, use the following (Terminal on MacOSX/Linux, Git Shell on Windows):

```
git clone https://github.com/mazerab/forge-koa-vue-passport-boilerplate
```

Set all FORGE_ aenvironment variables described on the **Setup** section using the following:

- Mac OSX/Linux (Terminal)

```
export VARIABLE_NAME=value
```

- Windows (use <b>Node.js command line</b> from Start menu)

```
set VARIABLE_NAME=value
```

## Deployment

The first step is to download the Git repository to a local directory on your machine. 

### Setup

Test


## Troubleshooting

If running into errors while running the script, on the terminal shell, use the following to confirm the version of Python:

    python --version

## License

This sample is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT). Please see the [LICENSE](LICENSE) file for full details.


## Authors

Autodesk Premium Support Services

- Bastien Mazeran [@BastienMazeran](https://twitter.com/BastienMazeran)

See more at [Forge blog](https://forge.autodesk.com/blog).

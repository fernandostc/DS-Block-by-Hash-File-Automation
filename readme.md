Security Automation by Voice Control
===

![](Docs/Architecture/architecture.png)


A Python 3 integration using Falsk-ask to integrate with Deep Security Web API's, Alexa, and awscli.

>NOTE: This is a very initial commit and not recommended for use in production environment yet.



# Creating Alexa Lab – (Flask-ask Install)

### Create a [virtualenv] to install [Flask-ask]

```sh
$ virtualenv -p python3 --no-site-packages AlexaLab
$ . AlexaLab/bin/activate
```
### Following process on the link below to create a Flask Environment, Alexa Skill and Install ngrok

- [Flask-ask: Alexa Skills Kit Development]

:warning:`OBS:. Before to go to the next steps make sure Flask-ask and Alexa Skill it’s working properly. You will need an Alexa Dot or Tap to complete this first step.`



# Creating Alexa Lab - (DSP3 Install)

### Install [DSP3] inside the virtualenv AlexaLab

* Check if the virtualenv have these following requirements installed:
```sh
  suds-py3 >= 1.2.0.0
  requests >= 2.9.1
```
:warning:`OBS:. If not, install using pip install.`

* Install DSP3 inside virtualenv

```sh
  $ pip install -i https://testpypi.python.org/pypi dsp3
```



# Creating Alexa Lab - (awscli install)

* Install [awscli] inside the virtualenv AlexaLab
```sh
  $ pip install awscli
```

# Project Files Description

| Files Name | Description |
| ------ | ------ |
| sec_in_cloud.py | The main code to be used by the Flask-ask web service|
| templates.yaml | YAML file for speech templates|
| SecDashCloud.json | Cloud Formation JSON code to deploy a demo environment|
| deploy_ds | Deployment script for Deep Security Agent |

:warning:`OBS:. There are comments in each file for the code lines that you will need to update with your own information.`


# Video demo about Project :movie_camera:
- [Video Demo]


# Next Features (Planning)
  * Create security process to keep the credentials for Deep Security and the .pem for AWS account.
  * Create some authentication when you asked the application. This could be an integration with Google Authenticator.
  
:warning:`OBS:. This is an Open Source project that can anyone help to develop new call or features to help everyone that would like to use voice control for security automation.`

[//]: # (External Links)

[virtualenv]:https://virtualenv.pypa.io/en/stable/
[Flask-ask]:https://github.com/johnwheeler/flask-ask
[Flask-ask: Alexa Skills Kit Development]:https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/flask-ask-a-new-python-framework-for-rapid-alexa-skills-kit-development
[DSP3]:http://dsp3.readthedocs.io/en/latest/
[Video Demo]:https://www.youtube.com/watch?v=WaE5hjnuPOU
[awscli]:https://aws.amazon.com/cli/

Security Automation by block hash files using Deep Security API's
===

A Python 3 script using DSP3 SDK for Deep Security to create a Security automation for hash files.

Following the current functionalities:
1. Add File Hash by text file
2. Search by Hash
3. Delete File Hash by Hash
4. Delete File Hash by text file
5. List File Hashes


# Creating the Environment to use the Python3 script

:rotating_light:`To make it easy there is an install bash file that you could run to install everything automatically`

```sh
$ ./install.sh
```

### Create a [virtualenv] to install [DSP3]

```sh
$ virtualenv -p python3 --no-site-packages AlexaLab
$ . AlexaLab/bin/activate
```

### Install [DSP3] inside the virtualenv

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

# Project Files Description

| Files Name | Description |
| ------ | ------ |
| install.sh | Bash script to install (pip, virtualenv and DSP3) and create the virtualenv automatically|
| block_by_hash_sec_automation.py | The main python3 script with the API calls automation|


# Next Features (Planning)
  * Add Hash file by Hash
  
:warning:`OBS:. This is an Open Source project that can anyone help to develop new calls or features to help everyone that would like to use voice control for security automation.`

[//]: # (External Links)
[virtualenv]:https://virtualenv.pypa.io/en/stable/
[DSP3]:http://dsp3.readthedocs.io/en/latest/


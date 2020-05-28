Security Automation by block hash files using Deep Security API's
===

A Python 3 script using DSP3 SDK for Deep Security to create a Security automation for hash files.

Following the current functionalities:
1. Add Hashes through TEXT file
2. Search by Hash
3. Delete File Hash by Hash
4. Delete File Hash by text file
5. List File Hashes
6. Close Session

:warning:`OBS:. Use "python3 block_by_hash_sec_automation.py" to run the script. Python 3 is required.`


# Requirements
```sh
  python 3
  suds-py3 >= 1.2.0.0
  requests >= 2.9.1
  dsp3
```

# Creating the Environment to use the Python3 script

:rotating_light:`To make it easy there is an install bash file that you could run to install everything automatically`

```sh
$ ./install.sh
```

### Create a [virtualenv] to install [DSP3]

```sh
$ virtualenv -p python3 --no-site-packages DS_block_by_hash
$ . DS_block_by_hash/bin/activate
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
  $ pip install dsp3
```

# Project Files Description

| Files Name | Description |
| ------ | ------ |
| install.sh | Bash script to install (pip, virtualenv and DSP3) and create the virtualenv automatically|
| block_by_hash_sec_automation.py | The main python3 script with the API calls automation|
| add_file_hash.txt | TEXT file example to use in option 1 to add one or more hash file with description to Deep Security |

# Next Features (Planning)
  * Add Hash file by Hash
  
:warning:`OBS:. This is an Open Source project that can anyone help to develop for security automation.`

[//]: # (External Links)
[virtualenv]:https://virtualenv.pypa.io/en/stable/
[DSP3]:http://dsp3.readthedocs.io/en/latest/


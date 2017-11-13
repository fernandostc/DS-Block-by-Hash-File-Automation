sudo easy_install pip
sudo pip install virtualenv
local=$PWD
mkdir DSPS3
cd DSPS3
virtualenv -p python3 --no-site-packages venv
source venv/bin/activate
pip install suds-py3
pip install requests
pip install -i https://testpypi.python.org/pypi dsp3

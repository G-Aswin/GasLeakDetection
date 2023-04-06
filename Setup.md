# All the steps to set up this project (Ubuntu)

## Setting up Python 2.7
```bash
sudo apt install python2-minimal
python2 -V
```

## Setting up Pip2
```bash
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
pip2 --version
```

## Creating and Activating `virtualenv`
```bash
pip2 install virtualenv         # installing virtualenv package
virtualenv v_env                # creating a new virtual env
source v_env/bin/activate       # activating the new virtual env
```

## Installing the required set of packages
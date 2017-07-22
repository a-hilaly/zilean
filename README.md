# Zilean
Mysql tool kit and backup manager

- [1 - Getting Zilean](#getting-zilean)
- [2 - Setup](#setup)
- [3 - Documentation](#documentation)
- [3.1 - Setting zilean](#setting-zilean)
- [3.2 - Python3](#python3)
- [3.3 - Command Line](#command-line)
- [4 - Zilean Decorators](#zilean-decorators)
- [5 - Zilean Scripts](#zilean-scripts)

## Getting Zilean
classic git command

```shell
git clone https://github.com/iallabs/zilean.git
```
Or !
Try to use our one-feet-coded git like command line [babtu](https://github.com/iallabs/babtu.git)

## Setup

Make sure you have a mysql-server installed on your machine !

Zilean Python3 library:
```shell
cd Zilean/
sudo pip3 install -r requirements.txt
make -f Makefile py-setup
```

Zilean command line:
```shell
cd Zilean/
sudo pip3 install -r requiremenets.txt
make -f Makefile makezilean
```

## Documentation

Zilean Python and command line documentation

Zilean uses by default these settings to access to your mysql-server :
```json
{
    "hostname" : "localhost",
    "port" : 22,
    "user" : "root",
    "password" : ""
}    
```
Skip 3.1 if you have the same settings.

### 3.1 Setting Zilean

MySQL logs :

If you have installed only python3 package run the following commands at zilean directory
```shell
python3 setup.py setmysqllogs [-h hostname -p port -u user -p password]
```
If you have installed Zilean command line simply run
```shell
Zilean --settings sql [-h hostname -p port -u user -p password]
```

### Python3
At a first place


### Command Line

## Zilean Decorators

## Zilean Scripts

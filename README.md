# Zilean
mysql-server management : backups, security, partition, dev support


| Master | Dev | Coverage |
| --- | --- | --- |
| [![CircleCI](https://circleci.com/gh/iallabs/zilean-machine/tree/master.svg?style=svg&circle-token=f3d193e37ae25eb26cc445151abea74239fdc2a7)](https://circleci.com/gh/iallabs/zilean-machine/tree/master) | [![CircleCI](https://circleci.com/gh/iallabs/zilean/tree/zilean-dev.svg?style=svg&circle-token=f3d193e37ae25eb26cc445151abea74239fdc2a7)](https://circleci.com/gh/iallabs/zilean/tree/zilean-dev) | X |
#


- [1 - Getting Zilean](#1---getting-zilean)
- [2 - Setup](#2---setup)
- [3 - Documentation](#3---documentation)
- [3.1 - Setting zilean](#3.1---setting-zilean)
- [3.2 - Zilean Python3 Library](#3.2---python3)
- [3.2.1 - Zilean Session](#3.2.1---zilean-session)
- [3.2.2 - Zilean Pen](#3.2.1---zilean-pen)
- [3.2.3 - Zilean Backup](1)
- [3.3 - Zilean Command Line](#3.3---command-line)
- [3.4 - Zilean Decorators](#4---zilean-decorators)
- [3.5 - Zilean Scripts](#5zilean-scripts)

## 1 - Getting Zilean
classic git command

```shell
git clone https://github.com/iallabs/zilean.git
```
Or !
Try to use our one-feet-coded git like command line [babtu](https://github.com/iallabs/babtu.git)

## 2 - Setup

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

## 3 - Documentation

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

### 3.1 - Setting Zilean

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

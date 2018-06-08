# SugarLabs Social

A Platform of discussion for the projects, Activities, and Softwares of SugarLabs Organisation.

## Getting Started


* clone the project in your local computer
```
$ git clone https://github.com/avinashbharti97/SugarLabs_Social.git
```

### Prerequisites



```
- python3
- pip3
- virtualenvwrapper
- mongoDB
```

### Installing Prerequisites

```
$ sudo apt-get install python3 python3-pip virtualenvwrapper
```
To install mongoDB follow this link.

* [Install MONGO](https://www.mongodb.com/download-center#community)

start mongod in background before running the project
```
$ sudo service mongod start
```
check the status of mongoDB
```
$ sudo systemctl status mongod
```
You should see something like the lines below:

```
avinash@engine:~$ sudo systemctl status mongod
● mongod.service - MongoDB Database Server
   Loaded: loaded (/lib/systemd/system/mongod.service; enabled; vendor preset: e
   Active: active (running) since Thu 2018-06-07 16:26:02 IST; 7min ago
     Docs: https://docs.mongodb.org/manual
 Main PID: 7824 (mongod)
   CGroup: /system.slice/mongod.service
           └─7824 /usr/bin/mongod --config /etc/mongod.conf

Jun 07 16:26:02 engine systemd[1]: Started MongoDB Database Server.
Jun 07 16:26:02 engine mongod[7824]: 2018-06-07T16:26:02.788+0530 I CONTROL  [ma
lines 1-10/10 (END)

```


## Creating Virtual Enviornment
* move to the cloned project directory
```
$ virtualenv -p /usr/bin/python3 env
```
activate the virtualenv
```
$ source env/bin/activate
```
you should see (env) in the begining, something like this.
```
(env) avinash@engine:/media/avinash/raw/development/SugarLabs_Social$
```


### Installing and Running the project



```
$ pip install -r requirements.txt
```
```
$ cd Project_DIR
```
```
$ python manage.py runserver
```
you will see something like This
```
Performing system checks...

System check identified no issues (0 silenced).
June 07, 2018 - 11:12:23
Django version 1.11.13, using settings 'Project_SLS.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Redirect at the link shown.
# :boom: BOOM!

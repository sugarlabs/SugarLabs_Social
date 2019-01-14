<div align="center">
  <br>
  <img
    alt="Sugar Social"
    src="https://image.ibb.co/hX7JhU/sugarsocial.png"
    width=500px
  />
  <br/>
  <h1>Sugar Labs Social</h1>
  <strong>Learn | Create | Share</strong>
</div>
<br/>


<p align="center">
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-v2.0.6-brightgreen.svg" alt="django version"/>
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-v3-orange.svg" alt="python version"/>
  </a>
  <a href="https://www.postgresql.org/">
    <img src="https://img.shields.io/badge/Database-postgresql-blue.svg" alt="database postgresql"/>
  </a>
</p>

Welcome to the Sugar Labs Social codebase. We are so excited to have you. With your help, we can build out Sugar Labs Social to be more stable and better.


## What is Sugar Labs Social?
A Platform for sugar users/instructors/developers/teachers/parents to explore/discuss/share about Projects/softwares/activities/blogs/posts related to Sugar Labs|OLPC ❤️



## Table of Contents


- [Contributing](#contributing)
  - [What to contribute](#what-to-contribute)
  - [How to contribute](#how-to-contribute)
- [Contribution guideline](#contribution-guideline)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing Prerequisites](#installing-prerequisites)
  - [Setting up postgresql database](#setting-up-postgresql-database)
  - [Creating Virtual Enviornment](#creating-virtual-enviornment)
  - [Installing and Running the project](#installing-and-running-the-project)
  - [populating the data](#populating-the-data)
    - [creating superuser(admin)](#creating-superuseradmin)
- [Codebase](#codebase)



# Contributing
We expect contributors to abide by our underlying [code of conduct](https://github.com/sugarlabs/sugar-docs/blob/master/src/CODE_OF_CONDUCT.md). All conversations and discussions on GitHub (issues, pull requests) and across Sugar Labs Social must be respectful and harassment-free.

## What to contribute

**Refactoring** code, e.g. improving the code without modifying the behavior is an area that can probably be done based on intuition and may not require much communication to be merged.

**Fixing bugs** is the most sensitive area to work . bugs are magnets for other bugs.

**Improving UI/UX** i.e Responsiveness across diffrent width of devices.

**Building features** is the area which will require the most communication and/or negotiation. Every feature is subjective and open for debate.

**Documentation** is also a important area to work on.

## How to contribute

1. Fork the project & clone locally. Follow the initial setup [here](#getting-started) .
2. Create a branch, naming it either a feature or bug: `git checkout -b feature/that-new-feature` or `bug/fixing-that-bug`
3.  Code and commit your changes. Bonus points if you write a [good commit message](https://chris.beams.io/posts/git-commit/): `git commit -m 'Add some feature'`
4.  Push to the branch: `git push origin feature/that-new-feature`
5.  [Create a pull request](#create-a-pull-request) for your branch 🎉


# Contribution guideline

-----




# Getting Started


* clone the project in your local computer
```
$ git clone https://github.com/sugarlabs/social.git
```

## Prerequisites



```
- python3
- python3-pip
- virtualenvwrapper
- postgresql
- postgresql-contrib
- python-dev
- libpq-dev
```

## Installing Prerequisites

```
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip virtualenvwrapper python-dev libpq-dev postgresql postgresql-contrib
```

## Setting up postgresql database
>keep the value of database name, username and password same,
>else change the config respectively of settings.py in Project_SLS dir.
### Run the Postgresql Service
```
$ sudo service postgresql start
```
### Creating Database
```
$ sudo su - postgres
```
or
```
$ sudo -u postgres -i
```
> You should now be in a shell session for the postgres user. Log into a Postgres session by typing:
```
psql
```
> creating the database
```
CREATE DATABASE database;
```
*Remember to end all commands at an SQL prompt with a semicolon.*
> create the user with password
```
CREATE USER username WITH PASSWORD 'password';
```
> one more step
```
GRANT ALL PRIVILEGES ON DATABASE database TO username;
```
> exit the shell
```
\q
```
```
exit
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


## Installing and Running the project

```
$ cd Project_DIR
```

```
$ pip install -r requirements.txt
```

```
$ python manage.py makemigrations
```
>if any prompt choose option 2
```
$ python manage.py migrate
```
> ignore some errors
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

> use ctrl+c to stop the server and execute other command whenever needed.

## populating the data
Populate the data using admin panel

### creating superuser(admin)
```
$ python manage.py createsuperuser
```
> Fill the data asked in prompt


> run the server again
```
$ python manage.py runserver
```
> redirect to http://127.0.0.1:8000/admin.

> Login using the data you provided during creation of super user.


> populate some data of custom tags, Projects, softwares, activities.


> other data can be populated using the main app itself.


# Codebase
Hello World!!

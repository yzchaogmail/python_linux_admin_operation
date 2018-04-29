#-*- coding: UTF-8 -*-

from __future__ import print_function

from fabric.api import (cd, run,sudo,task,env,roles,put,execute,hide,settings)
from fabric.colors import red,green,yellow
from fabric.contrib.files import exists
import json

env.roledefs = {'web':['49.4.1.145','114.115.176.23'],
                'db':['114.115.180.236']}
env.hosts=['49.4.1.145','114.115.176.23','114.115.180.236']
env.key_filename = '/Users/liwenli/Downloads/KeyPair-y00300912.pem'
env.user = 'root'

############################
############################test_debug##########################
############################

def hostname():
    run('hostname')


def print_env():
    print(json.dumps(env,indent=4))

############################
############################redis_install_deploy#################
############################

def is_redis_installed():
    with settings(hide('everything'),warn_only=True):
        result = run("netstat -tl | grep -w 6379")
        return result.return_code == 0

def install_redis():
    run('yum install redis-server')

def chanage_redis_conf():
    run("sed -i 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf")

def reboot_redis():
    run("/etc/init.d/redis-server restart",pty=False)

@task
@roles('db')
def deploy_db():
    if is_redis_installed():
        print(yellow('redis was successfully installed'))
    else:
        install_redis()
        chanage_redis_conf()
        reboot_redis()
        print(green('redis was successfully installed'))


############################
############################web_server_install#######################
############################

def is_python_package_installed(package):
    with settings(hide('everything'),warn_only=True):
        result = run("python -c 'import {0}".format(package))
        return result.return_code == 0

def install_python_package(package):
    run('pip install {0}'.format(package))

def pip_install_if_need(package):
    if not is_python_package_installed(package):
        install_python_package(package)
        print(green('{0} has installed'.format(package)))

    else:
        print(yellow('{0} was installed'.format(package)))

def install_packages():
    for package in ['gunicorn','flask','redis']:
        pip_install_if_need(package)


def kill_web_app_if_exists():
    with cd('/tmp'):
        if exists('app.id'):
            pid = run('cat app.pid')
            print(yellow('kill app which pid is {0}'.format(pid)))
            with settings(hide('everything'),warn_only=True):
                run('kill -9 {0}'.format(pid))
        else:
            print(green('pid file not exists'))

def upload_web_app():
    put('/Users/liwenli/Documents/Github/python_linux_admin_operation/app.py','/tmp/app.py')

def run_web_app():
    with cd('/tmp'):
        run('gunicorn -w 1 app:app -b 0.0.0.0:5000 -D -p /tmp/app.pid --log-file /tmp/app.log',pty=False)

def restart_web_app():
    kill_web_app_if_exists()
    run_web_app()

@task
@roles('web')
def deploy_web():
    install_packages()
    upload_web_app()
    restart_web_app()


###################################
###################################deploy_all#####################
###################################

@task
def deploy_all():
    execute(deploy_db)
    execute(deploy_web)

import os, sys, shutil, platform, subprocess, json
import threading


def getType(p):
    type = 'string'
    if isinstance(p, list):
        type = 'list'
    elif isinstance(p, str):
        try:
            if isinstance(p, dict):
                type = 'string_dictionary'
            else:
                type = 'string'
        except Exception as e:
            type = 'string'
            return type
    elif (p is not None) and (isinstance(p, dict)):
        type = 'dictionary'
    else:
        type = 'other'
    return type


def git_clone(repository_url, directory_name):
    try:
        shutil.rmtree('./{}'.format(directory_name))
    except Exception as e:
        print(e)

    gitClone = subprocess.Popen(['git', 'clone', repository_url, directory_name], stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)

    try:
        stdout, stderr = gitClone.communicate()
        retcode = gitClone.returncode
        if retcode == 0:
            print('stdout: {}'.format(stdout))
            print('cloning finish...')
        else:
            print('stderr: {}'.format(stdout))
    except Exception as e:
        print("git_clone Error: ", sys.exc_info())


def git_pull(directory_name):
    try:
        if platform.system() == 'Windows':
            cmd = 'git'
        else:
            cmd = 'git'

        gitPull = subprocess.Popen([cmd, 'pull'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, cwd=os.getcwd() + '/' + directory_name, text=True)

        (stdout, stderr) = gitPull.communicate()

        retcode = gitPull.returncode
        if retcode == 0:
            print('stdout: {}'.format(stdout))
        else:
            print('stderr: {}'.format(stdout))

    except Exception as e:
        print('git_pull Error: ', sys.exc_info())
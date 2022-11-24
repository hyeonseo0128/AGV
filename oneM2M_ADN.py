import json
import requests
import configuration


def retrieveCSE(path):

    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'SOrigin'
    }

    response = requests.request("GET", path, headers=headers, data=payload)

    print(response.text)


def createAE(ae_name, path):
    payload = {
        'm2m:ae': {
            'rn': ae_name,
            'api': configuration.ae['api'],
            'rr': 'true'
        }
    }
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'S' + configuration.ae['origin'],
        'Content-Type': 'application/json;ty=2'
    }

    response = requests.request("POST", path, headers=headers, data=json.dumps(payload))

    print(response.text)


def retrieveAE(path):
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'S' + configuration.ae['origin']
    }

    response = requests.request("GET", path, headers=headers, data=payload)

    print(response.text)


def deleteAE(path):
    payload = ""
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': configuration.conf['masterUser']
    }

    response = requests.request("DELETE", path, headers=headers, data=payload)

    print(response.text)


def createCNT(cnt_name, path):
    payload = {
        'm2m:cnt': {
            'rn': cnt_name,
            'lbl': [cnt_name]
        }
    }
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'S' + configuration.ae['origin'],
        'Content-Type': 'application/json; ty=3'
    }

    response = requests.request("POST", path, headers=headers, data=json.dumps(payload))

    print(response.text)


def retrieveCNT(path):
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'S' + configuration.ae['origin']
    }

    response = requests.request("GET", path, headers=headers, data=payload)

    print(response.text)


def deleteCNT(path):
    payload = ""
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': configuration.conf['masterUser']
    }

    response = requests.request("DELETE", path, headers=headers, data=payload)

    print(response.text)


def createCIN(con, path):
    payload = {
        'm2m:cin': {
            'con': con
        }
    }
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'S' + configuration.ae['origin'],
        'Content-Type': 'application/json; ty=4'
    }

    response = requests.request("POST", path, headers=headers, data=json.dumps(payload))

    print(response.text)


def retrieveLatestCIN(path):
    cinPath = path + '/la'
    payload = {}
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'S' + configuration.ae['origin']
    }

    response = requests.request("GET", cinPath, headers=headers, data=payload)

    print(response.text)


def createSUB(rn, nu, path):
    payload = {
        'm2m:sub': {
            'rn': rn,
            'enc': {
              'net': [1, 2, 3, 4]
            },
            'nu': [nu],
            'exc': 10
        }
    }
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': 'S' + configuration.ae['origin'],
        'Content-Type': 'application/json;ty=23'
    }

    response = requests.request("POST", path, headers=headers, data=json.dumps(payload))

    print(response.text)


def deleteSUB(path):
    payload = ""
    headers = {
        'Accept': 'application/json',
        'X-M2M-RI': '12345',
        'X-M2M-Origin': configuration.conf['masterUser']
    }

    response = requests.request("DELETE", path, headers=headers, data=payload)

    print(response.text)

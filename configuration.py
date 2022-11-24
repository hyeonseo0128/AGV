import json
import uuid

conf = {}
cse = {}
ae = {}

cse["host"] = '203.253.128.161'
cse["port"] = '7579'
cse["name"] = 'Mobius'
cse["id"] = '/Mobius2'
cse["mqttport"] = '1883'

ae["rn"] = 'AGV'
ae["api"] = str(uuid.uuid1())
ae["origin"] = 'Son'
ae["port"] = '3000'

conf["cse"] = cse
conf["ae"] = ae
conf["masterUser"] = 'Sponde'

import json
import configuration
import oneM2M_ADN


csePath = 'http://' + configuration.cse['host'] + ':' + configuration.cse['port'] + '/' + configuration.cse['name']
aePath = csePath + '/' + configuration.ae['rn']
cntPath = aePath + '/' + 'test'
subPath = cntPath + '/' + 'sub'
nu = "mqtt://203.253.128.164/parkingSpot_cin_to_flx?ct=json"

# oneM2M_ADN.createAE('AGV', csePath)
# oneM2M_ADN.retrieveAE(aePath)
# oneM2M_ADN.deleteAE(aePath)
# oneM2M_ADN.createCNT('test', aePath)
# oneM2M_ADN.retrieveCNT(cntPath)
# oneM2M_ADN.retrieveLatestCIN(cntPath)
# oneM2M_ADN.createSUB('sub', nu, cntPath)
# oneM2M_ADN.deleteSUB(subPath)
import requests
from requests_toolbelt.utils import formdata
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
import time


while True:
    time.sleep(5)
    ## REQUEST BUS STOP DATA
    url = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last/geo/GetArriveStop.php'
    query = {
        "idClient":"WEB.SERV.marc.aguilar@gmail.com",
        "passKey":"A6C8FC19-2A93-4CCB-AA8C-D044CF02D934",
        "idStop":"5089",
        "cultureInfo":"ES"
    }
    resp = requests.post(
        url,
        data=formdata.urlencode(query),
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
    )

    data = resp.json()
    arrives = data['arrives']
    for arrive in arrives:
        if(arrive['lineId'] == "63"):
            print arrive
            if(arrive['busDistance'] < 2):
                print "################## El autobus ha llegado a la parada! BusId: " + arrive['busId']
    
    


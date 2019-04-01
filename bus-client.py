import requests
from requests_toolbelt.utils import formdata
from BusArrive import BusArrive
from datetime import datetime
#from kafka import KafkaProducer
#from kafka import KafkaConsumer
import json
import time


arrivals = []

while True:
        time.sleep(5)
        ## REQUEST BUS STOP DATA
        url = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last/geo/GetArriveStop.php'
        query = {
            "idClient":"WEB.SERV.marc.aguilar@gmail.com",
            "passKey":"A6C8FC19-2A93-4CCB-AA8C-D044CF02D934",
            "idStop":"1887",
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
        data_mock = {
            "arrives": [
                {
                    "stopId": 1887,
                    "lineId": "3",
                    "isHead": "False",
                    "destination": "SAN AMARO",
                    "busId": "4615",
                    "busTimeLeft": 10,
                    "busDistance": 0,
                    "longitude": -3.7113742223573,
                    "latitude": 40.406431234994,
                    "busPositionType": 1
                },
                {
                    "stopId": 1887,
                    "lineId": "3",
                    "isHead": "False",
                    "destination": "SAN AMARO",
                    "busId": "4616",
                    "busTimeLeft": 100,
                    "busDistance": 200,
                    "longitude": -3.7130161106724,
                    "latitude": 40.408697090458,
                    "busPositionType": 1
                },
                {
                    "stopId": 1887,
                    "lineId": "3",
                    "isHead": "False",
                    "destination": "SAN AMARO",
                    "busId": "4616",
                    "busTimeLeft": 0,
                    "busDistance": 0,
                    "longitude": -3.7130161106724,
                    "latitude": 40.408697090458,
                    "busPositionType": 1
                },
                {
                    "stopId": 1887,
                    "lineId": "3",
                    "isHead": "False",
                    "destination": "SAN AMARO",
                    "busId": "4617",
                    "busTimeLeft": 400,
                    "busDistance": 600,
                    "longitude": -3.7130161106724,
                    "latitude": 40.408697090458,
                    "busPositionType": 1
                }
            ]
        }
        arrives = data_mock['arrives']
        for arrive in arrives:
            if(arrive['lineId'] == "3"):
                if(arrive['busDistance'] < 2):
                    busArrive = BusArrive (arrives[0]['busId'],datetime.now(), arrives[1]['busId'], arrives[1]['busTimeLeft']);
                    arrivals.append(busArrive);
                    print "################## El autobus ha llegado a la parada! BusId: " + busArrive.busId + " Hora:" + busArrive.arrivalTime.strftime("%H:%M:%S.%f - %b %d %Y");
                    print "################## Siguiente bus: " + busArrive.nextBusId + " Estimacion:" + str(busArrive.estimatedNextBusTime);

                    time.sleep(95)
                    busArrive = BusArrive (arrives[2]['busId'],datetime.now(), arrives[3]['busId'], arrives[3]['busTimeLeft']);
                    arrivals.append(busArrive);
                    timeEstimated = arrivals[0].estimatedNextBusTime;
                    timeReal = (arrivals[1].arrivalTime - arrivals[0].arrivalTime).seconds

                    print "The difference is " + str(timeEstimated - timeReal);

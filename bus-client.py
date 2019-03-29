import requests
from requests_toolbelt.utils import formdata
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

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
# TODO Verify response code
# TODO Loop every X seconds
print resp.json();
# TODO Publish on Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    # Encode all values as JSON
    value_serializer=lambda value: json.dumps(value).encode('utf-8'),
)
while True:
    producer.send('EMTStopGeoBusData', value={'foo': 'bar'})

# producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
# for i in range(1000):
#     producer.send('EMTStopGeoBusData', {'foo': 'bar'})
#producer = KafkaProducer(bootstrap_servers='localhost:9092')
#for _ in range(100):
#    producer.send('EMTStopGeoBusData', b'some_message_bytes')

consumer = KafkaConsumer('EMTStopGeoBusData')
for msg in consumer:
    print (msg)
    



from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['kafka-0:9093', 'kafka-1:9093', 'kafka-2:9093'],\
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'),\
                        client_id='sepehr',\
                        # acks='all'
                        )
                        
def Kafka_Send_Message(message_body):

    producer.send('sepehr', value=message_body)
    producer.flush()

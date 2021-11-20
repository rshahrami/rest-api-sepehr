import pika
# blocked_connection_timeout=300

# credentials = pika.PlainCredentials('user', 'password')
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='ip_rabbit',\
#                                                             credentials=credentials, heartbeat=10,\
#                                                             blocked_connection_timeout=10,\
#                                                             ))
# channel = connection.channel()


# def Rabbitmq_Send_Message(message_body):
#     channel.exchange_declare(exchange='test_test2', exchange_type='durable')
#     channel.queue_declare(queue='test_test2', durable=True)
 
#     channel.queue_bind(exchange='test_test2', queue='test_test2', routing_key='test_test2')
#     channel.basic_publish(exchange='test_test2', routing_key='test_test2', body=message_body,\
#                         )


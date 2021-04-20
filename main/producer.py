import pika, json

params = pika.URLParameters('amqps://ioznqevc:cQpmRVSd2BmxHAhLt7g050r2AMb0FyXY@vulture.rmq.cloudamqp.com/ioznqevc')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)

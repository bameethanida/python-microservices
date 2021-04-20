import pika, json

params = pika.URLParameters('amqps://vqrnohxh:FsSNaQZ74kW8X6G8lKcm8zwCQz8kG8x-@fish.rmq.cloudamqp.com/vqrnohxh')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)

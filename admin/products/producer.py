import pika, json

params = pika.URLParameters('your_rabbamqps://vqrnohxh:FsSNaQZ74kW8X6G8lKcm8zwCQz8kG8x-@fish.rmq.cloudamqp.com/vqrnohxhitmq_url')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

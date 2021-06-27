import pika
import json

params = pika.URLParameters("amqps://javtojwu:D7B7KXkebYwCfWTw0orCUPYt6ZaU8b8n@roedeer.rmq.cloudamqp.com/javtojwu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange = '', routing_key = 'main', body = json.dumps(body), properties = properties)
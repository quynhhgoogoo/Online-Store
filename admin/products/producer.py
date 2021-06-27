import pika

params = pika.URLParameters("amqps://javtojwu:D7B7KXkebYwCfWTw0orCUPYt6ZaU8b8n@roedeer.rmq.cloudamqp.com/javtojwu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange = '', routing_key = 'admin', body = 'Hello')
import pika

params = pika.URLParameters("amqps://javtojwu:D7B7KXkebYwCfWTw0orCUPYt6ZaU8b8n@roedeer.rmq.cloudamqp.com/javtojwu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue = 'admin')


def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)


channel.basic_consume(queue = 'admin', on_message_callback = callback, auto_ack = True)

print("Started Consuming")
channel.start_consuming()

channel.close()

import pika
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters("amqps://javtojwu:D7B7KXkebYwCfWTw0orCUPYt6ZaU8b8n@roedeer.rmq.cloudamqp.com/javtojwu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue = 'admin')


def callback(ch, method, properties, body):
    print("Received in admin")
    data = json.loads(body)
    print(data)

    # Update likes for product
    product = Product.objects.get(id = data)
    product.likes = product.likes + 1
    product.save()
    print("Product's likes increased")


channel.basic_consume(queue = 'admin', on_message_callback = callback, auto_ack = True)

print("Started Consuming")
channel.start_consuming()

channel.close()

#!/usr/bin/python
# #coding:utf-8 change
# filename：pythonpkia.py

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'HELLO')
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,queue='HELLO',no_ack=True)

print '[*] Waiting for message. To exit press CRTL+C'
channel.start_consuming()
#!/usr/bin/python
# #coding:utf-8 change
# filename：pythonpkia.py

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='HELLO')

for i in range(10):
    channel.basic_publish(exchange='',routing_key='HELLO',body='Hello World'+str(i))
    print "[%d] Sent 'Hello World!'" % i

connection.close()
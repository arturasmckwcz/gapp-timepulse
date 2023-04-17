import pika
import time
import random

from console import log
from manager.loop_status import Statuses, get_loop_status, set_loop_status
from .current_day import get_current_day
from setup import rabbitmq_setup


def pulse():
    if get_loop_status() == Statuses.STOP:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbitmq_setup.host,
                                      credentials=pika.PlainCredentials(
                                          username=rabbitmq_setup.user,
                                          password=rabbitmq_setup.password)))
        channel = connection.channel()
        channel.exchange_declare(rabbitmq_setup.exchange,
                                 exchange_type='fanout')
        set_loop_status(Statuses.LOOP)

    while get_loop_status() != Statuses.STOP:
        while get_loop_status() == Statuses.LOOP:
            message = get_current_day().strftime('%Y-%m-%d')
            channel.basic_publish(exchange=rabbitmq_setup.exchange,
                                  routing_key='',
                                  body=message)
            log(f"Sent message: {message}")
            time.sleep(rabbitmq_setup.day)

    connection.close()

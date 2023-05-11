import pika
import time

from console import log, log_debug
from manager.loop_status import loop_statuses, loop_status
from .current_day import date
from setup import rabbitmq_setup


def pulse():
    connection = None
    if loop_status.get_status() == loop_statuses.STOP:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=rabbitmq_setup.host,
                    credentials=pika.PlainCredentials(
                        username=rabbitmq_setup.user,
                        password=rabbitmq_setup.password)))
            channel = connection.channel()
            channel.exchange_declare(rabbitmq_setup.exchange,
                                     exchange_type='fanout')
            log_debug(f"current_date={date.current_date()}")
            loop_status.set_status(loop_statuses.LOOP)
        except Exception as e:
            log("Failed to connect to messaging service\n", e)
            log_debug(f"host={rabbitmq_setup.host}")

    while loop_status.get_status() != loop_statuses.STOP:
        message = date.next_date()
        channel.basic_publish(exchange=rabbitmq_setup.exchange,
                              routing_key='',
                              body=message)
        log(f"Sent message: {message}")
        time.sleep(rabbitmq_setup.day)

    if connection:
        connection.close()

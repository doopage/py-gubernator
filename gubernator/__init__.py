# This code is py3.7 and py2.7 compatible
import time
import grpc
from datetime import datetime
from gubernator.gubernator_pb2_grpc import V1Stub


MILLISECOND = 1
SECOND = MILLISECOND * 1000
MINUTE = SECOND * 60


def sleep_until_reset(reset_time):
    now = datetime.now()
    time.sleep((reset_time - now).seconds)


def V1Client(endpoint='127.0.0.1:9090'):
    channel = grpc.insecure_channel(endpoint)
    return V1Stub(channel)

import logging
import pytest

from mqtt_connector import MQTTConnector
from test_helpers.echo_client import TestEchoClient
from tests.connector_tests import TEST_ECHO_CLIENT_NAME, TEST_SENDER_NAME, TEST_PATH,\
    test_payload_big, test_payload_small

# Data for the MQTT Broker
BROKER_IP = "192.168.178.111"
BROKER_PORT = 1883
BROKER_USER = None
BROKER_PW = None


@pytest.fixture
def echo_client():
    sender = MQTTConnector(TEST_ECHO_CLIENT_NAME,
                           BROKER_IP,
                           BROKER_PORT,
                           BROKER_USER,
                           BROKER_PW)
    echo = TestEchoClient(sender)
    yield echo
    sender.__del__()


@pytest.fixture
def sender():
    sender = MQTTConnector(TEST_SENDER_NAME,
                           BROKER_IP,
                           BROKER_PORT,
                           BROKER_USER,
                           BROKER_PW)
    yield sender
    sender.__del__()


def test_mqtt_connector_send(sender: MQTTConnector, test_payload_big, echo_client):
    response = sender.send_request(TEST_PATH, TEST_ECHO_CLIENT_NAME, test_payload_big)
    assert response is not None
    assert response.get_payload() == test_payload_big
    return


def test_mqtt_connector_send_split_long(sender: MQTTConnector, test_payload_big, echo_client):
    response = sender.send_request_split(TEST_PATH, TEST_ECHO_CLIENT_NAME, test_payload_big)
    assert response is not None
    assert response.get_payload() == test_payload_big
    return


def test_mqtt_connector_send_split_short(sender: MQTTConnector, test_payload_small, echo_client):
    response = sender.send_request_split(TEST_PATH, TEST_ECHO_CLIENT_NAME, test_payload_small)
    assert response is not None
    assert response.get_payload() == test_payload_small
    return


def test_mqtt_connector_broadcast(sender: MQTTConnector, test_payload_big, echo_client):
    responses = sender.send_broadcast(TEST_PATH, test_payload_big)
    assert len(responses) >= 1
    assert responses[0].get_payload() == test_payload_big
    return


def test_mqtt_connector_broadcast_max_responses(sender: MQTTConnector, test_payload_big, echo_client):
    responses = sender.send_broadcast(TEST_PATH, test_payload_big, max_responses=1)
    assert len(responses) == 1
    assert responses[0].get_payload() == test_payload_big
    return

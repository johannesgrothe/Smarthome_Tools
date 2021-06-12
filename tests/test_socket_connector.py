import pytest

from socket_connector import SocketServer, SocketClient
from test_helpers.echo_client import TestEchoClient
from tests.connector_tests import test_payload_big, test_payload_small
from tests.connector_tests import send_test, send_split_test, broadcast_test, broadcast_single_response_test


SERVER_PORT = 5781
SERVER_IP = "localhost"

SERVER_NAME = "pytest_socket_server"
CLIENT_NAME = "pytest_socket_client"


@pytest.fixture
def server():
    server = SocketServer(SERVER_NAME,
                          SERVER_PORT)
    yield server
    server.__del__()


@pytest.fixture
def client():
    client = SocketClient(CLIENT_NAME,
                          SERVER_IP,
                          SERVER_PORT)
    yield client
    client.__del__()


@pytest.fixture
def echo_client(client):
    echo_client = TestEchoClient(client)
    return echo_client


@pytest.fixture
def echo_server(server):
    echo_server = TestEchoClient(server)
    return echo_server


def test_socket_server_send(server: SocketServer, test_payload_big: dict, echo_client: TestEchoClient):
    send_test(server, CLIENT_NAME, test_payload_big)


def test_socket_server_send_split_long(server: SocketServer, test_payload_big: dict, echo_client: TestEchoClient):
    send_split_test(server, CLIENT_NAME, test_payload_big)


def test_socket_server_send_split_short(server: SocketServer, test_payload_small: dict, echo_client: TestEchoClient):
    send_split_test(server, CLIENT_NAME, test_payload_small)


def test_socket_server_send_broadcast(server: SocketServer, test_payload_small: dict, echo_client: TestEchoClient):
    broadcast_test(server, test_payload_small)


def test_socket_server_send_broadcast_single_resp(server: SocketServer, test_payload_small: dict, echo_client: TestEchoClient):
    broadcast_single_response_test(server, test_payload_small)


def test_socket_client_send(echo_server: TestEchoClient, test_payload_big: dict, client: SocketClient):
    send_test(client, SERVER_NAME, test_payload_big)


def test_socket_client_send_split_long(echo_server: TestEchoClient, test_payload_big: dict, client: SocketClient):
    send_split_test(client, SERVER_NAME, test_payload_big)


def test_socket_client_send_split_short(echo_server: TestEchoClient, test_payload_small: dict, client: SocketClient):
    send_split_test(client, SERVER_NAME, test_payload_small)


def test_socket_client_send_broadcast(echo_server: TestEchoClient, test_payload_small: dict, client: SocketClient):
    broadcast_test(client, test_payload_small)


def test_socket_client_send_broadcast_single_resp(echo_server: TestEchoClient, test_payload_small: dict, client: SocketClient):
    broadcast_single_response_test(client, test_payload_small)

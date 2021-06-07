import pytest
from network_connector import Request

TEST_ECHO_CLIENT_NAME = "pytest_echo_client"
TEST_SENDER_NAME = "pytest_sender"
TEST_PATH = "smarthome/unittest"

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut " \
              "labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores " \
              "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem " \
              "ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore " \
              "et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea " \
              "rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

LOREM_IPSUM_SHORT = "Lorem ipsum, digga"


@pytest.fixture
def test_payload_big() -> dict:
    return {"data": 12345,
            "list": [1, 2, 3, 4, 5],
            "strings":
                {
                    "lorem_long": LOREM_IPSUM,
                    "lorem_short": LOREM_IPSUM_SHORT
                }
            }


@pytest.fixture
def test_payload_small() -> dict:
    return {"lorem": LOREM_IPSUM_SHORT}

import pytest
from ccm_simulator import CCMSimulator

@pytest.fixture
def ccm():
    return CCMSimulator()

from fastapi.testclient import TestClient
from main import workspace

client = TestClient(workspace)

def testGetController():
    path = "/getJson"

    response = client.get(path)
    statusCode = response.status_code
    contentType = response.headers['content-type']
    assert statusCode == 200
    assert contentType == "application/json"
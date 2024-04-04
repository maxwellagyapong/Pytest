import pytest
import source.service as service
import unittest.mock as mock
import requests


""" Mocking is a testing techniques which is used to isolate the system that we are
testing and replace the external dependencies with controlled implementations called
mocks. Usually used when we are testing a method that requests data from an external API.
We can not use the actual API for testing because, APIs may be slow, it might cause 
money or affect rate limits. Also, depending on the API data, as that is subject to change,
it might cause our test to fail. So we don't want to depend on the API itself. Also the 
connection might be distructed and the test might fail. So, we just know what the API will 
return then we mock that and test that."""


@mock.patch('source.service.get_user_from_db')
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Alice"
    user_name = service.get_user_from_db(1)
    
    assert user_name == "Alice"
    
@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
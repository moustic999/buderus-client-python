
import pytest
import asyncio
from asynctest import CoroutineMock
from unittest.mock import patch, MagicMock
from aiohttp import web, ClientSession
from bosch_thermostat_http.gateway import Gateway

@pytest.mark.asyncio
async def test_get_success():
     async with ClientSession() as session:
       
        with patch('bosch_thermostat_http.http_connector.HttpConnector.request', new=CoroutineMock(return_value="bla")) as mocked_get:
            with patch('bosch_thermostat_http.encryption.Encryption.decrypt', MagicMock(return_value='{"id": "/gateway/uuid"}')) as mocked_decrypt:
                gateway = Gateway(session, 'bla', 'aaa', 'xxx')
                gtw_resp = await gateway.get('/gateway/uuid')
                mocked_get.assert_called_once_with('/gateway/uuid')
                mocked_decrypt.assert_called_once_with('bla')
                assert gtw_resp == {'id': '/gateway/uuid'}
        
    
      
    

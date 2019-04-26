import unittest
from unittest.mock import patch, MagicMock
import json
import pytest
from asynctest import CoroutineMock
import asyncio
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web, ClientSession
from bosch_thermostat_http.gateway import Gateway
from bosch_thermostat_http.encryption import Encryption


    

@pytest.mark.asyncio
async def test_get():
     async with ClientSession() as session:
       
        with patch('bosch_thermostat_http.http_connector.HttpConnector.request', new=CoroutineMock(return_value="bla")) as mocked_get:
            with patch('bosch_thermostat_http.encryption.Encryption.decrypt', MagicMock(return_value='{"id": "/gateway/uuid"}')) as mocked_decrypt:
                gateway = Gateway(session, 'bla', 'aaa', 'xxx')
                gtw_resp = await gateway.get('/gateway/uuid')
                mocked_get.assert_called_once_with('/gateway/uuid')
                mocked_decrypt.assert_called_once_with('bla')
                assert gtw_resp == {'id': '/gateway/uuid'}
        
    
      
    

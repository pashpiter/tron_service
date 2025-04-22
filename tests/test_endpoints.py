from datetime import datetime

import pytest
from httpx import AsyncClient

from models.wallet import WalletQueryDB
from schemas.wallet import WalletQuery
from .fixtures.wallet import WALLET_ADDRESS


@pytest.mark.asyncio
async def test_get_latest_query(client: AsyncClient):
    response = await client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert len(data['items']) == 0


@pytest.mark.asyncio
async def test_get_query(client: AsyncClient, wallet_query: WalletQueryDB):
    response = await client.get('/')
    assert response.status_code == 200
    data = response.json()
    wallet = data['items'][0]
    query = WalletQuery.model_validate(wallet_query).model_dump()
    for key, value in query.items():
        if key == 'timestamp':
            assert wallet[key] == str(
                datetime.isoformat(value)
            ).replace('+00:00', 'Z')
        else:
            assert wallet[key] == value


@pytest.mark.asyncio
async def test_post_wallet_address(client: AsyncClient):
    input_data = {
        'address': WALLET_ADDRESS,
    }
    response = await client.post('/', json=input_data)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 4
    assert data['address'] == WALLET_ADDRESS
    assert 'trx_balance' in data
    assert 'bandwidth' in data
    assert 'energy' in data

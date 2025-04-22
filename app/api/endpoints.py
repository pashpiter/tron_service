from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.services import tron
from database.connection import get_session
from database.crud import add_wallet_request, get_latest_wallet_query
from schemas.wallet import (LatestWalletQueryList, WalletQueryCreate,
                            WalletQueryRead)

router = APIRouter()


@router.get('/', response_model=LatestWalletQueryList)
async def latest_wallet_query(
    offset: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_session)
):
    '''Получение последних записей из БД с данными по address'''
    query = await get_latest_wallet_query(
        session, offset, limit
    )
    return query


@router.post('/', response_model=WalletQueryRead)
async def get_info_about_address(
    query_create: WalletQueryCreate,
    session: AsyncSession = Depends(get_session)
):
    '''Получение информации по tron address'''
    wallet_info = await tron.get_wallet_info(query_create.address)
    await add_wallet_request(session, wallet_info)
    return wallet_info

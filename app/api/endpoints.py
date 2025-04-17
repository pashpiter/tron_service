from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.connection import get_session
from database.crud import get_latest_wallet_query
from schemas.wallet import (WalletResponse, LatestWalletQueryList,
                            WalletRequest)


router = APIRouter()


@router.get('/', response_model=LatestWalletQueryList)
async def latest_wallet_query(
    offset: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_session)
):
    query = await get_latest_wallet_query(
        session, offset, limit
    )
    return query


@router.post('/', response_model=WalletResponse)
async def get_info_about_adress(
    address: WalletRequest,
    session: AsyncSession = Depends(get_session)
):
    pass

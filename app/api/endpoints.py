from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.connection import get_session
from schemas.wallet import (WalletResponse, LatestWalletQueryListResponse,
                            WalletRequest)


router = APIRouter(prefix='/')


@router.get('/', response_model=LatestWalletQueryListResponse)
async def latest_wallet_query(
    offset: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_session)
):
    pass


@router.post('/', response_model=WalletResponse)
async def get_info_about_adress(
    adress: WalletRequest,
    session: AsyncSession = Depends(get_session)
):
    pass

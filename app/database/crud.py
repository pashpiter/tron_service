from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from models.wallet import WalletQueryDB
from schemas.wallet import (LatestWalletQueryList, WalletQuery,
                            WalletQueryReadWithTime)


async def get_latest_wallet_query(
        session: AsyncSession,
        offset: int,
        limit: int
) -> LatestWalletQueryList:
    '''Получение последних записей из БД'''
    stmt = (
        select(WalletQueryDB)
        .offset(offset)
        .limit(limit)
        .order_by(WalletQueryDB.id.desc())
    )
    results: Result = await session.execute(stmt)
    items = [
        WalletQueryReadWithTime.model_validate(
            item, from_attributes=True
        ) for item in results.scalars().all()
    ]
    return LatestWalletQueryList(items=items)


async def add_wallet_request(
        session: AsyncSession,
        wallet_query: dict
) -> WalletQuery:
    '''Добавление новой записи в БД'''
    wallet = WalletQueryDB(**wallet_query)
    session.add(wallet)
    await session.commit()
    await session.refresh(wallet)
    return wallet

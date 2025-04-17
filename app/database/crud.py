from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.wallet import WalletQueryDB
from schemas.wallet import WalletQuery, LatestWalletQueryList


async def get_latest_wallet_query(
        session: AsyncSession,
        offset: int,
        limit: int
) -> list[WalletQuery]:
    stmt = (
        select(WalletQueryDB)
        .offset(offset)
        .limit(limit)
        .order_by(WalletQueryDB.id.desc())
    )
    result: Result = await session.execute(stmt)
    items = [
        WalletQuery.model_validate(item) for item in result.scalars().all()
    ]
    return LatestWalletQueryList(items=items)


async def create_wallet_request(
        session: AsyncSession,
        wallet: WalletQuery
) -> WalletQuery:
    pass

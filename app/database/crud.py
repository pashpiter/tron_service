from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.wallet import Wallet


async def get_latest_wallet_query(
        session: AsyncSession,
        offset: int,
        limit: int
) -> list[Wallet]:
    pass


async def create_wallet_request(
        session: AsyncSession,
        wallet: Wallet
) -> Wallet:
    pass

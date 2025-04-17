from datetime import datetime
from typing import List
from pydantic import BaseModel


class WalletBase(BaseModel):
    wallet_address: str
    trx_balance: float
    bandwidth: int
    energy: int


class Wallet(WalletBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True


class WalletRequest(BaseModel):
    address: str


class WalletResponse(WalletBase):
    pass


class LatestWalletQueryListResponse(BaseModel):
    items: List[WalletBase]
    limit: int
    offset: int

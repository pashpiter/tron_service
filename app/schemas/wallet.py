from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WalletQueryBase(BaseModel):
    address: str
    trx_balance: float
    bandwidth: int
    energy: int


class WalletQuery(WalletQueryBase):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


class WalletQueryCreate(BaseModel):
    address: str


class WalletQueryRead(WalletQueryBase):
    pass


class WalletQueryReadWithTime(WalletQueryRead):
    id: int
    timestamp: datetime


class LatestWalletQueryList(BaseModel):
    items: list[WalletQueryReadWithTime]

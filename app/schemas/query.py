from datetime import datetime
from typing import List
from pydantic import BaseModel


class LatestQuery(BaseModel):
    id: int
    wallet_address: str
    timestamp: datetime
    trx_balance: float
    bandwidth: int
    energy: int

    class Config:
        orm_mode = True


class LatestQueryList(BaseModel):
    items: List[LatestQuery]
    page: int
    size: int

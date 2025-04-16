from pydantic import BaseModel


class WalletRequest(BaseModel):
    address: str


class WalletResponse(BaseModel):
    address: str
    trx_balance: float
    bandwidth: int
    energy: int

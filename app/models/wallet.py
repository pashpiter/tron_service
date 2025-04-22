from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WalletQueryDB(Base):
    __tablename__ = "wallet_query"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), default=func.now())
    trx_balance = Column(Float)
    bandwidth = Column(Integer)
    energy = Column(Integer)

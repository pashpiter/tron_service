from tronpy import Tron

from core.config import settings


class TronService:
    def __init__(self):
        self.client = Tron(network=settings.tron.network)

    async def get_wallet_info(
            self, address: str
    ) -> dict[str, str | int | float]:
        '''Проверка что существует такой адрес и получение bandwidth,
        trx_balance, energy по адресу'''
        if not self.client.is_address(address):
            raise ValueError('Invalid TRON address')
        account_resources = self.client.get_account_resource(address)
        trx_balance = float(self.client.get_account_balance(address))
        bandwidth = max(
            0,
            account_resources.get(
                'freeNetLimit', 0
            ) - account_resources.get(
                'freeNetUsed', 0
            )
        )
        energy = max(
            0,
            account_resources.get(
                'EnergyLimit', 0
            ) - account_resources.get(
                'EnergyUsed', 0
            )
        )
        return {
            'address': address,
            'trx_balance': trx_balance,
            'bandwidth': bandwidth,
            'energy': energy
        }


tron = TronService()

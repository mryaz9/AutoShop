from dataclasses import dataclass


@dataclass
class ColumnsData:
    user_id: int = 0
    username: str = "None"
    balance: float = 0.0
    card_name: str = "None"
    datetime_to_buy: str = "None"


@dataclass
class AdminData:
    user_id: int = 0
    username: str = "None"


@dataclass
class ShopData:
    name: str = "None"
    price: int = 0
    time_action: str = "None"
    description: str = "None"

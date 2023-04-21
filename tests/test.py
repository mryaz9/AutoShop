from dataclasses import dataclass, astuple, asdict


@dataclass
class ColumnsUserDC:
    user_id: int
    name_user: str
    balance: float
    card_name: str
    datetime_to_buy: str


print()

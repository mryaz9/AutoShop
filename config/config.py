from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: dict[int, str]  # Список id администраторов бота

    qiwi_token: str
    crypto_token: str

    PGUSER: str
    PGPASSWORD: str
    DATABASE: str
    ip: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(
        token=env('BOT_TOKEN'),
        admin_ids=env.list('ADMIN_IDS'),
        qiwi_token=env('QIWI_TOKEN'),
        crypto_token=env('CRYPTO_BOT'),
        PGUSER=env('PGUSER'),
        PGPASSWORD=env('PGPASSWORD'),
        DATABASE=env('DATABASE'),
        ip=env('ip'),
    ))

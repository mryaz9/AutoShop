from aiocryptopay import AioCryptoPay, Networks
from glQiwiApi import QiwiP2PClient

from config.config import Config, load_config


def init_qiwi_client():
    config: Config = load_config()

    p2p = QiwiP2PClient(secret_p2p=config.tg_bot.qiwi_token,
                        shim_server_url="http://referrerproxy-env.eba-cxcmwwm7.us-east-1.elasticbeanstalk.com/proxy/p2p/")

    return p2p


def init_crypto_client():
    config: Config = load_config()
    crypto = AioCryptoPay(token=config.tg_bot.crypto_token, network=Networks.TEST_NET)

    return crypto

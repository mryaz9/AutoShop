from aiocryptopay import AioCryptoPay, Networks
from glQiwiApi import QiwiP2PClient

from config.config import Config, load_config


def init_qiwi_client():
    config: Config = load_config()

    p2p = QiwiP2PClient(secret_p2p=config.payment.qiwi_token,
                        shim_server_url="http://referrerproxy-env.eba-cxcmwwm7.us-east-1.elasticbeanstalk.com/proxy/p2p/")

    return p2p


def init_crypto_client():
    config: Config = load_config()
    crypto = AioCryptoPay(token=config.payment.crypto_token, network=Networks.MAIN_NET)

    return crypto

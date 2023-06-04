from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '2.5.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


MAINNET = 'mainnet'
TESTNET = 'testnet'
#GOERLI = 'goerli'
#PRATER = 'prater'
#SEPOLIA = 'sepolia'
#ZHEJIANG = 'zhejiang'
CARTENZ = 'cartenz'

# Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95'))
# Testnet setting
TestnetSetting = BaseChainSetting(
    NETWORK_NAME=TESTNET, GENESIS_FORK_VERSION=bytes.fromhex('10001103'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('0e65119cfae7557ec49e899a055da7b650b12db9b4908a2bb6918632f951e84e'))
# Cartenz setting
CartenzSetting = BaseChainSetting(
    NETWORK_NAME=CARTENZ, GENESIS_FORK_VERSION=bytes.fromhex('10001103'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('0e65119cfae7557ec49e899a055da7b650b12db9b4908a2bb6918632f951e84e'))
# Goerli setting
#GoerliSetting = BaseChainSetting(
#    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'),
#    GENESIS_VALIDATORS_ROOT=bytes.fromhex('043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb'))
# Sepolia setting
#SepoliaSetting = BaseChainSetting(
#    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'),
#    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d8ea171f3c94aea21ebc42a1ed61052acf3f9209c00e4efbaaddac09ed9b8078'))
# Zhejiang setting
#ZhejiangSetting = BaseChainSetting(
#    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('00000069'),
#    GENESIS_VALIDATORS_ROOT=bytes.fromhex('53a92d8f2bb1d85f62d16a156e6ebcd1bcaba652d0900b2c2f387826f3481f6f'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    CARTENZ: CartenzSetting,
    TESTNET: TestnetSetting,
#    GOERLI: GoerliSetting,
#    PRATER: GoerliSetting,
#    SEPOLIA: SepoliaSetting,
#    ZHEJIANG: ZhejiangSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )

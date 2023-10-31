from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class MongoDBConfig:
    db_name: str
    db_col: str
    pas: str
    user: str
    db_url: str


@dataclass
class Config:
    mongo: MongoDBConfig


def load_config(path: Optional[str]) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        mongo=MongoDBConfig(
            db_name=env.str("BASE_NAME"),
            db_col=env.str("COL_NAME"),
            user=env.str("DB_USER"),
            pas=env.str("DB_PASS"),
            db_url=env.str("DB_URL"),
        )
    )

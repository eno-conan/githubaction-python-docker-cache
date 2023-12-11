"""
Config file.

Setting Env Variables.
"""

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


load_dotenv()


class GlobalConfig(BaseSettings):
    title: str | None = Field(default="myapp")
    version: str | None = Field(default="1.0.0")


settings = GlobalConfig()

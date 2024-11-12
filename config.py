from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class OpenAISecret(BaseSettings):
    openai_api_key: str
    model_config = SettingsConfigDict(env_file=".env", env_prefix="")


# Instantiate the settings, automatically loading environment variables
_openaisecret = OpenAISecret()  # type: ignore

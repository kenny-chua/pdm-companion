from pydantic import BaseSettings


class OpenAISecret(BaseSettings):
    api_key: str

    class Config:
        env_file = ".env"


# Instantiate the settings, automatically loading environment variables
_openaisecret = OpenAISecret()  # type: ignore

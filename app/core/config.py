import os


class Settings:
    APP_NAME = os.getenv("APP_NAME", "FastAPI Feature Tour")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    API_KEY = os.getenv("API_KEY", "demo-api-key")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")


settings = Settings()

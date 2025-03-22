from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "yo6%q)#=o6$jc@u6388xray=tl@i07s1s9zys7etbrl5hj6add"  # کلید مخفی برای امضای توکن‌ها
    ALGORITHM: str = "HS256"  # الگوریتم رمزنگاری
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # زمان انقضای توکن

    class Config:
        env_file = ".env"

settings = Settings()

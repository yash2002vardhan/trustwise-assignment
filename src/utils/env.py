# Import BaseSettings from pydantic for environment variable management
from pydantic_settings import BaseSettings

# Define Settings class to handle environment variables
class Settings(BaseSettings):
    # Define required environment variables
    SUPABASE_URL: str        # URL for Supabase instance
    SUPABASE_ANON_KEY: str   # Anonymous key for Supabase authentication

    class Config:
        # Specify the location of the environment file
        env_file = ".env"

# Create settings instance
settings = Settings() #type: ignore

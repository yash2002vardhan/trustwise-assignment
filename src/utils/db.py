# Import Supabase client and environment settings
from supabase import create_client, Client
from src.utils.env import settings

# Function to initialize Supabase client
def get_supabase_client():
    url = settings.SUPABASE_URL
    key = settings.SUPABASE_ANON_KEY
    return create_client(url, key)

# Create global Supabase client instance
supabase : Client = get_supabase_client()

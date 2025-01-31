from supabase import create_client, Client
from src.utils.env import settings

def get_supabase_client():
    url = settings.SUPABASE_URL
    key = settings.SUPABASE_ANON_KEY
    return create_client(url, key)

supabase : Client = get_supabase_client()

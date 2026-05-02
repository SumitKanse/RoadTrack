import os
from dotenv import load_dotenv

print(f"CWD: {os.getcwd()}")
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
print(f"API_KEY from load_dotenv(): {API_KEY}")

# Try explicitly loading from backend/.env
backend_env = os.path.join("backend", ".env")
if os.path.exists(backend_env):
    print(f"Found {backend_env}, loading it...")
    load_dotenv(backend_env)
    API_KEY = os.getenv("GEMINI_API_KEY")
    print(f"API_KEY after explicit load: {API_KEY}")
else:
    print(f"{backend_env} not found from current CWD")

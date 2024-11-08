from uptime_kuma_api import UptimeKumaApi
from dotenv import load_dotenv
import os
import json

load_dotenv()

api = UptimeKumaApi(os.getenv('API_URL'))

api.login(os.getenv('ADMIN_USERNAME'), os.getenv('ADMIN_PASSWORD'))


api.disconnect()
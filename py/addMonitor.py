from uptime_kuma_api import UptimeKumaApi, MonitorType
from dotenv import load_dotenv
import time
import json
import os

api = UptimeKumaApi(os.getenv('API_URL'))

api.login(os.getenv('ADMIN_USERNAME'), os.getenv('ADMIN_PASSWORD'))

monitTime=os.getenv('MONIT_TIME') #second

f = open('list.json')
listDemo = json.load(f)
f.close()

for demoName, demoUrl in listDemo.items():
    api.add_monitor(
        type=MonitorType.HTTP,
        name=demoName,
        url=demoUrl,
        interval=monitTime,
        retryInterval=30,
        maxretries=1,
        timeout=20,
        maxredirects=0,
        parent=1, #demom2
        notificationIDList=[1] #skype bot
    )
    monitTime+=10
    print(demoName + " added to monitor.")

api.disconnect()
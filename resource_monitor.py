import psutil
from datetime import datetime


data_now = datetime.now()
now = data_now.strftime("%Y-%m-%d %H:%M:%S")

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent

with open("/Users/wolos/Documents/project-monitor/log.csv", "a") as f:
    f.write(f"{now}, {cpu}, {ram}")

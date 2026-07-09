import psutil
from datetime import datetime
import platform
import time


sys_name = platform.system()


if sys_name != 'Linux':
    path = "log.csv"
else:
    path = "/var/log/monitor/log.csv"


while True:
    data_now = datetime.now()
    now = data_now.strftime("%Y-%m-%d %H:%M:%S")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent


    try:
        with open(path, "a") as f:
            f.write(f"{now}, {cpu}, {ram}\n")
    except PermissionError:
        print("permission denied, run: sudo mkdir /var/log/monitor && chown $USER:$USER /var/log/monitor")

        time.sleep(5)
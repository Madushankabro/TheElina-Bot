import platform
import re
import socket
import sys
import time
import uuid
from datetime import datetime
from os import environ, execle, path, remove
from DewmiBot import telethn as tbot
from DewmiBot.events import register

import psutil
from pyrogram import  Client, filters, __version__


# FETCH SYSINFO

@register(pattern="^/sysinfo$")
async def give_sysinfo(event):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    cpu_len = len(psutil.Process().cpu_affinity())
    somsg = f"""**System Info of rose video player**
    
**📲PlatForm :** `{splatform}`
**💡PlatForm - Release :** `{platform_release}`
**💾PlatFork - Version :** `{platform_version}`
**⌚️Architecture :** `{architecture}`
**🔋Hosting service :** `{hostname}`
**🧭IP :** `{ip_address}`
**⏲Mac :** `{mac_address}`
**📟Processor :** `{processor}`
**💻CPU :** `{cpu_len}`
**💽CPU FREQ :** `{cpu_freq}`
    """
    await message.reply(somsg)

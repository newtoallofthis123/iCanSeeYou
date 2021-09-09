from datetime import time
from typing import final
import socket
import requests
import json

def get_host_name():
    host_name = socket.gethostname()
    return host_name

def get_time(time_zone):
    time_zone_url = f'https://www.timeapi.io/api/Time/current/zone?timeZone={time_zone}'
    headers = {
        'Content-Type': "application/json"
    }
    time_zone_page = requests.request("GET", time_zone_url, headers=headers)
    time_zone_info = json.loads(str(time_zone_page.content).replace("b'", "").replace("'", ""))
    return time_zone_info

def get_lat_long():
    geo_ip_url = "https://freegeoip.app/json/"
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }

    page = requests.request("GET", geo_ip_url, headers=headers)
    ip_info = json.loads(page.text)
    return ip_info

def engine():
    ip_info = get_lat_long()
    time_zone_info = get_time(ip_info["time_zone"])
    host_name = get_host_name()
    final_info = [ip_info, time_zone_info, host_name]
    return final_info

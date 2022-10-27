import os
import time
import sys
from requests import post
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

# strip colors if stdout is redirected
init(strip=not sys.stdout.isatty())

# LaunchDarkly SDK
import ldclient
from ldclient.config import Config

# Read required ENV variables
ha_api_key = os.getenv('HA_API_KEY')
ha_ip = os.getenv('HA_IP')
launchdarkly_key = os.getenv('LAUNCHDARKLY_KEY')

# Basic API parameters
base_url = 'http://'+ha_ip+'/api/services/light'
headers = {"Authorization": ha_api_key}
data = {"entity_id": "light.launchdarkly"}

# LaunchDarkly SDK config
ldclient.set_config(Config(launchdarkly_key))
client = ldclient.get()

print ("Evaluating LaunchDarkly feature flag.")

while True:

    # Slow down loop to not overwhelm HomeAssistant
    time.sleep(0.5)

    # Read Feature Flag
    turn_on_light = client.variation("HomeAssistantLight", {"key": "user@test.com"}, False)

    if turn_on_light == True:
        # cprint(figlet_format('lighton', font='starwars'), 'grey', 'on_white')
        response = post(
            f'{base_url}/turn_on',
            headers=headers,
            json=data
            )
        
    else:
        # cprint(figlet_format('lightoff', font='starwars'), 'white', 'on_grey')
        response = post(
            f'{base_url}/turn_off',
            headers=headers,
            json=data
            )

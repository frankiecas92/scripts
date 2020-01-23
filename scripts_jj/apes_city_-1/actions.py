#Load Custom functions
import sys
sys.path.append('../scripts/')
from lib import *
import global_actions

# Cast spell if no ammo
def client:
    if action == "check_ammo":
    spell_hotkey = "V"
    ammo_count = client.equips.equip_slot
      if ammo count < 100:
        client.spell_hotkey

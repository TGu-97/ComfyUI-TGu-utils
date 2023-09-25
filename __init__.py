import folder_paths
import os
import sys

comfy_path = os.path.dirname(folder_paths.__file__)
modules_path = os.path.join(os.path.dirname(__file__), "modules")

sys.path.append(modules_path)

from Switch import *

NODE_CLASS_MAPPINGS = {
    "LoRASwitch": LoRASwitch
}
        
NODE_DISPLAY_NAME_MAPPINGS = {
    "LoRASwitch": "LoRA Switch"
}
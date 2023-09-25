class LoRASwitch:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                    "active": ("BOOLEAN", {"default": False, "label_on": "ON", "label_off": "OFF", "forceInput": False}),
                    "model1": ("MODEL",),
                    "condition1": ("CONDITIONING",),
                    "model2": ("MODEL",),
                    "condition2": ("CONDITIONING",),
                    },
                "hidden": {"unique_id": "UNIQUE_ID"},
                }

    RETURN_TYPES = ("MODEL", "CONDITIONING")
    FUNCTION = "doit"

    CATEGORY = "TGu_util"

    def doit(self, active, model1, condition1, model2, condition2, unique_id):
        if active:
            return (model2, condition2)
        else:
            return (model1, condition1)
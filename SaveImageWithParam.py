import os
import json
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import numpy as np

class SaveImageWithParam:
    def __init__(self):
        self.output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "output")
        self.type = "output"

    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    {"images": ("IMAGE", ),
                     "PARAM": ("PARAM",),
                     "MODELNAME": ("MODELNAME",),
                    },
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }

    RETURN_TYPES = ()
    FUNCTION = "save_images_wparam"

    OUTPUT_NODE = True

    CATEGORY = "image"

    def save_images_wparam(self, images, PARAM, MODELNAME, prompt=None, extra_pnginfo=None):
        filename_prefix = MODELNAME + "_" + PARAM

        subfolder = os.path.dirname(os.path.normpath(MODELNAME))
        filename = os.path.basename(os.path.normpath(filename_prefix))

        full_output_folder = os.path.join(self.output_dir, subfolder)

        if os.path.commonpath((self.output_dir, os.path.realpath(full_output_folder))) != self.output_dir:
            print("Saving image outside the output folder is not allowed.")
            return {}

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        results = list()
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text("prompt", json.dumps(prompt))
            if extra_pnginfo is not None:
                for x in extra_pnginfo:
                    metadata.add_text(x, json.dumps(extra_pnginfo[x]))
            w, h = img.size
            file = f"{filename}_{w}_{h}.png"
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, optimize=True)
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": self.type
            });
        return { "ui": { "images": results } }

NODE_CLASS_MAPPINGS = {
    "SaveImageWithParam": SaveImageWithParam
}

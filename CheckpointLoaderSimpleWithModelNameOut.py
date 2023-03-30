import os
import sys
sys.path.append('..')
import comfy.sd
import folder_paths


class CheckpointLoaderSimpleWithModelNameOut:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                             }}
    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "MODELNAME")
    FUNCTION = "load_checkpoint_mnout"

    CATEGORY = "loaders"

    def load_checkpoint_mnout(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        return out + (ckpt_name,)

NODE_CLASS_MAPPINGS = {
    "CheckpointLoaderSimpleWithModelNameOut": CheckpointLoaderSimpleWithModelNameOut
}

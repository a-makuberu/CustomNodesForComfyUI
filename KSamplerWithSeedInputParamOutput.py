import sys
sys.path.append('..')
import comfy.samplers
from nodes import common_ksampler

class KSamplerWithSeedInputParamOutput:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"model": ("MODEL",),
                    "seed": ("SEED",),
                    "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                    "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                    "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                    "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                    "positive": ("CONDITIONING", ),
                    "negative": ("CONDITIONING", ),
                    "latent_image": ("LATENT", ),
                    "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                    }}

    RETURN_TYPES = ("LATENT","PARAM")
    FUNCTION = "samplewsipo"

    CATEGORY = "sampling"

    def samplewsipo(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        param = '{}_{}_{}_{}_{}_{}'.format(seed,steps,cfg,sampler_name,scheduler,denoise)
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise) + (param,)

NODE_CLASS_MAPPINGS = {
    "KSamplerWithSeedInputParamOutput": KSamplerWithSeedInputParamOutput
}

class SeedNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
                    }}

    RETURN_TYPES = ("SEED",)
    FUNCTION = "genseed"

    CATEGORY = "sampling"

    def genseed(self, seed):
        return (seed,)

NODE_CLASS_MAPPINGS = {
    "SeedNode": SeedNode
}

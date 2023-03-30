class CLIPTextEncodeWithTextInput:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("TEXT",), "clip": ("CLIP", )}}

    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode_wtext"

    CATEGORY = "conditioning"

    def encode_wtext(self, clip, text):
        return ([[clip.encode(text), {}]], )


NODE_CLASS_MAPPINGS = {
    "CLIPTextEncodeWithTextInput": CLIPTextEncodeWithTextInput
}

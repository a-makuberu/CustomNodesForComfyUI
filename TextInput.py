class TextInput:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True})
            },
        }

    RETURN_TYPES = ("TEXT",)
    FUNCTION = "inputtext"

    CATEGORY = "TextNode"

    def inputtext(self, text):
        return (text,)

NODE_CLASS_MAPPINGS = {
    "TextInput": TextInput
}

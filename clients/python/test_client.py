from PIL import Image
import base64
from io import BytesIO
from text_generation import Client
from huggingface_hub import InferenceClient

def b64_encode(image: Image.Image, format: str = "JPEG") -> str:
    im_file = BytesIO()
    image.save(im_file, format=format)
    im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    return base64.b64encode(im_bytes)


# client = InferenceClient("http://127.0.0.1:8081")
# client.text_generation(prompt="Write a code for snake game")

image = b64_encode(Image.open("./australia.jpg"))
client = Client("http://127.0.0.1:8081")
client.generate(
    prompt="Why is the sky blue?",
    image=image).generated_text

# result = ""
# for response in client.generate_stream("Why is the sky blue?"):
#  if not response.token.special:
#      result += response.token.text
# result

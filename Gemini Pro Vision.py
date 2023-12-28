import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import PIL.Image

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key="REPLACE WITH YOUR OWN API KEY")

img = PIL.Image.open('images/image.jpg')
model = genai.GenerativeModel('gemini-pro-vision')
Input = input("Enter query: ")


response = model.generate_content([Input, img], stream=True)
response.resolve()
print(response.text)

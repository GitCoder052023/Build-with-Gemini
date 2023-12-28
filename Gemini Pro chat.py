import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import PIL.Image

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="REPLACE WITH YOUR OWN API KEY")

model = genai.GenerativeModel('gemini-pro')

messages = []

while True:
    message = input("You: ")
    messages.append({
        "role": "user",
        "parts": [message],
    })

    response = model.generate_content(messages)

    messages.append({
        "role": "model",
        "parts": [response.text],
    })

    print("Gemini: " + response.text)

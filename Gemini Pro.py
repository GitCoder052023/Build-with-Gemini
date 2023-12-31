import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key="REPLACE WITH YOUR OWN API KEY")
model = genai.GenerativeModel('gemini-pro')
Input = input("Enter query: ")


response = model.generate_content(Input)
print(response.text)

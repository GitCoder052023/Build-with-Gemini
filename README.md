# Project Gemini
# Introduction
Gemini contains a collection of Python scripts designed for various AI-powered tasks, including text-to-speech conversion, chat interaction, image and video processing, and content generation using Google's Gemini models. 
The scripts uses Google's Gemini-pro and Gemini-pro-vision models to perform AI powered tasks like chatting, generation of content, image recognition, video recognition.
And Gemini also gives an ideas of AI projects using Google's Gemini models for students 

# Gemini Pro Vision (Cricket).py
This script is tailored for generating commentaries of cricket using Google' Gemini-pro-vision model. But note that Gemini-pro-vision directly does not support mp4 files,
so I converted each frame of mp4 video in JPG image using cv2 module of python and then I ask same query query for each frame in while loop to continuosly convert each frame of video in JPG file
So do not try to input mp4 videos directly: 

Let me me explain the code:

Importing necessary libraries: The script begins by importing the necessary libraries. These include pathlib, textwrap, google.generativeai, IPython.display, PIL.Image, cv2, and pyttsx3.



Text-to-Speech engine initialization: The pyttsx3 library is used to initialize a text-to-speech engine. The speech rate is set to 200 words per minute.



Google Generative AI configuration: The Google Generative AI is configured with an API key and the model 'gemini-pro-vision' is initialized.



Video file path: The path to the local video file is specified. This is the video for which the commentary will be generated.



Video capture: The script opens the video file and starts reading it frame by frame using the cv2.VideoCapture function.



Frame processing: For each frame, the script saves it as a JPEG image in a specified directory. The frame is then loaded as an image using the PIL library.



Commentary generation: A query is generated to instruct the AI model to write a commentary for the cricket action happening in the image. The model then generates a response based on the query and the image. The response is resolved to get the text of the commentary.



Commentary output: The commentary is printed to the console and also spoken out loud using the text-to-speech engine.



Video release: Once all frames have been processed and the end of the video is reached, the video capture is released.



This script provides an interesting application of AI in generating human-like commentary for a cricket match. It demonstrates the use of Google's Generative AI model and the pyttsx3 text-to-speech library.

# Gemini Pro Vision (Video Processing).py

Overview:
This Python script is designed to extract frames from a video file, save them as JPEG images, and then use Google's Generative AI model, Gemini Pro Vision, to generate content based on a user's query and the saved image.

Dependencies:
The script uses the following libraries:


pathlib: For manipulating filesystem paths in a way that is compatible with a variety of operating systems.

textwrap: For formatting text output.

google.generativeai: For interacting with Google's Generative AI model.

IPython.display: For displaying output in Jupyter notebooks.

PIL.Image: For opening and manipulating images.

cv2: For video capture and image processing.

How it Works

The script first configures the Generative AI model with a provided Google Cloud Platform API key.



It then defines the path to the video file and the directory where the extracted frames will be saved.



The script opens the video file using OpenCV's VideoCapture function.



It enters a loop where it reads the video frame-by-frame. If there are no more frames to read (i.e., the end of the video has been reached), it breaks the loop.



For each frame, it saves the frame as a JPEG image in the specified directory. The name of the image file is based on the current frame number.



The script then opens the saved image using PIL's Image.open function.



It prompts the user to enter a query for the current frame.



The script uses the Generative AI model to generate content based on the user's query and the image. The generated content is then printed to the console.



Once all frames have been processed, the script releases the video capture.



Purpose:
The purpose of this script is to demonstrate how to use Google's Generative AI model to generate content based on a combination of text and image input. It can be used as a starting point for developing more complex applications that require image-based content generation.

# Gemini Pro chat.py

Overview:

This Python script is designed to interact with Google's Generative AI model, specifically the 'gemini-pro' model. The purpose of this script is to facilitate a conversational interface between the user and the AI model. The user inputs a message, which is then processed by the AI model to generate a response. This interaction continues in a loop, allowing for an ongoing conversation.

Dependencies:

The script relies on several Python libraries:

- `textwrap`: This is used to format the text output.
- `google.generativeai`: This is the main library used to interact with Google's Generative AI model.
- `IPython.display`: This is used to display the output in a Jupyter notebook environment.
- `PIL.Image`: This is used for image processing, although it's not directly used in this script.

How It Works:

The script first configures the Generative AI model with the user's Google Cloud Platform (GCP) API key. It then initializes an empty list, `messages`, to store the conversation history.

The script then enters an infinite loop, where it:

1. Takes an input message from the user.
2. Appends the user's message to the `messages` list.
3. Passes the `messages` list to the AI model to generate a response.
4. Appends the AI model's response to the `messages` list.
5. Prints the AI model's response.

The `to_markdown` function is used to format the text output in Markdown style, replacing bullet points with asterisks and indenting the text.

Purpose:

The purpose of this script is to provide a simple interface for interacting with Google's Generative AI model. It can be used for a variety of applications, such as chatbots, virtual assistants, and other conversational AI applications.

# Gemini Pro Vision.py

Overview:

This Python script is designed to use Google's Generative AI to generate content based on a given input and an image. The generated content is then printed to the console. 

Dependencies:

The script uses several Python libraries:

- `pathlib`: For manipulating filesystem paths in a way that is compatible across different operating systems.
- `textwrap`: For formatting text by wrapping and indenting lines.
- `google.generativeai`: A Google library for using their Generative AI models.
- `IPython.display`: For displaying output in Jupyter notebooks.
- `PIL.Image`: For opening, manipulating, and saving different image file formats.

How it Works:

First, the script imports the necessary libraries and configures the Generative AI model with a provided Google Cloud Platform (GCP) API key. 

Next, it opens an image file located at 'images/image.jpg' using the PIL library. 

The script then initializes a Generative AI model named 'gemini-pro-vision'. 

The user is prompted to enter a query, which is stored in the variable `Input`. 

The script then calls the `generate_content` method of the model, passing in the user's query and the opened image. The `stream=True` argument indicates that the generated content should be streamed (i.e., delivered in chunks as it is generated, rather than all at once when generation is complete).

The `response.resolve()` line is used to ensure that all the content has been generated and received.

Finally, the generated content is printed to the console.

The `to_markdown` function is defined but not used in this script. It appears to be designed to convert a string of text into Markdown format, replacing bullet points (represented as '•') with asterisks and indenting all lines with '> '.

Purpose:

The purpose of this script is to demonstrate how to use Google's Generative AI to generate content based on a user's query and an image. This could be used, for example, to generate descriptions of images, to create AI-generated art based on a user's description, or for any other application that requires combining text and image inputs to generate new content.

# Gemini Pro.py

Overview:
This Python script is designed to use Google's Generative AI to generate content based on user input. The script is built using the `google.generativeai` library and is configured to use the 'gemini-pro' model.

Dependencies:
The script requires the following Python libraries:
- pathlib
- textwrap
- google.generativeai
- IPython.display

Working:
The script begins by importing the necessary libraries. It then defines a function `to_markdown` that takes a string as input, replaces all instances of '•' with '  *', and then indents the entire text string with '> '. This function is used to format the generated content in markdown style.

The script then configures the Generative AI model with a Google Cloud Platform (GCP) API key. The 'gemini-pro' model is used for content generation.

The script then prompts the user to enter a query. This query is passed to the `generate_content` method of the model, which generates a response. The generated response is then printed to the console.

Purpose:

The purpose of this script is to generate content based on user input. This can be used for a variety of applications, such as generating responses for a chatbot, creating content for a blog, or any other application where automated content generation is required. The use of the 'gemini-pro' model allows for high-quality content generation.

# Kiara.py

Dependencies:

The script utilizes the following libraries:

- `textwrap`: for text formatting
- `google.generativeai`: Google's Generative AI library
- `IPython.display`: for displaying Markdown and images in Jupyter notebooks
- `PIL.Image`: for handling images
- `pyttsx3`: a text-to-speech conversion library
  `OpenCV`: for video handling

Description:

Kiara is a ChatBot that seamlessly integrates various files, consolidating all preceding components (Gemini Pro Vision (Video Processing), Gemini Pro Vision, Gemini Pro chat, Gemini Pro). The result is an advanced interactive chatbot featuring six specialized models, each serving a unique purpose:

- Kiara TLDR: A text model
- Kiara VITA: A text + vision model(IMG)
- Kiara VLDR: A voice model
- Kiara VIVA: A voice + vision model
- Kiara VIVA (V): Voice + Vision Model(VID)
- Kiara VITA (V): Text + Vision Model(VID)

Each model is meticulously crafted to fulfill specific roles, enhancing the chatbot's versatility and user-friendliness. This integration enables users to seamlessly leverage various functionalities within a unified chatbot environment.

How it Works:

The script first initializes the text-to-speech engine and sets the voice property. Then it prints the available models and asks the user to choose one.

Depending on the user's choice, the script configures the Generative AI library with the appropriate API key and initializes the chosen model.

For the text models (Kiara TLDR and Kiara VLDR), the script enters a loop where it takes input from the user, generates a response using the model, and then prints the response. For the voice model (Kiara VLDR), the response is also spoken out loud using the text-to-speech engine.

For the vision models (Kiara VITA and Kiara VIVA), the script also opens an image file and includes it in the input to the model. The response from the model is then printed and, for the voice + vision model (Kiara VIVA), also spoken out loud.

If the script encounters a `FileNotFoundError`, it handles it by printing an error message.

Usage:

To use the script, simply run it in a Python environment where the required libraries are installed. When prompted, enter the name of the model you want to chat with. Then enter your messages when prompted. The script will print (and possibly speak) the model's responses.

# Setup and Installation of Gemini

# Setting up API KEY
 

To use the API, we have to first get an API key that you can can from here: https://ai.google.dev/tutorials/setup

After that click on “Get an API key” button and then click on “Create API key in new project”.

Copy the API key and set it as an environment variable. We are using Deepnote and it is quite easy for us to set the key with the name you want. Just go to the integration, scroll down and select environment variables.

# Dependencies of Gemini
To use these scripts, you will need to install the following dependencies:

pathlib
textwrap
google.generativeai
IPython.display
PIL.Image
cv2
pyttsx3

You will also need to configure the Google Generative AI models with your API key. And you will will need to install "Python 3.10" to use Gemini.

# follow these steps to clone Gemini:

# Clone the repository
```bash
git clone https://github.com/GitCoder052023/Gemini.git
```

# Navigate to the project directory
```bash
cd Gemini
```

# Install the dependencies
```bash
npm install Gemini
```

# Start the application
```bash
npm start Gemini
```

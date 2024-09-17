import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

myfile = genai.upload_file("media/pexels-adaptphotos-10306505.jpg")
print(f"{myfile=}")

model = genai.GenerativeModel("gemini-1.5-flash")
result = model.generate_content(
    [myfile, "\n\n", "Can you tell me about this photo? How can I recreate she shot?"]
)
print(f"{result.text=}")

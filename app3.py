from github import Github
import subprocess
import os
import openai
from langchain.llms import AzureOpenAI
from dotenv import load_dotenv
from azure.identity import DeviceCodeCredential
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
import requests
import re
import json

def find_longest_substring(input_string):
    start_index = input_string.find('{')  # Find the first '{' from the beginning
    end_index = input_string.rfind('}')  # Find the last '}' from the end

    if start_index != -1 and end_index != -1 and start_index < end_index:
        longest_substring = input_string[start_index:end_index + 1]
        return longest_substring
    else:
        return None
def save_file(save_path, name_of_file, content):
    content = content.replace("\\n", "\n")
    completeName = os.path.join(save_path, name_of_file)
    file1 = open(completeName, "w")
    file1.write(content)
    file1.close()
def read_and_append(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""

def generate_prompt(local_directory):
    # File paths for the three files
    file1_path = os.path.join(local_directory, "part1.txt") # Replace with the actual path to file1
    file2_path = os.path.join(local_directory, "s2t.java")  # Replace with the actual path to file2
    file3_path = os.path.join(local_directory, "part2.txt")  # Replace with the actual path to file3

    # Initialize an empty string to store the combined text
    prompt = ""

    # Read and append content from each file
    prompt += read_and_append(file1_path)
    prompt += "\n"  # Add a newline between file contents
    prompt += read_and_append(file2_path)
    prompt += "\n"  # Add a newline between file contents
    prompt += read_and_append(file3_path)

    return prompt

def call_gen_ai_model(message):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    messages = [
        {
            "role": "system", "content": "You are an intelligent assistant."
        }
    ]

    reply = ""

    if message:
        messages.append(
            {
                "role": "user", "content": message
            }
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature = 0
        )
        reply = chat.choices[0].message.content

    return reply

def get_new_file_content(text):
    print(text)
    last_match = find_longest_substring(text)




    if last_match is not None:
        print(last_match)
        try:
            # Define a second regular expression pattern to match the "new_content" field
            # second_pattern = r'"new_content":\s*"([^"]*)"'
            # second_pattern = r'"new_content":\s*"((?:[^"]|\\")*)"'
            second_pattern = r'"new_content"\s*:\s*"(.*?)(?<!\\)"'

            # Search for the pattern in the JSON-like string
            match = re.search(second_pattern, last_match)

            # Check if a match is found
            if match:
                print("success. found new content value.")
                new_content_value = match.group(1)
                return new_content_value
            else:
                print("failure. no 'new_content' field found in the JSON-like string.")
                return ""

        except:
            print("failure. found matching regex but could not parse into json")
            return ""
    else:
        print("failure. cound find matching regex")
        return ""


if __name__ == "__main__":
    load_dotenv()

    repo_name = "test"
    local_git_directory = r"C:\Users\I871655\OneDrive - SAP SE\Desktop\git"

    # Local directory where you want to save the repository
    local_directory = os.path.join(local_git_directory, repo_name)

    prompt = generate_prompt(local_directory)

    # response = call_gen_ai_model(prompt)
    response = read_and_append(os.path.join(local_directory, "response.txt"))
    new_content = get_new_file_content(response)

    print("parsed: " + new_content)

    save_file(local_directory, "s2t_modified.java", new_content)
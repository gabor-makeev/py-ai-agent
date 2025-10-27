import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

  try:
    if not abs_file_path.startswith(abs_working_dir):
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
      return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(abs_file_path, "r") as f:
      file_content_string = f.read()

      if len(file_content_string) > MAX_CHARS:
        file_content_string = f"{file_content_string[:MAX_CHARS]} [...File '{file_path}' truncated at 10000 characters]"

    return file_content_string
  except Exception as e:
    return f"Error: {e}"
  
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Shows content of a specified file, limited to 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
              type=types.Type.STRING,
              description="The path to the file to show content of, relative to the working directory.",
            ),
        },
    ),
)
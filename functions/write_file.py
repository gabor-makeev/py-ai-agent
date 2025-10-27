import os
from google.genai import types

def write_file(working_directory, file_path, content):
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

  if not abs_file_path.startswith(abs_working_dir):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
  
  try:
    file_path_dirs = os.path.dirname(abs_file_path)

    if not os.path.exists(file_path_dirs):
      os.makedirs(file_path_dirs)
    
    with open(abs_file_path, "w") as f:
      f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
    return f'Error: {e}'
  
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes specified content to a specified file, constrained to the working directory. If the file path provided includes directories that don't exist, creates the required directories. If the file specified in the file path doesn't exist, creates the required file. Outputs a successful write operation to the specified file and the number of characters written.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
              type=types.Type.STRING,
              description="The real or expected path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
              type=types.Type.STRING,
              description="The content to write to the specified file."
            )
        },
    ),
)
  
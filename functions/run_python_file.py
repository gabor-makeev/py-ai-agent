import os
import subprocess
from config import SUBPROCESS_TIMEOUT
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

  if not abs_file_path.startswith(abs_working_dir):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  
  if not os.path.exists(abs_file_path):
    return f'Error: File "{file_path}" not found.'
  
  if not abs_file_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'

  try:
    completed_process = subprocess.run(
      args=["python", abs_file_path, *args], 
      capture_output=True, 
      timeout=SUBPROCESS_TIMEOUT,
      cwd=abs_working_dir
    )

    output = []

    if completed_process.stdout:
      output.append(f'STDOUT: {completed_process.stdout}')

    if completed_process.stderr:
      output.append(f'STDERR: {completed_process.stderr}')

    if not completed_process.returncode == 0:
      output.append(f'Process exited with code {completed_process.returncode}')

    return "\n".join(output) if output else "No output produced."
  except Exception as e:
    return f"Error: executing Python file: {e}"
  
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python script in a specified python file, constrained to the working directory. If specified, includes arguments for the python script. If arguments are not provided, an empty list is used for arguments by default. Returns the output of the completed process, the output includes the stdout and stderr if available. If the return code of the completed process is not 0, the output includes the return code the process exited with. If the output doesn't include stdout, stderr and the code the process exited with, returns 'No output produced.'.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
              type=types.Type.STRING,
              description="The path to the python file to be run, relative to the working directory.",
            ),
            "args": types.Schema(
              type=types.Type.ARRAY,
              items=types.Schema(
                type=types.Type.STRING,
                description="An argument to be passed to the python script."
              ),
              description="The array of arguments to be passed to the python script.",
            )
        },
    ),
)
import os
import subprocess
from config import SUBPROCESS_TIMEOUT

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
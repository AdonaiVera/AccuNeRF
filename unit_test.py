import os
import uuid
import subprocess

def process_data(file_video, folder_output):
    print(file_video)
    print(folder_output)
    # First step, process video
    command = "ns-process-data"
    
    args = ["video", "--data", file_video, "--output-dir", folder_output]

    # Run the command
    process = subprocess.run([command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output and error messages
    output = process.stdout

    # Check for errors and handle them
    if process.returncode != 0:
        print("Error running command:", output)
        return False
    else:
        print("Command output:", output)
        return True

def create_model(MODEL, DATA_PATH, DATA_OUTPUT):
    # Output model
    DATA_OUTPUT = "{}/output".format(DATA_OUTPUT)

    # Construct the command and arguments
    command = "ns-train"
    args = [MODEL, "--data", DATA_PATH, "--pipeline.model.predict-normals", "True", "--output-dir", DATA_OUTPUT, "--vis", "tensorboard"]

    # Execute the command
    process = subprocess.run([command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture the output and errors
    output = process.stdout

    # Handle the results
    if process.returncode != 0:
        print("Error running command:", output)
        return False
    else:
        print("Command output:", output)
        return True

def convert_ply_to_js(ply_file):
    command = "./PotreeConverter"

    args = [ply_file, "--overwrite"]

    # Execute the command
    process = subprocess.run([command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture output and errors
    output = process.stdout

    # Check for errors and handle them
    if process.returncode != 0:
        print("Error running PotreeConverter:", output)
        return False
    else:
        print("PotreeConverter output:", output)
        return True



example= "pointclouds/base_accunerf/point_cloud.ply"
convert_ply_to_js(example)
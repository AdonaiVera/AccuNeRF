from flask import Flask, request
import os
import uuid
import subprocess

app = Flask(__name__)

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

def create_point_cloud(config_path, output_dir):
    print(config_path)
    print(output_dir)
    # Define the command and its arguments
    command = "ns-export"

    args = ["pointcloud", "--load-config", config_path, "--output-dir", output_dir]

    # Execute the command
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


@app.route('/upload_video', methods=['POST'])
def upload_video():
    video = request.files['video']
    model = request.form['model']  # Retrieve the 'model' variable
    print("GET REQUEST")
    print(model)
    if video:
        random_uuid = str(uuid.uuid4())

        filename = '{}.mp4'.format(random_uuid)

        folder_ply = os.path.join('pointclouds/', random_uuid)
        if not os.path.exists(folder_ply):
            os.makedirs(folder_ply) 

        file_video = os.path.join(folder_ply, filename)
        video.save(file_video)
        
        folder_database = "{}/database".format(folder_ply)
        if not os.path.exists(folder_database):
            os.makedirs(folder_database) 

        print("[INFO] Init preprocessing the video")
        # Process video with COLMAP
        if process_data(file_video, folder_database) == False:
            return 'Issue preprocessing the video'
        print("[INFO] Finished processing data")

        print("[INFO] Init creating model")
        # Create model 
        if create_model(model, folder_database, folder_ply) == False:
            return 'Issue pre-processing the video'
        
        # Create pointcloud
        folder_config ="{}/output/database/{}".format(folder_ply, model)

        print(folder_config)
        if os.path.exists(folder_config):
            name_config = os.listdir(folder_config)[0] 
            config_path = "{}/{}/config.yml".format(folder_config, name_config)
        else:
            print('Issue pre-processing the video')
            return 'Issue creating pointcloud'
        if create_point_cloud(config_path, folder_ply) == False:
            return 'Issue pre-processing the video'
    
        # Convert ply file to .js format to display in Potree
        print("[INFO] Finished creating model")


        return 'Video uploaded successfully.'
    
    return 'No video uploaded.'

if __name__ == '__main__':
    app.run(debug=True, port=1235) 
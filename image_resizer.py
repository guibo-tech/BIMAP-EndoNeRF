import os
from PIL import Image

# Set the input and output folder paths
input_folder = '../reco_0003/depth/'
output_folder = '../reco_0003/depth_resized'

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        file_path = os.path.join(input_folder, filename)

        # Open the image using PIL
        image = Image.open(file_path)

        # Check the dimensions of the image
        width, height = image.size
        if width == 800 and height == 600:
            # Resize the image to 576x768
            resized_image = image.resize((768, 576))

            # Generate the output file path
            output_file_path = os.path.join(output_folder, filename)

            # Save the resized image
            resized_image.save(output_file_path)

            print(f"Converted {filename} to 576x768 and saved as {output_file_path}")
        else:
            print(f"Skipped {filename} as it does not have dimensions 600x800")

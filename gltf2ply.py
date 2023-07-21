import os
import aspose.threed as a3d # install aspose from homepage
import argparse

# The provided Python script is a command-line tool that converts 3D glTF files to PLY format
# using the Aspose.ThreeD library. Users can run the script from the command line,
# passing the input and output directories as --input-dir and --output-dir arguments.
# The script loads glTF scenes from the input directory, converts them to PLY format,
# and saves them in the output directory. This provides an efficient way to batch convert
# glTF files to PLY format for further processing.

# Example usage
# python gltf2ply.py --input-dir data/pc_gltf --output-dir data/pc_ply

def convert_gltf_to_ply(input_dir, output_dir):
    # Iterate over files in the directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".gltf"):
            # Load GLTF scene from file
            gltf_file = os.path.join(input_dir, filename)
            scene = a3d.Scene.from_file(gltf_file)

            # Generate output PLY file name
            ply_file = os.path.splitext(filename)[0] + ".ply"
            ply_path = os.path.join(output_dir, ply_file)

            # Save scene as PLY file
            scene.save(ply_path)

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Convert 3D gltf to ply format")

    # Add arguments for input_dir and output_dir
    parser.add_argument("--input-dir", dest="input_dir", required=True, help="Directory path containing GLTF files")
    parser.add_argument("--output-dir", dest="output_dir", required=True, help="Output directory to save PLY files")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to convert GLTF to PLY
    convert_gltf_to_ply(args.input_dir, args.output_dir)


# # Directory path containing GLTF files
# input_dir = "data/pc_gltf"
# output_dir = "data/pc_ply"
#
# # Iterate over files in the directory
# for filename in os.listdir(input_dir):
#     if filename.endswith(".gltf"):
#         # Load GLTF scene from file
#         gltf_file = os.path.join(input_dir, filename)
#         scene = a3d.Scene.from_file(gltf_file)
#
#         # Generate output PLY file name
#         ply_file = os.path.splitext(filename)[0] + ".ply"
#         ply_path = os.path.join(output_dir, ply_file)
#
#         # Save scene as PLY file
#         scene.save(ply_path)


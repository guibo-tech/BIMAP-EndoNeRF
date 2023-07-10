import os
import aspose.threed as a3d

# This script converts 3D gltf to ply format
# It converts all files in the folder.

# install aspose #

# Directory path containing GLTF files
input_dir = "data/pc_gltf"
output_dir = "data/pc_ply"

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

# import aspose.threed as a3d
#
# scene = a3d.Scene.from_file("frame_000000_pc.gltf")
# scene.save("frame_000000_pc-2.ply")
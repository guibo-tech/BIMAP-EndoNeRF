import numpy as np
from PIL import Image
import open3d as o3d
import os


def create_3d_obj(rgb_image, depth_image, image_path, depth=10):
    depth_o3d = o3d.geometry.Image(depth_image)
    image_o3d = o3d.geometry.Image(rgb_image)
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(image_o3d, depth_o3d, convert_rgb_to_intensity=False)
    w = int(depth_image.shape[1])
    h = int(depth_image.shape[0])

    camera_intrinsic = o3d.camera.PinholeCameraIntrinsic()
    camera_intrinsic.set_intrinsics(w, h, 500, 500, w/2, h/2)

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image, camera_intrinsic)

    print('normals')
    pcd.normals = o3d.utility.Vector3dVector(
        np.zeros((1, 3)))  # invalidate existing normals
    pcd.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=30))
    pcd.orient_normals_towards_camera_location(
        camera_location=np.array([0., 0., 1000.]))
    pcd.transform([[1, 0, 0, 0],
                   [0, -1, 0, 0],
                   [0, 0, -1, 0],
                   [0, 0, 0, 1]])
    pcd.transform([[-1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    print('run Poisson surface reconstruction')
    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        mesh_raw, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
            pcd, depth=depth, width=0, scale=1.1, linear_fit=True)

    voxel_size = max(mesh_raw.get_max_bound() - mesh_raw.get_min_bound()) / 256
    print(f'voxel_size = {voxel_size:e}')
    mesh = mesh_raw.simplify_vertex_clustering(
        voxel_size=voxel_size,
        contraction=o3d.geometry.SimplificationContraction.Average)

    # vertices_to_remove = densities < np.quantile(densities, 0.001)
    # mesh.remove_vertices_by_mask(vertices_to_remove)
    bbox = pcd.get_axis_aligned_bounding_box()
    mesh_crop = mesh.crop(bbox)
    if not os.path.exists('./gltf_files'):
        os.mkdir('./gltf_files')
        print("Folder for gltf_files has been created.")
    gltf_path = f'./gltf_files/{image_path}.gltf'
    o3d.io.write_triangle_mesh(
        gltf_path, mesh_crop, write_triangle_uvs=True)
    print(f"{gltf_path} has been created.\n")

# Get the absolute path of the script
script_path = os.path.abspath(__file__)

# Extract the directory name
script_directory = os.path.dirname(script_path)

directory = script_directory + r'\data'
images_dir = directory + r'\images\\'
depth_dir = directory + r'\depth\\'
for file in os.listdir(images_dir):
    image = Image.open(images_dir+file)
    rgb_np = np.array(image).astype('uint8')
    depth_file = depth_dir + os.path.splitext(os.path.basename(file))[0] + '.png'
    depth_img = Image.open(depth_file)
    depth_np = np.array(depth_img).astype('uint8')
    create_3d_obj(rgb_np, depth_np, file)

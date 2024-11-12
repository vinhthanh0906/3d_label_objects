import open3d as o3d
import pyvista as pv
import numpy as np

# Paths to your ShapeNet .obj files
obj_files = [
    '/Users/nguyenthanhvinh/Desktop/MS-DBSCAN/evaluation_dataset/SIGGRAPH_2006/brick_part01.obj',
    '/Users/nguyenthanhvinh/Desktop/MS-DBSCAN/evaluation_dataset/SIGGRAPH_2006/brick_part02.obj',
    '/Users/nguyenthanhvinh/Desktop/MS-DBSCAN/evaluation_dataset/SIGGRAPH_2006/brick_part03.obj',
    '/Users/nguyenthanhvinh/Desktop/MS-DBSCAN/evaluation_dataset/SIGGRAPH_2006/brick_part04.obj',
    '/Users/nguyenthanhvinh/Desktop/MS-DBSCAN/evaluation_dataset/SIGGRAPH_2006/brick_part05.obj',
    '/Users/nguyenthanhvinh/Desktop/MS-DBSCAN/evaluation_dataset/SIGGRAPH_2006/brick_part06.obj',
]

# List to store all points
all_points = []

# Load each surface and sample points
for obj_file in obj_files:
    # Load the .obj file
    mesh = o3d.io.read_triangle_mesh(obj_file)
    
    # Check if the mesh is valid
    if mesh.is_empty():
        print(f"Mesh from {obj_file} is empty or invalid.")
        continue
    
    # Sample points uniformly on the surface
    num_points = 10000  # Number of points to sample
    points = mesh.sample_points_uniformly(number_of_points=num_points)
    
    # Convert the point cloud to a numpy array
    point_cloud_np = np.asarray(points.points)
    
    # Append points to the list
    all_points.append(point_cloud_np)

# Concatenate all points into a single numpy array
merged_points = np.vstack(all_points)

# Create a PyVista point cloud from the merged numpy array
merged_point_cloud = pv.PolyData(merged_points)

# Initialize a Plotter
p = pv.Plotter()
p.background_color = "black"

# Add the merged point cloud to the plot
p.add_mesh(merged_point_cloud, color='cyan', point_size=5, render_points_as_spheres=True)

# Add title and show the plot
p.add_title("Completed Brick", font_size=16)
p.show()
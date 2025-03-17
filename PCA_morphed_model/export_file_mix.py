# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_export_file_mix.ipynb.

# %% auto 0
__all__ = ['export_file']

# %% ../nbs/05_export_file_mix.ipynb 1
import trimesh
from .export_key import export_key_file
import numpy as np
import glob
import os

# %% ../nbs/05_export_file_mix.ipynb 2
def export_file (input_dir: str, # input directory
                output_dir: str, # output directory
                coordinates_pos: list[list[float]], #new coordinates with positive k.std 
                coordinates_neg: list[list[float]], #new coordinates with negetive k.std 
                coordinates_mean: list[list[float]] , #new coordinates with k = 0 
                shells: np.array , #shells of morphed model, each shell enclosed by nodes
                id_nodes: list[int], # id of nodes of morphed model
                k: int):  #desired scaling factor 
    """ This function export .stl or .key file for three kind of coordinates (positive, negative, mean)"""

    all_morphed_file_pathes = [f for f in glob.glob(os.path.join(input_dir, "*")) if os.path.isfile(f)]     # All files (excluding folders)
    
    file_extension = os.path.splitext(all_morphed_file_pathes[0])[1].lower()
    if file_extension == ".stl":
        # create stl file
        vertices_pos = np.array(coordinates_pos)
        vertices_neg = np.array(coordinates_neg)
        vertices_mean = np.array(coordinates_mean)
        faces = shells
        mesh_pos = trimesh.Trimesh(vertices=vertices_pos, faces=faces)
        mesh_neg = trimesh.Trimesh(vertices=vertices_neg, faces=faces)
        mesh_mean = trimesh.Trimesh(vertices=vertices_mean, faces=faces)

        # Define filenames dynamically based on data type
        filenames = {
            "pos": f"mesh_{k}_pos_std.stl",
            "neg": f"mesh_{k}_neg_std.stl",
            "mean": f"mesh_mean.stl",
        }

        # Generate the full file path dynamically
        # Define output paths
        output_paths = {
            "pos": os.path.join(output_dir, filenames["pos"]),
            "neg": os.path.join(output_dir, filenames["neg"]),
            "mean": os.path.join(output_dir, filenames["mean"]),
        }

        # Export STL files with appropriate names
        mesh_pos.export(output_paths["pos"])
        mesh_neg.export(output_paths["neg"])
        mesh_mean.export(output_paths["mean"])


    elif file_extension == ".key" or ".k":
        #export .key file for quad shells
        filenames = {
            "pos": f"mesh_{k}_pos_std.key",
            "neg": f"mesh_{k}_neg_std.key",
            "mean": f"mesh_mean.key",
        }
        # Generate the full file path dynamically
         # Define output paths
        output_paths = {
            "pos": os.path.join(output_dir, filenames["pos"]),
            "neg": os.path.join(output_dir, filenames["neg"]),
            "mean": os.path.join(output_dir, filenames["mean"]),
        }
        #file_name = output_path
        mesh_pos = export_key_file(coordinates_pos , shells, id_nodes,output_paths["pos"])
        mesh_neg = export_key_file(coordinates_neg , shells, id_nodes,output_paths["neg"])
        mesh_mean = export_key_file(coordinates_mean , shells, id_nodes,output_paths["mean"])
    
    return mesh_pos, mesh_neg, mesh_mean 

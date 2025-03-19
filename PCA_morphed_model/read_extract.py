# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_read_extract.ipynb.

# %% auto 0
__all__ = ['read_extract_nodes_shells']

# %% ../nbs/01_read_extract.ipynb 2
import glob
import os
import numpy as np
from .extract_NSH_stl_key import extract_nodes_shells_mix_stl_key



# %% ../nbs/01_read_extract.ipynb 3
def read_extract_nodes_shells(input_dir:str  ):  # input directory
    """Reads STL or KEY files from a directory and extracts node coordinates and shell elements."""
    
    all_morphed_file_pathes = [f for f in glob.glob(os.path.join(input_dir, "*")) if os.path.isfile(f)]     # All files (excluding folders)

    # extract the cordinates of nodes of all morphed files
    nodes_all_morphed_files = []
    shells = np.empty(0)
    id_nodes = []
    data_array = np.empty(0)

    if all_morphed_file_pathes != []:
        for file_path in all_morphed_file_pathes:
            nodes1 = extract_nodes_shells_mix_stl_key(file_path)[0]
            
            nodes_without_id = [sublist[1:] for sublist in nodes1]    # extract nodes cordinates (x, y, z)
            id_nodes = [sublist[0] for sublist in nodes1]             # extract id of nodes
            nodes_list = [item for sublist in nodes_without_id for item in sublist]     # Convert to one list
            nodes_all_morphed_files.append(nodes_list)                # get nodes of all morphed files
        
        file_extension = extract_nodes_shells_mix_stl_key(all_morphed_file_pathes[-1])[2]
        print(f"{len(all_morphed_file_pathes)} {file_extension} files were read")
        shells = extract_nodes_shells_mix_stl_key(all_morphed_file_pathes[-1])[1]
        data_array = np.array(nodes_all_morphed_files) 
        
    return data_array, shells, id_nodes
    

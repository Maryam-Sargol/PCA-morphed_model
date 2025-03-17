# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_extract_NSH_stl_key.ipynb.

# %% auto 0
__all__ = ['extract_nodes_shells_mix_stl_key']

# %% ../nbs/00_extract_NSH_stl_key.ipynb 1
import numpy as np
import os
import trimesh

# %% ../nbs/00_extract_NSH_stl_key.ipynb 2
def extract_nodes_shells_mix_stl_key (file_path : str): # path of morphed files
    """ extracts nodes and shells from given files, only .stl and .key files are accepted """

    file_extension = os.path.splitext(file_path)[1].lower()
 

    if file_extension == ".stl":
        #"Processing an STL file"
        model = trimesh.load_mesh(file_path)
        shells = np.array(model.faces)
        nodes = np.array(model.vertices)
        nodes_list = nodes.tolist()
        # Generating IDs starting from 1
        # Create a list with IDs attached to each sublist
        ids = list(range(1, len(nodes_list) + 1))
        # Attach IDs to each row
        nodes_with_ids = [[id] + row for id, row in zip(ids, nodes_list)]
   
   
    elif file_extension == ".key" or ".k":
        #"Processing a KEY file"

        # Flags to track sections
        in_node_section = False
        in_element_section = False
    
        nodes_with_ids = []
        shells = []

        with open(file_path, 'r') as file:
            for line in file:
                if "*NODE" in line:  # Check for the keyword
                    in_node_section = True
                    in_element_section = False
                    continue  # Skip the current line containing "START"

                elif "*ELEMENT_SHELL" in line:
                    in_node_section = False
                    in_element_section = True
                    continue

                    # Process lines in the *NODE section
                if in_node_section:

                    first_chunk = line[:8]
                    remaining_chunks = [line[i:i + 16] for i in range(8, len(line), 16)]

                    try:
                        id, x, y, z = float(first_chunk), float(remaining_chunks[0]), float(remaining_chunks[1]), float(
                            remaining_chunks[2]),
                        nodes_with_ids.append((id, x, y, z))



                    except (ValueError, IndexError):
                    #Skip lines that don't contain valid coordinate data
                        continue

                    # Process lines in the *ELEMENT_SHELL section
                elif in_element_section:

                    chunks = [line[i:i + 8] for i in range(0, len(line), 8)]
                    try:
                        i, n_fix, p1, p2, p3, p4 = chunks[0], chunks[1], chunks[2], chunks[3], chunks[4], chunks[5]
                        shells.append((i, n_fix, p1, p2, p3, p4))              

                
                    except (ValueError, IndexError):
                    # Skip lines that don't contain valid coordinate data
                        continue
    
    
    else:
        print("Unsupported file format.")
        print(file_extension + ' is not accepted')


    nodes_array = np.array(nodes_with_ids)
    shells_array = np.array(shells)
    

    return  nodes_array, shells_array, file_extension

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_main_pca.ipynb.

# %% auto 0
__all__ = ['input_dir', 'output_dir', 'data_array', 'shells', 'id_nodes', 'coefficients', 'scores', 'explained_variance',
           'pca_mean', 'pca_index', 'k', 'coordinates_pos', 'coordinates_neg', 'coordinates_mean', 'mesh_pos',
           'mesh_neg', 'mesh_mean']

# %% ../nbs/06_main_pca.ipynb 1
from .read_extract import read_extract_nodes_shells
from .pca import run_PCA 
from .STD import desired_STD
from .export_file_mix import export_file

# %% ../nbs/06_main_pca.ipynb 2
#input_dir = './geometry_data_example'     # there are .key files
input_dir = './geometry_data_example/triangular_morphed_models'       # there are .stl files
output_dir = './result'


# %% ../nbs/06_main_pca.ipynb 3
data_array, shells, id_nodes = read_extract_nodes_shells(input_dir)

# %% ../nbs/06_main_pca.ipynb 4
# run pca

coefficients,scores, explained_variance, pca_mean= run_PCA(data_array)

# %% ../nbs/06_main_pca.ipynb 5
# apply desired standard deviations
pca_index = 0  # PCA1
k = 3  # Number of standard deviations

coordinates_pos, coordinates_neg, coordinates_mean = desired_STD(coefficients, pca_mean, scores, pca_index, k )

# %% ../nbs/06_main_pca.ipynb 6
mesh_pos, mesh_neg, mesh_mean = export_file (input_dir,output_dir, coordinates_pos, coordinates_neg, coordinates_mean , shells, id_nodes,k)

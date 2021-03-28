import Bio
import numpy as np
from Bio import SubsMat

PAM = open("/Users/parkerhicks/Desktop/Senior_Thesis/Notebook/PAM_250.txt").read()

print(Bio.SubsMat.read_text_matrix(data_file="/Users/parkerhicks/Desktop/Senior_Thesis/Notebook/PAM_250.txt"))

# Try np.where()
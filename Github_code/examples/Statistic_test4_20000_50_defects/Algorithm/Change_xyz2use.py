import pandas as pd
from scipy.io import savemat


def read_xyz(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    comment = lines[1].strip()  # Read comment line
    data = []

    # Skip the first two lines and parse the following atomic information
    for line in lines[2:]:
        parts = line.split()
        atom_Id, atom_type, x, y, z, coor = map(float, parts[0:6])
        data.append([atom_Id, atom_type, x, y, z, coor])

    df = pd.DataFrame(data, columns=['Atom_Id', 'Atom_Type', 'X', 'Y', 'Z', 'Coordination'])
    return df, comment


def xyz_to_mat(xyz_file_path, mat_file_path):
    df, comment = read_xyz(xyz_file_path)

    # Convert DataFrame to dictionary with numpy arrays
    mat_data = df.to_numpy()

    # Save to .mat file
    savemat(mat_file_path, {'test1': mat_data})
    print(f"Saved {mat_file_path}")
    return comment




import main_detect
import argparse
from Algorithm import Change_xyz2use

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enter your XYZ particle data file path.')
    parser.add_argument('xyz_file_path', type=str, help='Path to the input XYZ file.')
    parser.add_argument('--amplification_coefficient4abc', type=float, default=15.9427,
                        help='Amplification coefficient for point defects a,b,c (default: 15.9427)')
    parser.add_argument('--amplification_coefficient4de', type=float, default=13.8229,
                        help='Amplification coefficient for point defects d,e (default: 13.8229)')
    parser.add_argument('--atom_type', type=float, default=1,
                        help='Type of atom to be detected (default: 1)')
    parser.add_argument('xyz_file_output_path', type=str, help='Path to the output XYZ file.')

    args = parser.parse_args()
    # Show user command line reminder
    print("Detection of complex point defects in  beta-gallium oxide:")
    print(f"  XYZ File: {args.xyz_file_path}")
    print(f"  Amplification Coefficient for a b c defect type : {args.amplification_coefficient4abc}")
    print(f"  Amplification Coefficient for d e defect type : {args.amplification_coefficient4de}")
    print(f"  XYZ output File : {args.xyz_file_output_path}")
    print(f"  Atom_type : {args.atom_type}")


    # xyz_file_path = './use_file.xyz'

    mat_file_path = './n_0620_t1.mat'
    message_comment = Change_xyz2use.xyz_to_mat(args.xyz_file_path, mat_file_path)
    print('message_comment: ', message_comment)
    main_detect.main(args.xyz_file_output_path, args.amplification_coefficient4de, args.amplification_coefficient4de,
                     args.atom_type, message_comment)

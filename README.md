# ARDF_PSO&K-Means for defects detection in $\beta$-Ga2O3

## Description

This project contain one main branch for our essay, Github_code. The Github_code mainly contained the algorithm we designed: 1, detective algorithm; 2. PSO algorithm for amplification coefficient. See mor details in Refs. [1].

## Github_code

### ARDF algorithm

This algorithm contained the curves of database $\text V_{\text ia}^{\text Ga}$, $\text V_{\text ib}^{\text Ga}$, $\text V_{\text ic}^{\text Ga}$, $\text Ga_{\text iad}$, $\text Ga_{\text iae}$, Ori data and some additional data. Meanwhile, the Algorithm package contained the contents of ***<u>PSO</u>*** algorithm for `amplification coefficient` $\alpha$, and the details of ***<u>K-MC  clustering</u>***. The output is saved in a .xyz file.

## How to:

### Create a datafile in .xyz form

1、Get your .xyz file through lammps\Ovito\VASP\Material Studio 

> [!NOTE]
>
> For the test procedure, the descriptors should be in the order: `atom_id`, `atom_type`, `X`, `Y`, `Z`, `Coordination`

2、Run run_file.py directly. Write something like:

```python
python3.11.0 run_file.py /path/to/input.xyz /path/to/output.xyz 
```

- `/path/to/input.xyz` should be changed to the test file directory, while `/path/to/output.xyz` refers to the output result directory.

- Amplification coefficient for split vacancy defects ($\text V_{\text ia}^{\text Ga}$, $\text V_{\text ib}^{\text Ga}$, $\text V_{\text ic}^{\text Ga}$) and split interstitial defects ( $\text Ga_{\text iad}$, $\text Ga_{\text iae}$) could be modified through:

  ```python
  python3.11.0 run_file.py ./use_file.xyz --amplification_coefficient4abc 'Y' --amplification_coefficient4de 'X'
  ```

  The default values of amplification coefficient`(15.9427 for type a, b & c, 13.8829 for type d&e)` are usually sufficient to get a good accuracy after PSO algorithm for them.

- For `atom type`, the default value is set as 1. While it could be changed through :

  ```python
  python3.11.0 run_file.py ./use_file.xyz --amplification_coefficient4abc 'Y' --amplification_coefficient4de 'X' --atom_type 'num'
  ```

  `--atom_type 'num'` stands for the atom type you need to change for your tests.

## References

If you use this code to run a defects detection process, please cite:

1. Yan M, Zhao J, Djurabekova F, et al. Generalized Algorithm for Recognition of Complex Point Defects in Large-Scale β-Ga2O3[J]. arXiv preprint arXiv:2401.15920, 2024.[ https://doi.org/10.48550/arXiv.2401.15920](https://doi.org/10.48550/arXiv.2401.15920)

## Contributors

- Mengzhi Yan (main)

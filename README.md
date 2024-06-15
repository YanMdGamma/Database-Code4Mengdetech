# README

## Description

This project contain one main branch for our essay, Github_code. The Github_code mainly contained the algorithm we designed: 1, the automatic method to produce test systems we need; 2, the data processing procedure; 3, detective algorithm. 

## Github_code

### automatic method for procedure tests

This part of the code is consisted with several ***<u>database</u>***, which contains atoms less than 90. $\text V_{\text ia}^{\text Ga}$, $\text V_{\text ib}^{\text Ga}$, $\text V_{\text ic}^{\text Ga}$, $\text Ga_{\text iad}$, $\text Ga_{\text iae}$, Ori. Then we designed the algorithm by defining the `magnification`, `defects ratio` and the `position of deferent database blocks`.

### data processing procedure

In order to guarantee the data we use is stable and doable, we need to use the `average location` of ***<u>stable data frame</u>*** after lammps tests other than just one frame of the lammps. So we use the algorithm to averaging each test. We use the positions of atoms from .txt, which can be easily formed by .dat from Ovito. These stable positions are got from numerous stable timesteps. After the origin .txt files are obtained, the averaging process is applying, final data is generated and saved in a .csv file.

### detective algorithm

This algorithm contained the curves of database $\text V_{\text ia}^{\text Ga}$, $\text V_{\text ib}^{\text Ga}$, $\text V_{\text ic}^{\text Ga}$, $\text Ga_{\text iad}$, $\text Ga_{\text iae}$, Ori data and some additional data. Meanwhile, the Algorithm package contained the contents of ***<u>PSO</u>*** algorithm for `amplification coefficient` $\alpha$, and the details of ***<u>K-MC  clustering</u>***. The output is saved in a .txt file.

## How to:

### Construct large tests from small data blocks

The `if __name__ == "__main__":` is used for generate large test sets.

1. Change the `examples_num` to the number you need for the number of your tests.

   ```python
   examples_num = 'num' # the number you want
   ```

2. Change the copy_files(`f'/home/ps/YMZ/py_tests_mul/ori/test_ori'`, `f'/home/ps/YMZ/py_tests_mul/ori/ori'`)

   ```python
   copy_files(f'/home/ps/YMZ/py_tests_mul/ori/test_ori', f'/home/ps/YMZ/py_tests_mul/ori/ori')
   ```

   The original file contains an empty <u>***.txt***</u> file, followed by the path where the datas are created.

3. Change `mul_x`, `mul_y`, `mul_z` to the  magnification you need.

   ```python
       mul_x = 'x_multiple' # x_direction 
       mul_y = 'y_multiple' # y_direction 
       mul_z = 'z_multiple' # z_direction
   ```

   

4. Use `r_a`, `r_b`, `r_c` ,`r_d`, `r_e` to obtain the proportion of different defect types in the whole system, this proportion is calculated by the magnification of x, y and z in the three directions.

   ```python
       r_a = 'ratio_ia' # The proportion of the ia configuration in the magnification
       r_b = 'ratio_ib' # The proportion of the ib configuration in the magnification
       r_c = 'ratio_ic' # The proportion of the ic configuration in the magnification
       r_d = 'ratio_id' # The proportion of the id configuration in the magnification
       r_e = 'ratio_ie' # The proportion of the ie configuration in the magnification
   ```

5. Remember to change file_storage`(the information of generating information about the data test set, including time, each defect, and the proportion of perfect lattice structures.)`

   ```python
    file_storage = '/path/to/info.txt'
   ```

6. Then the data files are generated from code.

> [!NOTE]
>
> `The raw data collection is stored in the <u>***data_base***</u> folder` xxx.txt can be changed to other basic structures.
>
> ```python
> file_name = 'path/to/data_base/xxx.txt'
> ```

### Create a test file

1. Use ***<u>.dat</u>*** file generated from OVITO to obtain the ID, type`(The type of atom to be studied)`, x-coordinate, y-coordinate, z-coordinate, and coordination number. then convert it to a ***<u>.mat</u>*** file. *<u>Following is an example:</u>*

   ![image-20240612093110771](https://s2.loli.net/2024/06/12/JqnYKzc5eAHpy6r.png)

2. Add the ***<u>.mat</u>*** file into the folder just as the ‘n_0620_t1.mat’ in examples. The database <u>***.mat***</u> files are in the upper folder, ‘ia.mat’, ‘ib.mat’, ‘ic.mat’, ‘ida.mat’, ‘ide.mat’……

### Set up Cython  to enhance the speed of ARDF calculation

add ‘setup.py’ and ‘my_module.pyx’ to the folder, open terminal in aim folder and write following code in it to generate Cython environment.

```python
 python3 setup.py build_ext --inplace
```

Use 

```python
import my_module
```

to introduce computational process after Cython compilation.

### Import detective method: “threshold_defects.py”, “threshold_interstitials.py”

The main two functions are contained in folder <u>***“Algorithm”***</u>

1. “threshold_defects” function contains the procedure of K-MS Hierarchical clustering algorithm to select split vacancy defects in test set.
2. “threshold_interstitials” function contains the procedure of K-MS Hierarchical clustering algorithm to select split interstitial defects in test set.

#### Import ‘Elbow.py’ to utilize K-MS evaluations

According to the evaluation criteria of elbow chart we introduced the method in “threshold_defects.py” and “threshold_interstitials.py”.

### Import periodic boundary condition algorithm “Periodic_boundary_condition.py”

The main function is contained in folder <u>***“Algorithm”***</u>

The periodic boundary condition algorithm is used in the dynamic detection process of high temperature annealing to avoid the problem of atomic environment information contained in ARDF due to particles moving out of the lattice of the test system.

## After setting up the storage data path and introducing the corresponding function package, the test begins: 

After importing all the functions you need, the `if __name__ == "__main__":` is set for running the test program. The <u>***output.txt***</u> file contains the information of test results, ID, positions of complex point defects in test system.

We provided an example of both static and dynamic testing: <u>***statistic_example***</u>, <u>***anneal_example***</u>

## Data preprocessing

The code base provides a way to obtain dynamically stable files in the data set, and if the reader has a better way to obtain a stable atomic point, it can also use the atomic point directly and skip the data preprocessing process.

The main function is contained in folder <u>***“stable_temp”***</u>.

1. We can get stable .dat files from OVITO, then put all of these stable files in one folder.

2. Use Statas_Processing function in <u>***“Use_Excel_file.py”***</u>

3. Change ori_dir to f‘path/to/stable_files’.

4. Run the ‘if \_\_name__ == "\_\_main__":’ function to change <u>***.dat***</u> files into <u>***.txt***</u> files.

   ![image-20240612151029577](https://s2.loli.net/2024/06/12/YaCVhOyRwPFE3Wi.png)

5. After obtaining the .txt files, run <u>***Excel_Generator***</u> function. Changing the files to <u>***Excels***</u>

6. Next step is running ‘if \_\_name__ == "\_\_main__":’ function in <u>***Use_test_23_3_23***</u>

7. Change file_name into  f‘path/to/stable_files’.

8. `file_name` contains all the stable_files’ name. Different test sets are separated by Spaces and stored as.txt documents.

   ![](https://s2.loli.net/2024/06/12/YWMUlswCbOoLk9u.png)

9. `address_all` contains all direction to all stable_files.

10. The average location of every atom is generated through all above  steps. The file is generated in a <u>***.xlsx***</u> file.

    ![image-20240612151544600](https://s2.loli.net/2024/06/12/pPLYJXtiMwmcoTz.png)




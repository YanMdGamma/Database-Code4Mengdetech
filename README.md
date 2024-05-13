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


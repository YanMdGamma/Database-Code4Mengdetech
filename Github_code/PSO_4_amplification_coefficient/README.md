# Details for Amplification coefficient

## How to:

### calculate through PSO algorithm

The standard ARDF data is calculated through interpolation. Stored as **ia.mat**, **ib.mat**, **ic.mat**, **id1.mat**, **id2.mat**, **ie1.mat**, **ie2.mat**, **f_c.mat** and **s_c.mat**.

1. Devide into 2 group split vacancy and split interstitial.
2. Calculate pairwise differences between curves, `summ` contains <u>***10***</u> values for split vacancies and <u>***15***</u> values for split interstitials.
3. Use PSO generate the amplification_coefficient through the max value of the pairwise differences.

> [!TIP]
>
> You can change the database(**ia.mat**, **ib.mat**, **ic.mat**, **id1.mat**, **id2.mat**, **ie1.mat**, **ie2.mat**, **f_c.mat** and **s_c.mat**) for your individual amplification coefficient value.

## output _amplification_coefficient.txt

- Run the file [PSO.py](Github_code/PSO_4_amplification_coefficient/PSO.py) to obtain the amplification coefficient values.
- The output of amplification coefficient for split vacancy and split interstitial is stored in `output _amplification_coefficient.txt` .



**<u>*15.8327*</u>** for split vacancy defects, **<u>*13.8229*</u>** for split interstitials defects

------------------


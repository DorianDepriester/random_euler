# randrot

Python random Euler angles with Bunge convention

Generate random Euler angles (φ_1,ϕ,φ_2), leading to uniformly distributed rotation matrices. The rotation matrices are based on an algorithm described in [Arvo 1992](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.53.1357) whereas the related Euler angles are computed using the procedure described in [Depriester 2018](https://doi.org/10.13140/RG.2.2.34498.48321/2)


## Usage

```python
>>> import numpy as np
>>> import randrot
>>> np.random.seed(0)
>>> randrot.generate_euler()
(3.2295752825154871, 1.7777982464861195, 3.3603143153322188)
```
The output gives the random (φ_1,ϕ,φ_2) angles (in that order). By default, the function returns a single set of Euler angles. The requested number of sets can be passed to the function:
```python
>>> np.random.seed(0)
>>> randrot.generate_euler(3)
[(3.2295752825154871, 1.7777982464861195, 3.3603143153322188), 
(1.3731146396729803, 1.8668922177415044, 5.1920800234521609), 
(3.6402275718841621, 2.7579985692108107, 2.2508066181210702)]
```
In this case, the function returns a list containing each set of Euler angles.

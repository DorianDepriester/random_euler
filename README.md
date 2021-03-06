# RandomEuler

Generate random Euler angles (φ_1,ϕ,φ_2), leading to uniformly distributed rotation matrices in Python.


## Usage

```python
>>> from random_euler import random_euler
>>> random_euler()
(3.2295752825154871, 1.7777982464861195, 3.3603143153322188)
```
The output gives the random (φ_1,ϕ,φ_2) angles (in that order). By default, the function returns a single set of Euler angles. The requested number of sets can be passed to the function:
```python
>>> random_euler(10)
[(0.23331999363194408, 1.6942074455406866, 2.347188210883282),
 (3.037465399177238, 0.735466984664733, 2.5938673300301587),
 (5.721561178411581, 0.9152270703162974, 3.6664390111938103),
 (2.959668132786579, 1.1462625351591558, 3.0307806381134608),
 (0.7087528864855624, 2.6496135318177676, 1.8478991532398603),
 (6.122160717085102, 2.8401785908729464, 1.9252313646075445),
 (5.833281606783825, 2.7490776244484008, 5.237135869615346),
 (6.197927900242208, 2.308423093954234, 0.046351175657699674),
 (5.545143724441338, 1.218396042834138, 0.33644458760789286),
 (2.015539724567453, 0.7587384498303625, 4.522513220962139)]
```
In this case, the function returns a list containing each set of Euler angles.

## Implementation
This function takes advantage of the SciPy's module [stats.special_ortho_group](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.special_ortho_group.html) for generating random rotation matrices. Optional arguments given to the ``random_euler()`` function are passed-by to ``stats.special_ortho_group.rvs()``. Therefore, the initial seed for random generation can be set as follows:

````python
>>>random_euler(n=10,random_state=10)
[(5.474022811728411, 1.7270228795405778, 3.4727837749236867),
 (6.142681520579467, 1.570257135448455, 5.930005984115353),
 (0.8754077081420052, 0.902096420266995, 1.277311394127835),
 (3.3491355335719173, 0.5633346561783479, 1.0213278403114474),
 (3.3574257072788023, 2.653598269971141, 4.0553821794191425),
 (0.7349971410889019, 1.8707504269729494, 3.4618061253273162),
 (2.9010350258217037, 1.0996105414221873, 2.13459998376823),
 (1.718478072590325, 0.6572236020556066, 0.2676761417975663),
 (4.199879333029451, 2.0268650261126475, 0.17565495781011156),
 (4.559117731917635, 2.4700067112772754, 5.528194929190163)]
 ````
 
 Conversion from rotation matrices to Euler angles is made using the ``mat2euler()`` function, as detailed [here](https://www.researchgate.net/publication/324088567_Computing_Euler_angles_with_Bunge_convention_from_rotation_matrix).

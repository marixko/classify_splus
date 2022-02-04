# Tutorial: star/quasar/galaxy classification for S-PLUS fields

In this notebook you will find instructions on how to run the star, quasar, galaxy classification for the S-PLUS survey.

---------------------
## Installation

Install the `splusdata` package (version >= 3.83) for Python 3+:

```
pip install splusdata
```
---------------------
## SQGClass

The `SQGClass` is a pre-trained estimator that works especifically for the [S-PLUS](www.splus.iag.usp.br) survey. More information about the survey can be found in [Mendes de Oliveira et al. 2019](https://ui.adsabs.harvard.edu/abs/2019MNRAS.489..241M/abstract) and [Almeida-Fernandes et al. 2022](https://arxiv.org/abs/2104.00020). For more information about the classification performances, please check [Nakazono et al. 2021](https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.5847N/abstract).


### Parameters for SQGClass:

- model: {"auto", "RF18", "RF16"}, default = "auto"

> Indicates whether to use a model that was pre-trained with the addition of infrared magnitudes (W1 and W2 from ALLWISE) or not. 
> 
> If model = "auto", it automatically run the best model for each case.
> If model = "RF18", it only classify objects that have WISE counterpart.
> If model = "RF16", it classified all objects with a model that do not include infrared magnitudes in the per-trained model.
>
> Please ensure that you are aware of the different expected performances for RF18 and RF16. For that, check Section 6 from [Nakazono et al. 2021](https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.5847N/abstract).

- verbose: True or False
 
> Controls the verbosity when loading the pre-trained model

---------------------
## Method: classify()

SQGClass has a method classify() to predict class and probabilities for a single object or a dataframe.

### Returns

- **CLASS**: float

> The class atributted to an object.
> If CLASS = 0, the object is classified as a quasar.
> If CLASS = 1, the object is classified as a star.
> If CLASS = 2, the object is classified as a galaxy.

- **model_flag**: int

> Flag indicating whether the classification was obtained when training the model with the addition of infrared magnitudes (W1 and W2 from ALLWISE) or not. This is only returned when model = "auto".
> If model_flag = 0, ALLWISE magnitudes are included in the pre-trained model. The flag is 1, otherwise.

- **PROB_QSO**: float 

> Estimated probability of the object being a quasar [0,1]. Only returned when return_prob = True.

- **PROB_STAR**: float 

> Estimated probability of the object being a star [0,1]. Only returned when return_prob = True.

- **PROB_GAL**: float 

> Estimated probability of the object being a galaxy [0,1]. Only returned when return_prob = True.



### Parameters

- df: pandas dataframe

> This pandas dataframe **must** contain the following features:
>
> ```['u_iso', 'J0378_iso','J0395_iso', 'J0410_iso','J0430_iso','g_iso','J0515_iso', 'r_iso','J0660_iso', 'i_iso', 'J0861_iso','z_iso']```
>
> If match_irsa = True, it also must contain `['RA', 'DEC']`

- return_prob: True or False, default = True
 
> Indicates if probabilities should be included in the output. 

- match_irsa: True or False, default = False

> If True, queries ALLWISE observations from [IRSA](https://irsa.ipac.caltech.edu/TAP) TAP service. 
> Attention: if this is set to True, ensure that you enter a limited set of objects each time you call this method, otherwise it becomes computationally expensive to perform the query and the cross-match. We recommend that you classify objects from a single S-PLUS field per time.

- columns_wise: dict, default = {'w1mpro': 'w1mpro','w2mpro': 'w2mpro', 'w1snr': 'w1snr','w2snr': 'w2snr','w1sigmpro': 'w1sigmpro', 'w2sigmpro': 'w2sigmpro'} 

> Sets the names of each ALLWISE column in your df. For instance, if W1 is named "w1_mag" in your dataframe, do as follows: {'w1mpro': 'w1_mag',...} 

- verbose = True or False, default = False 

> Controls verbosity 

---------------------

## Output Example

![image](https://user-images.githubusercontent.com/14929100/152560234-7fb69202-273f-48d0-9929-438a7c7ef048.png)


## Problems?

If you have any problem, please feel free to contact me or open an issue.

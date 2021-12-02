# CAIN: Concordia Artificial Immune Network for B-cell Selection 
_________________
## Purpose
CAIN simulates B-cell selection and an immune response following the introduction of a 
foreign pathogenic antigen. This algorithm is only applicable to antigens with linear
epitope binding sites. B-cell selection occurs via amino acid substitution likelihoods 
according to the Point Accepted Mutation (PAM) matrix. The PAM250 matrix text file is 
provided. If you wish to use a different version, please place the file in the Resources 
directory and alter the code chunk in the `Bcell_Selection.py` file.

Following B-cell selection, an immune response is performed using game-theory concepts to
run a 1x1 matrix game between each individual of the lymphocyte and antigen populations.
The "loser" of each game loses an individual from their respective population and visa versa
for the "winner". 

_________________
## Dependencies
Please install these module versions prior to using CAIN.
- Python 3.0+
- Numpy
- Pandas
- tqdm

________________
## Selection and Response
First: Set your working directory in the `Arg_Parser.py` file at the very top.
Next, run the following command in the terminal, setting each argument per the desired parameters.
```bash
$ python Main.py -e <amino_acid_sequence> -n 100 -d 2 -p 4 -ex 1000 -r 10
```
Required arguments:
* `-e`: Antigen linear epitope.
* `-n`: Number of individuals in each B-cell population
* `-d`: Antigen division rate
* `-p`: Number of B-cell populations
* `-ex`: Number of exchange iterations that occur during B-cell selection
* `-r`: Number of immune response iterations

Running `Main.py` initiates the B-cell selection algorithm and immune response simultaneously.

________________
## Unsupervised Parameter Clustering
1) To collect your data, uncomment the block section `For Large Data Collection` and set the disired
ranges of your hyper-parameters. Run the model which will output an .npz file with kwds="data".
2) Load the data into `Parameter_Clustering.py` and choose the desired clustering method.

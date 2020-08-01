# Data Mining - Final Project

In this project we offer classification using:
k.n.n,kmeans,id3 and naive bayes classifiers
on a giving numpy train data set

## Getting Started

for now the only why to run this application is to run
Gui.py in any IDE using a compatible interpreter

### Prerequisites

acording to the current running mathod you need:
python 3.7 interpeter (conda version is recomended)
and any compitble IDE to run Gui.py

librarys:
scikit-lern on version 0.23.1
numpy

```
pip install -U scikit-learn
or 
conda install scikit-learn

pip install numpy
or
conda install numpy

pip install pandas
or
conda install pandas

```

### Installing

run Gui.py 

```
open Gui.py with PyCharm
and 
```

```
run it using conda interpeter 3.7
```


## Running the tests

in preprocessor:
1.load train,test and structure files or use 20/80 option
2.choose number of bins
3.choose bins type
4.choose how to handle missing elements
in classifier:
1.choose classifier
2.for id3 set t tolerance for max recursion
in Run:
run:)

### Break down into end to end tests

in Run you can view the precision of prediction
acording your train,test files (or 20/80)
and view the confusion matrix

mathod ussing single_test.py

```
kwargs = {   'test':pd.read_csv('test.csv'),
             'train':pd.read_csv('train.csv'),
             'structure':load_structure(),
             'number_of_bins':3,
             'k':5,
             'tolorance':5,
             'bin_type':'equal_frequency',
             'missing_values': 'replace_nans',
             '8020': 'no',
    }

print(
get_result('our_naive_bayes',**kwargs)
)

{'score': 60.34312108215111, 'TP': 708, 'TN': 1121, 'FP': 346, 'FN': 856}
```

## File Dependency

ide3.py,our_id3.py,naive_bayes.py,our_naive_bayes.py operate: Preprocessing.py
knn.py,kmeans.py operate: Preprocessing_for_knn_and_k_means.py
start.py operate:id3.py,kmeans.py,knn.py,naive_bayes.py,our_id3.py.our_naive_bayes.py
Gui.py,single_test.py,run_log_all.py operate: start.py




## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE used for this project
* [vim](https://www.vim.org/) - Dependency IDE used for this project


## Authors

* **Tal Alfi**
* **Oleg Belochitsky**
* **Ziv Friza**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
Copyright <2020> <COPYRIGHT HOLDER>

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

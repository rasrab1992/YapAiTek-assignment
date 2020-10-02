
## Table of Contents:
* Installation
* Usage



### Installation:
###### For displaying persian text install:
```
pip install arabic-reshaper
pip install python-bidi
```
###### For tokenizing persian texts install:
```
pip install hazm
```
###### For reading persian stopwords docx file install:
```
pip install python-docx
```

### Usage:
###### 1. Import two libraries that created for this task:
```
from data_utils import *
from plot_utils import *
```

###### 2. prepare the list of all comments and the list of all sockets name:
```
comments, results = prepare_data('betasahm1.csv', 'result.csv')
```
###### 3. tokenize the comments  
```
sents = tokenize_all(comments)
```
###### 4. make a sorted dictionary of tokenized comments that include these result names without stopwords:
```
sahms = cleaned_sorted_count_frequency(sents, results, 'stopwords-Farsi1.docx')
```
###### 5. Create an object of PlotFig for the first num_plot numbers:
```
num_plot = 6
pltfig = PlotFig(all_sorted = sahms, num_plot= num_plot)
```
###### 6. Use one of this methods for plotting:
```
- pltfig.plot_barh()
- pltfig.plot_pie()
- pltfig.plot_pie_barh()
- pltfig.plot_pie_barh()
```

<p align="center">
<a href="https://dscommunity.in">
	<img src="https://github.com/Data-Science-Community-SRM/template/blob/master/Header.png?raw=true" width=80%/>
</a>
	<h2 align="center"> Buildlytics </h2>
	<h4 align="center"> A comprehensive way to make your Exploratory data analysis process easy by using our package <h4>
</p>

---
[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](INSERT_LINK_FOR_DOCS_HERE) 
  [![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](INSERT_UI_LINK_HERE)

## Preview
- Preview of our package
<img src="https://github.com/Data-Science-Community-SRM/buildlytics/blob/master/Images/Screenshot%20from%202021-02-25%2022-52-32.png" width=40%/>
<br><br>
<img src="https://github.com/Data-Science-Community-SRM/buildlytics/blob/master/Images/Screenshot%20from%202021-02-25%2022-52-08.png" width=40%/>
<br><br>
<img src="https://github.com/Data-Science-Community-SRM/buildlytics/blob/master/Images/Screenshot%20from%202021-02-25%2022-52-13.png" width=40%/>

## Functionalities
The module contains `DataFrameSummary` function which takes dataframe in its parameter

 * **properties**
    * dfs.columns_stats: counts, uniques, missing, missing_perc, and type per column etc.
    * dsf.columns_types: a count of the types of columns
    * dfs[column]: more in depth summary of the column
<br>


## Instructions to run

* Pre-requisites:
	-  Install Pandas, Seaborn, Matplotlib
	-  Install Python

*
The module can be easily installed with pip:
```bash
!pip3 install buildlytics --upgrade
```
The `DataFrameSummary` expect a pandas `DataFrame` to summarise.

```
from pandas_summary import DataFrameSummary

dfs = DataFrameSummary(tips)
```

To get the columns types

```
dfs.columns_types


bool           3
numeric        3
categorical    1
Name: types, dtype: int64
```

To get the overall columns stats

```
dfs.columns_stats

	total_bill	tip	sex	smoker	day	time	size
counts	244	244	244	244	244	244	244
uniques	229	123	2	2	4	2	6
missing	0	0	0	0	0	0	0
missing_perc	0%	0%	0%	0%	0%	0%	0%
types	numeric	numeric	bool	bool	categorical	bool	numeric
```

To get the particular column stats

```
dfs['total_bill']

mean                            19.7859
std                             8.90241
variance                        79.2529
min                                3.07
max                               50.81
mode                              13.42
5%                               9.5575
25%                             13.3475
50%                              17.795
75%                             24.1275
95%                              38.061
iqr                               10.78
kurtosis                        1.21848
skewness                        1.13321
sum                             4827.77
mad                             6.86944
cv                             0.449936
zeros_num                             0
zeros_perc                           0%
deviating_of_mean                     4
deviating_of_mean_perc            1.64%
deviating_of_median                  12
deviating_of_median_perc          4.92%
top_correlations            tip: 67.57%
counts                              244
uniques                             229
missing                               0
missing_perc                         0%
types                           numeric
Name: total_bill, dtype: object

```

To get the heatmap

```
dfs._get_heatmap(tips) //tips is the dataframe
```

To get the pairplot

```
pairplot=DataFrameSummary(tips)
pairplot._get_pairplot()
```

To get the scatterplot

```
dfs._get_scatterplot(tips['total_bill'],tips['tip'],tips['day'])
```




## Contribute to this package

**For Maintainers:**

Guide for adding new features:

* You need to download the zip file for this project

* Download the package : buildlytics using pip3 

* Whatever changes you make to the code will only be reflected if package is updated with your changes, so, incase you are not the maintainer on PyPi , drop a message in the discord group.

* Update the version before uploading in setup.py

For uploading version changes type the following in terminal of the downloaded folder :

```bash
python3 setup.py sdist
    twine upload dist/*
```
**For Open Source Contributors**

* Open a Pull request 
* State the new feature you are proposing to add or issue you are solving clearly
* Wait for us to approve it. :wink:

**Notebooks**

You can find the notebook <a href="https://github.com/Data-Science-Community-SRM/buildlytics/blob/master/Experiment-NBS/Experiment-Package.ipynb">here</a>



<h1 align="center"> Project Maintainers </h1>


<table align="center">
<tr align="center">


<td>

Akshat Anand

<p align="center">
<img src = "https://github.com/hritikbhandari/ReCo.Ai/blob/master/images/Akshat.jpg"  height="120" alt="Your Name Here (Insert Your Image Link In Src">
</p>
<p align="center">
<a href = "https://github.com/cipheraxat"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/akshatanand1999">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>


<td>

Tarushi Pathak

<p align="center">
<img src = "https://tarushi98.github.io/3.jpg"  height="120" alt="Your Name Here (Insert Your Image Link In Src">
</p>
<p align="center">
<a href = "https://github.com/tarushi98"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/tarushi-pathak-6b7b5b177/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
</tr>
</table>

<h2 align="center"> Contributors </h2>



<table  align="center">
<tr align="center">


<td>

Stuti Sehgal

<p align="center">
<img src = "https://github.com/Data-Science-Community-SRM/buildlytics/blob/master/Images/me.jpg"  height="120">
</p>
<p align="center">
<a href = "https://github.com/stutisehgal"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/stutisehgal">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>


<td>

Soumya Snigdha Kundu

<p align="center">
<img src = "https://media-exp1.licdn.com/dms/image/C5603AQGoZeQyhZ_bHQ/profile-displayphoto-shrink_400_400/0/1613590285777?e=1620259200&v=beta&t=3ced-DD7g3vEcFG_1_DXTj8vMpM4M9V4HGbJWkvYO4o"  height="120">
</p>
<p align="center">
<a href = "https://github.com/aymuos15"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/soumya-snigdha-kundu-84b812183/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
</tr>
</table>



  
## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

<p align="center">
	Made with :heart: by <a href="https://dscommunity.in">DS Community SRM</a>
</p>


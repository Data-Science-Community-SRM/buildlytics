<h2> Buildlytics Package Experiment </h2>

**Guide to be removed before making this repo public**

Guide for adding new features:

1) You need to download the zip file for this project

2) Download the package : buildlytics-test-3 using pip3 ( We are still testing this package prior to release)

3) Whatever changes you make to the code will only be reflected if package is updated with your changes, so, incase you are not the maintainer on PyPi , drop a message in the discord group. 

4) Update the version before uploading in setup.py

 For uploading version changes type the following in terminal of the downloaded folder : 


``` python
    python3 setup.py sdist
    twine upload dist/*
```


[Here's](https://pypi.org/project/buildlytics-test-3/) the package link

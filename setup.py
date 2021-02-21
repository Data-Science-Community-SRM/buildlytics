from setuptools import find_packages, setup

setup(
    name= "buildlytics-test-3",
    packages=['EDALIB'],
    version="0.2.2",
    platforms='any',
    description="EDA Package Test --pairplot",
    install_requires=[
          'numpy',
          'pandas',
          'seaborn'
      ],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering'
    ],
    license="MIT"
)

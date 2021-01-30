# Python

<p align="center">
  <img src="metadata/python.png">
</p> 


### Miniconda Environment Guidelines 
- [Medium Post](https://codenamewei.medium.com/ctrl-c-ctrl-v-replicating-data-science-conda-environment-c190ad0d93fd)
- [miniconda-guidelines.md](https://github.com/codenamewei/pydata-science-env/blob/main/miniconda-guidelines.md)

### Application with Internal Package
```
helloworld/
│
│
├── docs/
│   ├── hello.md
│   └── world.md
│
├── helloworld/ (some do src/helloworld, some do src/)
│   ├── __init__.py
│   ├── runner.py
│   ├── hello/
│   │   ├── __init__.py
│   │   ├── hello.py
│   │   └── helpers.py
│   │
│   └── world/
│       ├── __init__.py
│       ├── helpers.py
│       └── world.py
│
├── data/
│   ├── input.csv
│   └── output.xlsx
│
├── examples/
|
├── tests/
│   ├── hello
│   │   ├── helpers_tests.py
│   │   └── hello_tests.py
│   │
│   └── world/
│       ├── helpers_tests.py
│       └── world_tests.py
|
├── setup.py
├── .gitignore
├── LICENSE
└── README.md
```

### setup.py and setuptools
Package and distribution management.

### requirements.txt
pip requirements file
Example
```
pip install -r requirements.txt
```

### config.yml
```
conda env create -f config.yml
```



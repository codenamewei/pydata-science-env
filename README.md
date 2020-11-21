# Python file directory
### One-off Script
```
helloworld/
│
├── .gitignore
├── helloworld.py (advise to go with name of project)
├── LICENSE
├── README.md
├── requirements.txt / config.yml
├── setup.py (pipenv)
└── tests.py
```

### Single Package
```
helloworld/
│
├── helloworld/
│   ├── __init__.py
│   ├── helloworld.py
│   └── helpers.py
│
├── tests/
│   ├── helloworld_tests.py
│   └── helpers_tests.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

### Application with Internal Package
```
helloworld/
│
├── bin/
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
│
├── .gitignore
├── LICENSE
└── README.md
```

Django and Flask structure refer to [here](https://realpython.com/python-application-layouts/)

The __init__.py is to treat python file like module (only need for before python 3.3)
https://stackoverflow.com/questions/448271/what-is-init-py-for

# Conda 
```
conda env create -f config.yml
conda remove --name format-converter-env --all
```
_config.yml_
```
name: format-converter-env
channels:
  - anaconda
dependencies:
  - python=3.7
  - pip=20.2.*
  - jupyterlab
  - pip:
    - click==7.1.*

```

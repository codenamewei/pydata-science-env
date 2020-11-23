# [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)


**Conda create environment from yml file**
```
conda env create -f config.yml
```

**Conda list all environments available**
```
conda env list
```

**Conda remove environment**
```
conda remove --name format-converter-env --all
```

** _config.yml_ Skeleton Structure**
```
name: python-dev-env
channels:
  - anaconda
dependencies:
  - python=3.7
  - pip=20.2.*
  - jupyterlab
  - pip:
    - click==7.1.*
```


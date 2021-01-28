# [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)


**Conda create an environment from yml file**
```
conda env create -f config.yml
```

**Conda create yml file from an existing environment**
```
conda env export --file config.yml
```

**Conda activate an environment**
```
conda activate python-dev-env
```

**Conda deactivate an environment**
```
conda deactivate
```

**Conda list all environments available**
```
conda env list
```

**Conda list all packages in an environment**
```
conda list -n python-dev-env
```

**Conda remove environment**
```
conda remove --name python-dev-env --all
```

**_config.yml_ Skeleton Structure**
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


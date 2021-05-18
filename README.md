# A sample data analysis repo 
Example repo to show a possible structure for a python data analysis project
with some library code and calls to it from an analysis notebook.

---

### `analysis_package` 
Folder containing the library code in python modules. Should be renamed to concisely represent the library.
(See https://docs.python.org/3/tutorial/modules.html#packages for more information)

#### `analysis_package/module.py`
Python module for the code. Should be renamed to concisely represent what the module is doing.
(See https://docs.python.org/3/tutorial/modules.html#packages for more information)

### `data` 
Folder containing the data.

### `test`
Folder containing unittests for the package

#### `test/test_module.py`
Test for module "module.py"

### `.gitignore`
File to list stuff that should be ignored by git

### `analysis.ipynb`
Notebook importing functions from the package, 
creates results from data and contains the interpretation of results.

### `environment.yml`
Conda environment yml file to recreate the environment for the analysis.
Can be created by something like this on bash:
```bash
conda env export --from-history | grep -v prefix > environment.yml
```

### `README.md`
File that is rendered by GitHub/GitLab when looking at the repo.

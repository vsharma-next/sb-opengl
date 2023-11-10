## Initialization

### Python

1.  Create a mamba env with python=3.10.\* and ipython
2.  Within the main work folder create a virtual env

````
					python -m venv .venv
					source .venv/bin/activate
					python -m pip install --upgrade pip
				```
3. Install packages
````

    		python -m pip install pygame numpy PyOpenGL PyOpenGL_accelerate
    		```

### Git

1.  git init
2.  echo ".venv" > .gitignore
3.  git add .
4.  git commit -m "project init"

# LAB - Class 01

## Project: Snakes Cafe

### Author: Ben Hill

### Links and Resources

- [Pull Request URL](https://github.com/ben-hill33/snakes_cafe/pull/1) 
- [python-poetry](https://python-poetry.org/)

### Setup
This program uses [python-poetry](https://python-poetry.org/) for dependency package manager. In order to create this project, follow the python-poetry link in the **Links and Resources** section above and install poetry.

Then enter the following commands into your CLI from the directory you want your project to live:
```
$ poetry new example-lab
$ cd example-lab
$ poetry add --dev black --allow-prereleases
$ touch example_lab/example_lab.py
$ mv README.rst README.md
$ git init
$ git add .
$ git commit -m "first commit"
```

### How to initialize/run your application 

- Now that your program is scaffolded you can run poetry virtual environment.
- To initialize, run this command in CLI:
  - ```$ poetry shell```
- To check output:
  - ```$ python snakes_cafe.py```

#### Tests

Tests coming soon!!


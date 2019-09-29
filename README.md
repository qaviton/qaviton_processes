# Qaviton Processes
![logo](https://www.qaviton.com/wp-content/uploads/logo-svg.svg)  
[![version](https://img.shields.io/pypi/v/qaviton_processes.svg)](https://pypi.python.org/pypi)
[![license](https://img.shields.io/pypi/l/qaviton_processes.svg)](https://pypi.python.org/pypi)
[![open issues](https://img.shields.io/github/issues/qaviton/qaviton_processes)](https://github/issues-raw/qaviton/qaviton_processes)
[![downloads](https://img.shields.io/pypi/dm/qaviton_processes.svg)](https://pypi.python.org/pypi)
![code size](https://img.shields.io/github/languages/code-size/qaviton/qaviton_processes)
-------------------------  

simple python wrappers for different processes  

## Installation  
```sh  
pip install --upgrade qaviton_processes
```  

### Requirements
- Python 3.6+  
  
## Features  
* programmatic support for automating different processes ✓  
* system cli wrapper ✓  
* async support ✓  
* pip wrappers ✓  
* git wrappers ✓  
* python wrappers ✓  
* pytest wrappers ✓  
  
## Usages  
  
```python
from qaviton_processes.system import (
    run,
    pip,
    git,
    escape,
    python,
    python_code,
    pytest,
    run_async,
    pytest_async,
    python_async,
    python_code_async,
)

stdout: bytes = run(f"echo \"{escape(input('say hi:'))}\"")

process = run_async("cd proj && touch jig.txt")
while process.poll() is None:
        ...
print(process.stdout, process.stderr)

git('clone {url}.git')
pip('install', 'qaviton_processes', '-U')
python('script.py')
python_code('import os', 'if os.path.exist("proj"+os.sep+"jig.txt"):', '  print("awsome!")')
python_async('-m scripts.monitor', 'log=log.txt')
...
```  
  
  
  
  
  
  
    
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

projectname = 'cnnClassifier'

file_names = [
    '.github/workflows/.gitkeep',
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/entity/__init__.py",
    f"src/{projectname}/utils/__init__.py",
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/config/__init__.py",
    f"src/{projectname}/config/configuration.py",
    f"src/{projectname}/utils/common.py",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/constants/__init__.py",
    'requirements.txt',
    'config/config.yaml',
    'params.yaml',
    'dvc.yaml',
    'setup.py',
    'research/trails.ipynb',
    'templates/index.html',
    'Dockerfile',
    'main.py',
    'app.py'
]

for file in file_names:
    file_path = Path(file)
    filedir,filename = os.path.split(file)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created the directory {filedir} for the file : {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,'w') as f:
            pass
        logging.info(f"Created the file {file_path}")
    else:
        logging.info(f"{filename} already exists")
import os
from pathlib import Path
import logging

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",  ##For CI/CD capabilities
    f"src/{project_name}/_init_.py", ## __init__.py signifies a Python package and we can call it locally
    f"src/{project_name}/components/_init_.py",
    f"src/{project_name}/utils/_init_.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/_init_.py",
    f"src/{project_name}/config/_init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init_.py",
    f"src/{project_name}/entity/_init_.py",
    f"src/{project_name}/constants/_init_.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.pynb",
    "test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)  ##Detects OS and gives path in right format (slashes etc)
    filedir, filename = os.path.split(filepath) #returns 2 values

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #if the dir is not there,it creates the directory
        logging.info(f"Creating directory : {filedir} for the file {filename}") ##To see terminal log


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
          ##if the folders are empty or the file inside have 0 size(as if something is there inside it shoulnt replace it rather creaeate new), we go inside an dcreate files
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating the file {filename}")
    else:
        logging.info(f"file {filename} aready exists")

    
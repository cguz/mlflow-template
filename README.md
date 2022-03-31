# Mlflow Pipeline Template

This repository contains a Mlflow pipeline. 

The source code is in the folder [src](src/).

- conda.yaml : define the configuration file of the conda. It contains the name, channels, and dependencies of the pipeline.
- MLproject : define the name of the pipeline, along with the configuration of the conda environment, and the entry points of the pipeline. Each entry point is related with a python file. 
    - main.py : the main file is the entry point and also define the mlflow tracking. 
    - create_dataset.py 
    - build_model.py
    - train_model.py
    - evaluate.py 
    - deploy.py
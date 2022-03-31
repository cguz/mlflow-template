# build_model.py
import mlflow
import click

@click.command(help="This program build the model")
@click.option("--data-path")
def build_model(data_path):
    with mlflow.start_run() as mlrun:
        # logic of the step goes here

        output = "log"
        print("Uploading output: %s" % output)
    
        mlflow.log_artifacts(output, "model.txt")


        # 1. setup experiment
        # 2. train model

if __name__ == '__main__':
    build_model()

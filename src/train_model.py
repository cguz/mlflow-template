# train_model.py
import mlflow
import click

@click.command(help="This program train the model")
@click.option("--model-path")
def train_model(model_path):
    with mlflow.start_run() as mlrun:
        # logic of the step goes here

        output = "log"
        print("Uploading output: %s" % output)
    
        mlflow.log_artifacts(output, "model_trained.txt")


        # 1. setup experiment
        # 2. train model
        # 3. Logging

if __name__ == '__main__':
    train_model()

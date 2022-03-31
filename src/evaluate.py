# evaluate.py
import mlflow
import click

@click.command(help="This program evaluate the model")
@click.option("--model-trained-path")
def evaluate(model_trained_path):
    with mlflow.start_run() as mlrun:
        # logic of the step goes here

        output = "log"
        print("Uploading output: %s" % output)
    
        mlflow.log_artifacts(output, "result.txt")


        # 1. setup experiment
        # 2. train model
        # 3. Logging

if __name__ == '__main__':
    evaluate()

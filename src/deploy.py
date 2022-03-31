# deploy.py
import mlflow
import click

@click.command(help="This program deploy the model")
@click.option("--result-path")
def deploy(result_path):
    with mlflow.start_run() as mlrun:
        # logic of the step goes here

        output = "log"
        print("Uploading output: %s" % output)
    
        #mlflow.log_artifacts(output, "artifact_deploy.txt")


        # 1. setup experiment
        # 2. train model
        # 3. Logging

if __name__ == '__main__':
    deploy()

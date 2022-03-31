# create_dataset.py
import mlflow
import click

@click.command(help="This program read and create the dataset")
def create_dataset():
    with mlflow.start_run() as mlrun:

        # logic of the step are in the jupyter notebooks/create_dataset.pynb  

        # Log mlflow attributes for mlflow UI
        # mlflow.log_param("alpha", alpha)
        # mlflow.log_param("l1_ratio", l1_ratio)
        
        # mlflow.log_metric("rmse", rmse)
        # mlflow.log_metric("r2", r2)
        # mlflow.log_metric("mae", mae)
        
        # mlflow.sklearn.log_model(lr, "model")
        # modelpath = "/dbfs/mlflow/test_diabetes/model-%f-%f" % (alpha, l1_ratio)
        # mlflow.sklearn.save_model(lr, modelpath)

        # Log artifacts (output files)
        # mlflow.log_artifact("ElasticNet-paths.png")


        output = "log"
        print("Uploading output: %s" % output)
    
        mlflow.log_artifacts(output, "dataset.txt")


if __name__ == '__main__':
    create_dataset()

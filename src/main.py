# main.py
import os
import click
import mlflow

@click.command()
@click.option("--input", default=10, type=int)
def workflow(input):
    with mlflow.start_run() as active_run:
        print("Launching 'create_dataset'")
        create_dataset_run = mlflow.run(".", "create_dataset", parameters={})
        create_dataset_run = mlflow.tracking.MlflowClient().get_run(create_dataset_run.run_id)
        data_path_uri = os.path.join(create_dataset_run.info.artifact_uri, "dataset.txt")

        print("Launching 'build_model'")
        build_model_run = mlflow.run(".", "build_model", parameters={"data_path": data_path_uri})
        build_model_run = mlflow.tracking.MlflowClient().get_run(build_model_run.run_id)
        model_path_uri = os.path.join(build_model_run.info.artifact_uri, "model.txt")

        print("Launching 'train_model'")
        train_model_run = mlflow.run(".", "train_model", parameters={"model_path": model_path_uri})
        train_model_run = mlflow.tracking.MlflowClient().get_run(train_model_run.run_id)
        model_trained_path_uri = os.path.join(train_model_run.info.artifact_uri, "model_trained.txt")
        
        print("Launching 'evaluate'")
        evaluate_run = mlflow.run(".", "evaluate", parameters={"model_trained_path": model_trained_path_uri})
        evaluate_run = mlflow.tracking.MlflowClient().get_run(evaluate_run.run_id)
        result_path_uri = os.path.join(evaluate_run.info.artifact_uri, "result.txt")
        
        print("Launching 'deploy'")
        deploy_run = mlflow.run(".", "deploy", parameters={"result_path": result_path_uri})
        deploy_run = mlflow.tracking.MlflowClient().get_run(deploy_run.run_id)

if __name__ == '__main__':
    workflow()

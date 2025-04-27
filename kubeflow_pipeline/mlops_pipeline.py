import kfp
from kfp import dsl 

def data_processing_op():
    return dsl.ContainerOp(
        name="Data Processing",
        image = "bhavith22/colorectal-app:latest",
        command = ["python3","src/data_processing.py"],
        )

def model_training_op():
    return dsl.ContainerOp(
        name="Model Training",
        image = "bhavith22/colorectal-app:latest",
        command = ["python3","src/model_training.py"],
        )
    
## Pipeline starts

@dsl.pipeline(
    name = "MLOps Pipeline",
    description = "kebeflow pipeline for MLOps"
    
)

def mlops_pipeline():
    data_processing = data_processing_op()
    model_training = model_training_op().after(data_processing)
    
## RUN

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(mlops_pipeline,"mlops_pipeline.yaml")
    
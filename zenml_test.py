from zenml.pipelines import pipeline
from zenml.steps import step

@step
def hello_world_step() -> None:
    print("Hello, ZenML!")

@pipeline
def hello_world_pipeline(step):
    step()

if __name__ == "__main__":
    hello_pipeline = hello_world_pipeline(hello_world_step())
    hello_pipeline.run()
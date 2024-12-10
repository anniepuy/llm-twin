## LLM-TWIN Project

### Overview

The project is a locally hosted version of the LLM-Twin designed from "LLM Engineer's Handbook" by Paul Lusztin & Maxime Labonne, published by Packt.

Instead of using cloud hosted ZenML and AWS tools such as SageMaker, I modified the code to use local and open source tools.

### ML OPS

ML Ops uses ZenML. Instead of using the cloud hosted ZenML I configured this project to use the local and open source version.
The steps I had to take:

1. Install pipx
2. pip install zenml
3. zenml init - this initializes the repositories and workspaces
4. pip install "zenml[server]==0.71.0" - installs dependencies to use the local dashboard
5. zenml login --local
6. Logged in with my username.

### Tools

1. Poetry
2. Python 3.11
3. ZenML

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

### Learning Take-Aways

1. Make code module. Instead of one lengthly 3000 line script, break the functions up into modularity for plug and play as technology and tools change. If someone asks "Well how many lines of code is this? its not thousands.." in a condescending tone, just know they don't know how to make resuable and module code. They are ego driven and not worth your time.

2. First time using Poetry and ZenML.

## modified project overview:

Project Overview 1. Visualize Generator Locations on a Map:
• Plot the locations of the generators using tools like OpenStreetMap or Plotly for interactive visualizations.
• Use folium or geopandas for location-based overlays.
• Add real-time or predictive outputs for each generator. 2. Predict Power Output Using Machine Learning Models:
• Use the meteorological features (temperature_2m, windspeed_10m, etc.) to train a regression model to predict Power (turbine output).
• Employ models like:
• Random Forests for a baseline.
• LSTMs or other time-series models for capturing temporal dependencies. 3. Integrate with an LLM Pipeline for Retraining:
• Fine-tune your base LLM (e.g., Mistral) with this domain-specific data to generate insights or answer questions related to wind power generation.
• Use your data to create structured prompt-response pairs for training. 4. Dashboard for Visualization and Insights:
• Use tools like Streamlit or Dash to build an interactive dashboard.
• Include:
• Map visualization of generators.
• Predicted vs. actual power outputs.
• Insights from the fine-tuned LLM.

Implementation Steps

1. Data Preprocessing
   • Handle missing or irrelevant columns.
   • Normalize the Power column for better interpretability.
   • Transform winddirection_10m and winddirection_100m into sine and cosine components to handle circular data.
   • Split data into training and test sets.

2. Map Visualization
   • Add geographic coordinates to the dataset (you may need to synthesize or map coordinates to locations).
   • Plot the data using:
   • folium for static maps.
   • Plotly for interactive maps.

3. Prediction Modeling
   • Train a regression model for predicting Power based on meteorological data.
   • Suggested approach:
   • Train a baseline Random Forest model.
   • Use time-series modeling (e.g., LSTM) for temporal predictions.
   • Evaluate the model using metrics like RMSE or MAE.

4. Fine-Tuning the LLM
   • Prepare text data for fine-tuning:
   • Generate Q&A pairs related to wind power data.
   • Include “explanations” generated from the dataset for model training.
   • Fine-tune Mistral with this data using a local framework like Hugging Face Transformers.

5. Build the Dashboard
   • Use Streamlit, Dash, or Flask for:
   • Integrating map visualizations.
   • Displaying model predictions.
   • Allowing users to query the fine-tuned LLM for domain-specific insights.

ZenML Pipeline

Integrate all these components into a ZenML pipeline: 1. Data Ingestion Step: Load and preprocess the Kaggle dataset. 2. Training Step: Train the power prediction model. 3. Evaluation Step: Evaluate the model and visualize results. 4. Visualization Step: Generate maps and dashboards. 5. LLM Fine-Tuning Step: Use ZenML to automate the retraining of the LLM model with new data.

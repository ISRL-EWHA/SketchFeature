# ML.ipynb: Traffic Classification Using CNN

This repository contains a Jupyter Notebook (`ML.ipynb`) that demonstrates how to train and test a Convolutional Neural Network (CNN) model for traffic classification. Follow the instructions below to set up the environment, access the datasets, and run the notebook.

## Datasets

To work with this project, you need to download the required datasets. The following datasets are used:

1. **DDoS Dataset**: Available for download at [UNB CIC DDoS Dataset 2019](https://www.unb.ca/cic/datasets/ddos-2019.html).
2. **BotNet Dataset**: Available for download at [UNB CIC BotNet Dataset](https://www.unb.ca/cic/datasets/botnet.html).
3. **Covert Storage Channel Dataset**: Available for download at [MPT Detection Resources](https://turbina.gsd.inesc-id.pt/resources/mpt_detection/).
4. **Benign Traffic Dataset**: Available for download at [CAIDA Passive Dataset](https://www.caida.org/catalog/datasets/passive_dataset/).

## Workflow

### 1. Dataset Preparation
- Extract the **PSD (Power Spectral Density)** and **IAT (Inter-Arrival Time)** features from the raw data.
- Save the extracted features in CSV format:
  - Each row corresponds to the feature information of a single flow.
  - The last column in each row contains the label for the flow (e.g., attack type or benign traffic).

### 2. Training the CNN Model
- Open the `ML.ipynb` file in Jupyter Notebook or your preferred IDE.
- Follow the code sections to train the CNN model using the extracted feature data.

### 3. Testing the Model
- Mix the data from different datasets and prepare a test set.
- Use the `sketfeature` encoding method to encode the mixed data.
- Decode the data after processing and feed it to the trained CNN model for inference.

## Requirements

Ensure you have the following installed:
- Python (3.8+ recommended)
- Jupyter Notebook
- Required Python libraries (install using `pip install -r requirements.txt` if a `requirements.txt` is provided)


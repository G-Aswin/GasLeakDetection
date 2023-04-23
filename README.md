# How to run 🤔

## Installing required packages

```bash
# install python 3 and pip3 first
pip3 install -r requirements.txt
```

## Preprocessing the raw data (only need to be done once)

```bash
# Assuming that Raw data is present in the directory : Data/SampleRawData
python3 Py3/ProcessRawData.py
# Output will be generated in Data/ProcessedRawData
```

## Running the flask server

```bash
python3 -m flask run
```

## Google Collab file for the ML algorithm testing
[Gas_Leak_Detection_ML_Sample_Runs.ipynb](Gas_Leak_Detection_ML_Sample_Runs.ipynb)
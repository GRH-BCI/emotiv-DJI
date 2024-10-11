# Emotiv DJI Controller

## Requirement
- This app works with Python >= 3.8
- Install websocket client via  `pip install websocket-client`


## About the app

This app is based on Emotiv Cortex V2 library. live_advance.py is an altered version of the existing version in python examples folder of Emotiv CortexV2. 
This app is used to map Emotiv Cortex commands generated through EMotivBCI app, to keyboard keypresses. the keyboard keypresses are further used to control a DJI robot through it's computer software. 

## Cortex Library
- [`cortex.py`](./cortex.py) - the wrapper lib around EMOTIV Cortex API.

## Susbcribe Data
- [`sub_data.py`](./sub_data.py) shows data streaming from Cortex: EEG, motion, band power and Performance Metrics.
- For more details https://emotiv.gitbook.io/cortex-api/data-subscription

## BCI
- [`mental_command_train.py`](./mental_command_train.py) shows Mental Command training.
- [`facial_expression_train.py`](./facial_expression_train.py) shows facial expression training.
- For more details https://emotiv.gitbook.io/cortex-api/bci

## Advanced BCI
- [`live_advance.py`](./live_advance.py) shows the ability to get and set sensitivity of mental command action in live mode.
- For more details https://emotiv.gitbook.io/cortex-api/advanced-bci

## Create record and export to file
- [`record.py`](./record.py) shows how to create record and export data to CSV or EDF format.
- For more details https://emotiv.gitbook.io/cortex-api/records

## Inject marker while recording
- [`marker.py`](./marker.py) shows how to inject marker during a recording.
- For more details https://emotiv.gitbook.io/cortex-api/markers



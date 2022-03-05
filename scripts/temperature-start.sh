#!/bin/bash

SERVICE_PATH="/TemperatureService"
SOURCE="TemperatureValidatorAPI.py"
SOURCE_PATH="$SERVICE_PATH/$SOURCE"
cd $SERVICE_PATH
sudo python3 $SOURCE_PATH >>Temperature_Validator_API.log 2>&1 &

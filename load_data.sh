#!/bin/bash

# download data
function download_data () {
    
    # download data
    wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1wulIkuLm69d2dTZjyksmH6evFx9GYDkX' -O data/raw/train.csv
    echo "################# downloaded successfully ###################"
}


# run preprocess
function run_preprocess () {
    "/home/wonseok/.pyenv/versions/2022_pnn_fl/bin/python" code/preprocess_data.py
    echo "################# preprocessed data! #################"
}








"$@"
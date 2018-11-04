#!/bin/sh

MODEL_URL="https://github.com/foamliu/Simple-Colorization/releases/download/v1.0/model.06-2.5489.hdf5"
MODEL_NAME=${MODEL_URL##*/}
DEP="numpy tensorflow keras opencv"

if [ ! -d models ]; then
  mkdir models
fi

if [ ! -f models/${MODEL_NAME} ]; then
  if [ ! -d ../.cache ]; then
    mkdir ../.cache
  fi
  if [ ! -f ../.cache/${MODEL_NAME} ]; then
    echo "Downloading the pre-built model itself (95M) which can take a minute or two..."
    wget --directory-prefix=../.cache $MODEL_URL
    echo ""
  fi
  cp ../.cache/${MODEL_NAME} models/
fi


echo "Installing dependencies:" $DEP
conda install $DEP

# mlp-covid-database

# Download Database

If you want to download the latest version to the database, click here:
https://www.kaggle.com/tawsifurrahman/covid19-radiography-database

# Data augmentation

Flip all COVID images horizontally.

Before augmentation: 3616 COVID images

After augmentation: 7232 COVID images

*Note*: augmentation.py is not being used in main.py. Run separately to increase the data.

# How to install dependencies to Project

*Note*: This guide was made using Python 3.8 and Windows 10

## Install OpenCv

```
pip install opencv-python
```

## Install skimage

```
python -m pip install -U scikit-im age
```

## Install sklearn

```
pip install -U scikit-learn
```

## Install numpy

```
pip install numpy
```

## Install MatPlotLib

```
pip install matplotlib
```

## Install Keras

```
pip install "tensorflow>=2.0.0"
```
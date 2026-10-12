# TensorFlow Basics

Deep learning experiments using TensorFlow and Keras, based on [Kaggle's Intro to Deep Learning](https://www.kaggle.com/learn/intro-to-deep-learning) course, plus notes from Kaggle's [Feature Engineering](https://www.kaggle.com/learn/feature-engineering) course.

## Key Concepts

### Lesson 1 - Single Neuron
Linear units (neurons) with weights and bias form the building blocks of neural networks.

### Lesson 2 - Deep Neural Networks
Multiple dense layers with activation functions (ReLU, sigmoid, ELU) create deep architectures capable of learning complex patterns.

### Lesson 3 - Stochastic Gradient Descent
Loss functions define the optimization objective, while optimizers (Adam, SGD) adjust weights through mini-batch training across epochs.

### Lesson 4 - Overfitting and Underfitting
EarlyStopping callbacks monitor validation loss to prevent overfitting by stopping training when performance plateaus.

### Lesson 5 - Dropout and Batch Normalization
Dropout layers randomly disable neurons during training, while batch normalization stabilizes learning by normalizing layer inputs.

### Lesson 6 - Binary Classification
Sigmoid activation in output layer with binary cross-entropy loss enables two-class prediction tasks.

## Notebooks

- `notebooks/deep-learning/tensorflow-experiments.ipynb` - TensorFlow installation verification
- `notebooks/deep-learning/neural-networks.ipynb` - Lessons 1-5 implementations
- `notebooks/deep-learning/dl-binary-classification.ipynb` - Binary classification with ion dataset
- `notebooks/feature-engineering/Mutual_Information.ipynb` - Mutual information scores with the Ames housing and automobile datasets

## Data Sources

The CSV files in `resources/` are small sample datasets used by Kaggle's [Intro to Deep Learning](https://www.kaggle.com/learn/intro-to-deep-learning) and [Feature Engineering](https://www.kaggle.com/learn/feature-engineering) courses by Ryan Holbrook. They are included here only so the notebooks run as-is, and remain subject to the terms of their original sources:

- `red-wine.csv` - [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) (Cortez et al., 2009), UCI Machine Learning Repository
- `concrete.csv` - [Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) (I-Cheng Yeh, 1998), UCI Machine Learning Repository
- `ion.csv` - [Ionosphere](https://archive.ics.uci.edu/dataset/52/ionosphere) (Sigillito et al., 1989), UCI Machine Learning Repository
- `ames.csv` - [Ames Housing](https://jse.amstat.org/v19n3/decock.pdf) (Dean De Cock, 2011)
- `autos.csv` - [Automobile](https://archive.ics.uci.edu/dataset/10/automobile) (Jeffrey Schlimmer, 1985), UCI Machine Learning Repository; cleaned subset used in the Feature Engineering course
- `fuel.csv` - vehicle fuel economy data from the U.S. DOE / EPA [fueleconomy.gov](https://www.fueleconomy.gov/feg/download.shtml) website, as packaged in the `FuelEconomy` data of the R package [AppliedPredictiveModeling](https://cran.r-project.org/package=AppliedPredictiveModeling)

## Next Steps

- Classify images with TPUs in [**Petals to the Metal**](https://www.kaggle.com/c/tpu-getting-started)
- Create art with GANs in [**I'm Something of a Painter Myself**](https://www.kaggle.com/c/gan-getting-started)
- Classify Tweets in [**Real or Not? NLP with Disaster Tweets**](https://www.kaggle.com/c/nlp-getting-started)
- Detect contradiction and entailment in [**Contradictory, My Dear Watson**](https://www.kaggle.com/c/contradictory-my-dear-watson)

## License

The code and notebooks in this repository are released under the [MIT License](LICENSE). The license does not cover the datasets in `resources/` (see [Data Sources](#data-sources)) or the Kaggle course material the notebooks are based on.

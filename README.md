# TensorFlow Basics

Deep learning experiments using TensorFlow and Keras, based on [Kaggle's Intro to Deep Learning](https://www.kaggle.com/learn/intro-to-deep-learning) course.

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

- `notebooks/tensorflow-experiments.ipynb` - TensorFlow installation verification
- `notebooks/neural-networks.ipynb` - Lessons 1-5 implementations
- `notebooks/dl-binary-classification.ipynb` - Binary classification with ion dataset

## Next Steps

- Classify images with TPUs in [**Petals to the Metal**](https://www.kaggle.com/c/tpu-getting-started)
- Create art with GANs in [**I'm Something of a Painter Myself**](https://www.kaggle.com/c/gan-getting-started)
- Classify Tweets in [**Real or Not? NLP with Disaster Tweets**](https://www.kaggle.com/c/nlp-getting-started)
- Detect contradiction and entailment in [**Contradictory, My Dear Watson**](https://www.kaggle.com/c/contradictory-my-dear-watson)
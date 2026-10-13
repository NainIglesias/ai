# Machine Learning Algorithms: A Historical Introduction

## The Evolution of Machine Learning

Machine learning, as a field, has evolved over several decades, with different algorithms emerging to solve specific types of problems. Understanding the historical context helps us appreciate why certain algorithms were developed and when to use each one.

Machine learning encompasses three fundamental paradigms:
- **Supervised Learning**: Learning from labelled examples (input-output pairs)
- **Unsupervised Learning**: Discovering patterns in unlabelled data
- **Reinforcement Learning**: Learning through interaction and feedback

## Timeline of Key Algorithms

### Linear Regression (1805)

**Purpose:** Predict a continuous value from input features.

**History:** The method of least squares, which fits it, was published by Legendre in 1805 and by Gauss in 1809.

**Why it matters:** It established the foundation of supervised learning, and it is still widely used for its simplicity and interpretability.

### Principal Component Analysis (1901)

**Purpose:** Unsupervised dimensionality reduction: summarise many correlated features with a few new ones.

**History:** Introduced by Karl Pearson in 1901 and developed by Harold Hotelling in 1933.

**Why it matters:** It compresses data, removes redundancy and makes high-dimensional data visible in two or three dimensions.

### Logistic Regression (1940s–1950s)

**Purpose:** Classification, particularly binary classification (yes/no, true/false).

**History:** It applies the logistic (sigmoid) function, which Pierre-François Verhulst had used in the 1830s and 1840s to model population growth. Joseph Berkson named the *logit* in 1944, and David Cox developed logistic regression as a regression method in 1958.

**Why it matters:** Despite its name, it is a classification algorithm: it turns a linear combination of the features into a probability. A neuron with a sigmoid activation computes exactly this.

### K-Nearest Neighbors (1951–1967)

**Purpose:** Both classification and regression through similarity-based learning.

**History:** Proposed by Evelyn Fix and Joseph Hodges in 1951, and analysed by Thomas Cover and Peter Hart in 1967.

**Why it matters:** KNN introduced instance-based learning (lazy learning): no explicit model is built during training, and a prediction looks at the most similar stored examples. It is intuitive, but predicting can be slow on large datasets.

### K-Means Clustering (1957)

**Purpose:** Unsupervised learning for grouping similar data points into clusters.

**History:** Stuart Lloyd devised the standard algorithm in 1957 (published only in 1982), and James MacQueen named it *k-means* in 1967.

**Why it matters:** It was one of the first widely used unsupervised algorithms, and it remains common for customer segmentation, image compression and data exploration.

### The Perceptron (1958)

**Purpose:** Binary classification with a single artificial neuron that learns its weights from examples.

**History:** Frank Rosenblatt, 1958.

**Why it matters:** It is the ancestor of every neural network ([Neural networks from the outside](neural_networks.md)).

### Naive Bayes (1960s)

**Purpose:** Classification by Bayes' theorem, assuming that the features are independent of each other within each class.

**History:** Used for classifying text from the early 1960s; it became the classic spam filter at the end of the 1990s.

**Why it matters:** It trains in a single pass over the data and works surprisingly well with many features, such as the words of a text, even though its independence assumption is almost never true.

### Decision Trees (1960s-1990s)

**History:** The concept emerged in the 1960s, but modern algorithms were developed later:
- **CART (Classification and Regression Trees)** (1984)
- **ID3** (1986)
- **C4.5** (1993) - an improvement of ID3

**Purpose:** Both classification and regression through hierarchical decision-making.

**Why it matters:** Decision trees are highly interpretable and can capture non-linear relationships. They became the foundation for powerful ensemble methods like Random Forests and Gradient Boosting.

### Q-Learning (1989)

**Purpose:** Reinforcement learning for sequential decision-making through trial and error.

**History:** Christopher Watkins, 1989.

**Why it matters:** Unlike supervised learning (which learns from labelled examples) or unsupervised learning (which finds patterns), reinforcement learning learns by interacting with an environment and receiving rewards or penalties. This approach has proven crucial for robotics, game playing, and autonomous systems.

**Key concept:** The algorithm builds a "Q-table" that stores the expected future reward for each action in each state, gradually learning optimal behaviour through experience.

### Support Vector Machines (1992–1995)

**Purpose:** Classification (and, with variants, regression) by finding the boundary that separates the classes with the widest possible margin.

**History:** Bernhard Boser, Isabelle Guyon and Vladimir Vapnik added the *kernel trick* in 1992, which lets the boundary be curved; Corinna Cortes and Vapnik allowed some examples on the wrong side, the *soft margin*, in 1995.

**Why it matters:** For a decade they were among the most accurate classifiers available, and they still work well on small and medium datasets.

### Boosting (1995–2001)

**Purpose:** Ensemble method that trains many weak models in sequence, each one correcting the errors of the ones before.

**History:** Yoav Freund and Robert Schapire's AdaBoost (1995), and Jerome Friedman's gradient boosting (2001), which generalised the idea to any differentiable loss.

**Why it matters:** Gradient-boosted trees (XGBoost, LightGBM, CatBoost) are today the strongest general-purpose models for tabular data.

### Random Forests (2001)

**Purpose:** Ensemble method for classification and regression that improves upon single decision trees.

**History:** Leo Breiman, 2001.

**Why it matters:** A random forest averages many deep trees, each trained on a random sample of the examples and considering a random subset of the features at each split. Each tree overfits in its own way, so their errors partly cancel out: averaging reduces the variance of a single tree. (Combining *weak* learners is the idea of boosting, not of random forests.)

## Which Paradigm Each Algorithm Belongs To

| Paradigm | Algorithms above | Tasks |
| --- | --- | --- |
| Supervised | Linear regression | Regression |
| Supervised | Logistic regression, perceptron, naive Bayes | Classification |
| Supervised | KNN, decision trees, SVMs, random forests, boosting | Both classification and regression |
| Unsupervised | K-means | Clustering |
| Unsupervised | PCA | Dimensionality reduction |
| Reinforcement | Q-learning | Sequential decisions from rewards |

The paradigms themselves, and when to use each, are explained in [Machine learning paradigms](machine_learning_paradigms.md).

## The Modern Era

Today's machine learning landscape has evolved to include:
- **Deep Learning (from 2012):** Neural networks with many layers: convolutional networks for images, recurrent networks and LSTMs for sequences
- **Advanced Ensemble Methods:** XGBoost (2014), LightGBM and CatBoost (2017)
- **Transfer Learning:** Reusing pre-trained models to solve new problems
- **Transformers and Large Language Models:** the transformer architecture (2017), BERT and the first GPT (2018), and the chat assistants built on large language models (ChatGPT, 2022; Claude, Gemini and others since)
- **Deep Reinforcement Learning:** DQN playing Atari games (2013–2015), AlphaGo (2016), AlphaZero (2017), and reinforcement learning from human feedback in chat assistants

However, the classical algorithms we study remain fundamental because:
- They're often the best choice for small to medium-sized datasets
- Several of them (linear models, small decision trees) are interpretable and explainable, which matters in regulated industries
- They serve as building blocks for more complex methods
- They're computationally efficient and often need less data than deep learning
- They're essential for understanding modern ML concepts
- Many state-of-the-art solutions still use these algorithms (e.g., XGBoost is based on decision trees)

## Choosing the Right Algorithm

The choice of algorithm depends on several factors:

| Factor | Consider |
|--------|----------|
| **Problem Type** | Classification, regression, clustering, or sequential decision-making? |
| **Data Availability** | Do you have labelled data? Unlabelled? Or can you define rewards? |
| **Data Size** | Small datasets favour simpler models; large datasets can leverage complex models |
| **Interpretability** | Do you need to explain predictions? (Use linear models, decision trees) |
| **Speed** | Training time vs. prediction time trade-offs |
| **Accuracy Requirements** | Simple models may suffice; complex problems may need ensembles |
| **Data Properties** | Linear vs. non-linear relationships, presence of outliers, feature interactions |
| **Sequential Decisions** | If actions affect future states, consider reinforcement learning |

> [Scikit-learn: choosing the right estimator](https://scikit-learn.org/stable/machine_learning_map.html)

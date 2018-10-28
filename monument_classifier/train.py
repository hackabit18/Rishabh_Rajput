import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
#from support_functions import generate_features_targets, plot_confusion_matrix, calculate_accuracy
import pandas as pd
from matplotlib import pyplot as plt
import itertools
import pickle


def calculate_accuracy(predicted_classes, actual_classes, ):
    return sum(actual_classes[:] == predicted_classes[:]) / len(actual_classes)


def generate_features_targets(csv_name):
    print("Generating features...")
    data = pd.read_csv("train_data.csv", header=None, index_col=False)
    data = data.sample(frac=1).reset_index(drop=True)
    output_targets = np.empty(shape=(data.shape[0]), dtype=float)
    output_targets[:] = data.iloc[:,0]

    input_features = np.empty(shape=(data.shape[0],(data.shape[1]-1)), dtype=float)
    input_features[:, :] = data.iloc[:, 1:]

    return input_features, output_targets


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, "{}".format(cm[i, j]),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')


# complete this function to get predictions from a random forest classifier
def rf_predict_actual(data, n_estimators):
  # generate the features and targets
    features, targets = generate_features_targets(data)
  # instantiate a random forest classifier using n estimators
    print("Creating and training random forest classifier...")
    rfc = RandomForestClassifier(n_estimators=n_estimators)
    rfc.fit(features, targets)
    print("Trained model!")
    filename = 'finalized_model.sav'
    print("Saving model in pickle (yum!)...")
    pickle.dump(rfc, open(filename, 'wb'))
    print("Saved!")
    
    #random_forest_pkl_filename = 'random_forest_classifier.pkl'
# Open the file to save as pkl file
    #random_forest_model_pkl = open(random_forest_pkl_filename, 'wb')
    
    
    #spickle.dump(rfc, random_forest_model_pkl)
# Close the pickle instances
    #random_forest_model_pkl.close()
  # get predictions using 10-fold cross validation with cross_val_predict
    predictions = cross_val_predict(rfc, features, targets, cv=10)
  # return the predictions and their actual classes
    return predictions, targets


def meow():
    data = 'train_data.csv'

  # get the predicted and actual classes
    number_estimators = 50       # Number of trees
    predicted, actual = rf_predict_actual(data, number_estimators)

  # calculate the model score using your function
    accuracy = calculate_accuracy(predicted, actual)
    print("Accuracy score:", accuracy)

  # calculate the models confusion matrix using sklearns confusion_matrix function
    class_labels = list(set(actual))
    model_cm = confusion_matrix(y_true=actual, y_pred=predicted, labels=class_labels)

    
  # plot the confusion matrix using the provided functions.
    plt.figure()
    plot_confusion_matrix(model_cm, classes=class_labels, normalize=False)
    plt.show()

meow()
    


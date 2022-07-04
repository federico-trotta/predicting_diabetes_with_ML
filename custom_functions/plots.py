#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import matplotlib.pyplot as plt
import seaborn as sns


# # LABELING PLOTS

# %%


def get_label(TITLE, X, Y):
    ''' 
    The get_label() function appends the labels to a seaborn plot. Arguments in the following order:
    Title, x label, y label
    '''
    plt.title(TITLE)
    plt.xlabel(X)
    plt.ylabel(Y)
    plt.show


# %%





# # PLOTTING KDE

# %%


def plot_kde(y_test, y_test_pred):
    ''' 
    The plot(kde) function plots the KDE. Inputs are just real and predicted y values, in this order:
    y_test, y_test_pred
    '''
    #figsize
    plt.figure(figsize=(10, 7))

    #Kernel Density Estimation plot
    ax = sns.kdeplot(y_test, color='r', label='Actual Values') #actual values
    sns.kdeplot(y_test_pred, color='b', label='Predicted Values', ax=ax) #predicted values

    #showing title
    plt.title('Actual vs Precited values')
    #showing legend
    plt.legend()
    #showing plot
    plt.show()


# %%





# # PLOTTING ACTUAL VS PREDICTED SCATTERPOT WITH A LINE

# %%


def scatter_with_regr(y_test, y_test_pred):
    ''' 
    The scatter_with_regr() function plots actual vs predicted values with a regression line.
    Arguments in the following order:
    y_test, y_test_pred
    '''
    #figure size
    plt.figure(figsize=(10, 7))

    #scatterplot of y_test and y_test_pred
    plt.scatter(y_test, y_test_pred)
    plt.plot(y_test, y_test, color='r')

    #labeling
    plt.title('ACTUAL VS PREDICTED VALUES')
    plt.xlabel('ACTUAL VALUES')
    plt.ylabel('PREDICTED VALUES')

    #showig plot
    plt.show()


# %%





# # RESIDUALS PLOT

# %%


def plot_residuals(y_test, y_test_pred, title, x_label, y_label):
    ''' 
    The plot_residuals() function plots the residuals. Arguments have to be passed in thid order:
    y_test, y_test_pred, title, x_label and y_label.
    REMEMBER: when invoking the function, y_test e y_test_pred have to be passed
    with no quotation marks if are not from
    the same dataframe (as usually it is).
    Then, pass: title, x_label and y_label (usying quotation marks)
    '''
    #figure size
    plt.figure(figsize=(10, 7))

    #residual plot
    sns.residplot(x=y_test, y=y_test_pred)

    #labeling
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


# %%





# # PRINT DOCUMENTATION

# %%


print(get_label.__doc__)
print(plot_kde.__doc__)
print(scatter_with_regr.__doc__)
print(plot_residuals.__doc__)


# %%





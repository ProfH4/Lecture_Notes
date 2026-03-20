#!/usr/bin/env python3

import numpy as np  # Importing NumPy for numerical computations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting
from sklearn.linear_model import LinearRegression, LogisticRegression  # Importing built-in models from sklearn
from sklearn.model_selection import train_test_split  # Function to split data into training and testing sets
from sklearn.metrics import mean_squared_error, accuracy_score  # Evaluation metrics for models

class Auto:
  reifen = None
  fenster = None
  farbe = None

  def __init__(self, rf, fr, fb):
    reifen = rf
    fenster = fr
    farbe = fb

  def fahren(self, richtung):
    print(f"Fährt Richtung: {richtung}")


def linear_regression_simple(X, y):
  """Computes Linear Regression parameters manually."""
  
  x_mean = np.mean(X)  # Compute mean of X
  y_mean = np.mean(y)  # Compute mean of y
  
  numerator = np.sum((X - x_mean) * (y - y_mean))  # Compute numerator of slope
  denominator = np.sum((X - x_mean) ** 2)  # Compute denominator of slope
  slope = numerator / denominator  # Compute slope (m)
  intercept = y_mean - slope * x_mean  # Compute intercept (b)
  
  return slope, intercept  # Return computed slope and intercept
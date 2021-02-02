# -*- coding: utf-8 -*-

#Basic Functions to show proof of method. 
import pandas as pd
import numpy as np

class DatasetView:
  def viewtop(self ,data):
    self.data = data
    view = self.data.head()
    return view

  def viewbottom(self ,data):
    self.data = data
    view = self.data.tail()
    return view

  def viewstats(self ,data):
    self.data = data
    mean = self.data.mean()
    median = self.data.median()
    mode =self.data.mode()
    return mean, median, mode

  def viewnull(self ,data):
    self.data = data
    view = self.data.notnull()
    return view

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This file contains python functions to read text and identify temporal data
like: days, weeks, year, time and finally return the number of days that content relates to.
Example1: Its been 9 weeks since experiencing any symptoms
Output: 63
Example2: entering third month post recovery
Output: 90
Code by Rajath C S.
Code Version: 1.1.0 
"""
# TODO: In the next version update all TODOs

# Importing Libraries
import dateparser
import pandas as pd
from number_parser import parse
from dateparser.search import search_dates
from datetime import *
import re
import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

# downloading stopwords
nltk.download('stopwords')


# #Static methods# #
def date_parser(parsedtime):
  """
  function to parse the formated text to dateparser library and calculate the number of days
  """
  sParsing = dateparser.parse(parsedtime)
  if sParsing != None:
    sParsing = sParsing.date()
    getDays = (datetime.now().date() - sParsing).days
    getDays = str(getDays)
  else:
    dateSearch = search_dates(parsedtime)
    if dateSearch != None:
      getDays = ((datetime.now().date() - dateSearch[0][1].date()).days)
      getDays = str(getDays)
    else:
      getDays = '9999'
  return getDays

def convert_non_ascii(text):
  """
  function to covert the non-unicode string literal to unicode
  """
  encoded_string = text.encode("ascii", "ignore")
  decode_string = encoded_string.decode()
  return decode_string

def data_analysis(text):
  # print('cleaned_text_pre_data_analysis',text)
  """
  function to perform temporal text identification following a rule based pattern
  """
  #TODO: check if the entered text is a string or not. If its integer, output directly. Check the same in date_parser method
  monthsList = ['january', 'jan', 'february', 'march', 'april', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'august', 'september', 'past', 'october', 'november', 'dec', 'december', 'nov', 'oct', 'sept', 'aug']
  weekPattern1 = r'^\d+(wks|wk)$'
  weekPattern2 = r'^(wks|wk)\d+$'
  dayPattern1 = r'^\d+(day|days|d)$'
  dayPattern2 = r'^(day|days|d)\d+$'
  monthPattern3 = r'^\d+(mths|mth)$'
  monthPattern4 = r'^(mths|mth)\d+$'
  splitData = text.split()
  # print('splitData:',splitData)
  if (len(splitData) == 2):
    if ((splitData[0].startswith('wk') or splitData[0].startswith('wks') ) and (type(eval(splitData[1])) == int)):
      splitData[0] = 'weeks'
      splitData[0], splitData[1] = splitData[1], splitData[0]
      parsedValue = date_parser(' '.join(splitData))
    elif ((splitData[1].startswith('wk') or splitData[1].startswith('wks')) and (type(eval(splitData[0])) == int)):
      splitData[1] = 'weeks'
      parsedValue = date_parser(' '.join(splitData))
    elif ((splitData[0].startswith('mth') or splitData[0].startswith('mths') ) and (type(eval(splitData[1])) == int)):
      splitData[0] = 'months'
      splitData[0], splitData[1] = splitData[1], splitData[0]
      parsedValue = date_parser(' '.join(splitData))
    elif ((splitData[1].startswith('mth') or splitData[1].startswith('mths')) and (type(eval(splitData[0])) == int)):
      splitData[1] = 'months'
      parsedValue = date_parser(' '.join(splitData))
    elif ((splitData[0] in monthsList) or (splitData[1] in monthsList)):
      parsedValue = date_parser(' '.join(splitData))
    elif not (splitData[0].startswith('week') or splitData[0].startswith('weeks') or splitData[1].endswith('week') or splitData[1].endswith('weeks') or splitData[0].startswith('day') or splitData[0].startswith('days') or splitData[1].endswith('day') or splitData[1].endswith('days') or splitData[1].endswith('month') or splitData[1].endswith('months') or splitData[0].startswith('month') or splitData[0].startswith('months')):
      date_parser(' '.join(splitData))
    try:
      if ((splitData[0].startswith('month') or splitData[0].startswith('months') or splitData[0].startswith('day') or splitData[0].startswith('days') or splitData[0].startswith('week') or splitData[0].startswith('weeks')) and (type(eval(splitData[1])) == int)):
        splitData[0], splitData[1] = splitData[1], splitData[0]
        parsedValue = date_parser(' '.join(splitData))
      elif ((splitData[1].endswith('month') or splitData[1].endswith('months') or splitData[1].endswith('day') or splitData[1].endswith('days') or splitData[1].endswith('week') or splitData[1].endswith('weeks')) and (type(eval(splitData[0])) == int)):
        parsedValue = date_parser(' '.join(splitData))
    except:
      pass
  elif (len(splitData) == 1) and ('week' in splitData[0] or 'weeks' in splitData[0]):
    if re.findall(r'^[0-9][week].*', splitData[0]):
      parsedValue = date_parser(''.join(splitData))
    elif re.findall(r'^[week|weeks].*', splitData[0]):
      splitData[0] = 'one week'
      parsedValue = date_parser(''.join(splitData))
  elif len(splitData) == 1:
    if splitData[0] in monthsList:
      parsedValue = date_parser(''.join(splitData))
    elif splitData[0] == 'month' or splitData[0] == 'months':
      splitData[0] = 'one month'
      parsedValue = date_parser(''.join(splitData))
    elif re.findall(weekPattern1, splitData[0]):
      newstring = re.sub(r'wks|wk',' weeks',splitData[0])
      data_analysis(newstring)
    elif re.findall(weekPattern2, splitData[0]):
      newstring1 = re.sub(r'wks|wk','weeks ',splitData[0])
      data_analysis(newstring1)
    elif re.findall(dayPattern1, splitData[0]):
      newDayString = re.sub(r'days|day|d',' days',splitData[0])
      data_analysis(newDayString)
    elif re.findall(dayPattern2, splitData[0]):
      newDayString1 = re.sub(r'days|day|d','days ',splitData[0])
      data_analysis(newDayString1)
    elif re.findall(monthPattern3, splitData[0]):
      newDMonthString1 = re.sub(r'mths|mth',' months',splitData[0])
      data_analysis(newDMonthString1)
    elif re.findall(monthPattern4, splitData[0]):
      newDMonthString2 = re.sub(r'mths|mth','months ',splitData[0])
      data_analysis(newDMonthString2)
  else:
    parsedValue = date_parser(' '.join(splitData))
# TODO: If the number associated with weeks is greater than 52, revert output to 9999
  # print('output_value',parsedValue)
  return parsedValue

class TemporalTextAnalysis(object):
  def __init__(self):
    pass

  def text_cleaning(self, original_text):
    # print('original_text',original_text)
    #TODO: rename this function to 'retrive_days'
    """
    function to perform text cleaning so the 'dateparse' library understands context of time related data in a proper format.
    """
    # TODO: check if the passes value is empty string and assign '9999' as output value
    # TODO: use the remove_punt used in vaderSentiment codebase
    original_text = original_text.strip()
    remove_punctuation = [char for char in original_text if char not in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"] # removing special characters
    remove_punctuation = ''.join(remove_punctuation)
    remove_stopwords = [word for word in remove_punctuation.split() if word.lower() not in stopwords.words('english')] # removing stop words
    remove_stopwords = ' '.join(remove_stopwords)
    convert_non_unicode = [convert_non_ascii(word) for word in remove_stopwords.split()] # converting non-unicode characters to their unicode equivalent
    convert_non_unicode = ' '.join(convert_non_unicode)
    # removing unrelated terms based on their, the below list of words were 
    #TODO: Make the below line more dynamic
    remove_extra_words = [word for word in convert_non_unicode.split() if word.lower() not in ['ive', 'many', 'late','past', 've', 'tomo', 'almost','postcovid','tomorrow', 'it', 'its', 'it\'s','last','self', 'isolation', 'symptoms', 'symptom', 'selfisolation', 'continue', 'continues', 'im', 'first', 'cv','nearly', 'quarantine', 'something', 'right', 'relief', 'ill', 'beginning','begin', 'begins', 'starting', 'initial', 'life','due', 'took', 'several','end','covid','since','lockdown','fever','ago','early','symptoms','later','results','onwards','suspected','covid19','long','got','sick','feel','suffer','suffering','struggling','virus','ongoing','worse','kick','kicked','viral','usual','get','worst','post','currently','middle','mid','between','experiencing','better','coming','came','come','began','illness','made','started','mild','onset','first']]
    remove_extra_words = ' '.join(remove_extra_words)
    remove_single_char = [word for word in remove_extra_words.split() if word.lower() not in "abcdefghijklmnopqrstuvwxyz"]
    remove_single_char = ' '.join(remove_single_char)
    remove_length_words = [word for word in remove_single_char.split() if len(word.lower()) < 15] # Based on a common understanding that temporal text cannot exceed 15 characters combined
    remove_length_words = ' '.join(remove_length_words)
    text_to_numeric = parse(remove_length_words)
    # print('text2numberic',text_to_numeric)
    processed_data = data_analysis(text_to_numeric)
    return processed_data

  def days_number():
    """
    check for the appropriateness of total number of days value generated and update accordingly
    """
  # TODO: Assuming COVID-19 start date is considered as Jan 1st 2020. Jan 1st 2020 to current system date will be XYZ number of days.
  # The number of days generated by the program cannot exceed this date, if exceeded the days returned should be '9999'
    pass
  # TODO: try https://github.com/FraBle/python-sutime
  # TODO: create class object and write test cases within main function.
  # TODO: detect and remove vulgur/obscene terminologies

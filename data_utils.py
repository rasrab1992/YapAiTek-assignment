from __future__ import unicode_literals

import os
import re
from hazm import *
import pandas as pd
import numpy as np
import docx







def prepare_data(file_path, result_path):
    """
    This Method prepares the datas and returns a string list of all comments and a           string list of result_words. file_path is path of csv file of all comments and           result_path is path of result csv file. 
    
    file_path: Path of source csv file
    result_path: Path of result csv file
    
    
    comments_list: String list of all comments 
    result_words: String list of result_words
    """
    
    comments_list = []
    #Labeling the columns
    new_Index = ['Date', 'News']
    
    results  = pd.read_csv(result_path, encoding = "UTF-8")
    #result_words is a list of all stocks name
    result_words = results["symbolFA"]
    result_words = [f"{r}" for r in result_words]
    
    
    comments = pd.read_csv(file_path, encoding = "UTF-8")
    first_row = np.array(comments.columns)
    comments.columns = new_Index
    new_row = pd.DataFrame({'Date':first_row[0], 'News':first_row[1]},index =[0])
    #Regulared comments
    comments = pd.concat([new_row, comments]).reset_index(drop = True) 

    #A list of regulared comments
    for row in range(0,len(comments.index)):
        comments_list.append(str(comments['News'][row]))
        
        
    return comments_list, result_words





def tokenizer(text):
    """
    This function creates a list of tokenized text and returns it.
    For tokenizing each sentence this function calls sent_tokenizer function of hazm         module
    text: Input string for tokenizing
    
    """
    #creating normalizer object
    normalizer = Normalizer()
    #normalizing the text
    text = normalizer.normalize(text)
    #replacing {*,"“”,\n, …, +, -, /, =, (, ), ‘•:,[, ], |, ’, ;} with space
    text = re.sub(r"[\*\"“”\n\\…\+\-\/\=\(\)‘•:\[\]\|’;]", " ", str(text))
    text = re.sub(r"[ ]+", " ", text)
    text = re.sub(r"\!+", "!", text)
    text = re.sub(r"\.+", ".", text)
    text = re.sub(r"\,+", ",", text)
    text = re.sub(r"\?+", "?", text)
    # return tokenized texts
    return [f'{token}' for sent in sent_tokenize(text) for token in word_tokenize(sent)]


def tokenize_all(cmnt_list):
    """
    This function creates a list of all tokenized comments and returns it.
    For tokenizing each comment this function calls tokenizer function.
    
    cmnt_list: String list of comments 
    
    """
    return [tokenizer(cmnt) for cmnt in cmnt_list]




def result_clean_stopwords(sents, results, stopwords_path):
    """
    This function takes tokenized list of all comments and result list.
    Cleans the source file from stopwords and other words that aren't in result list.
    
    sents: Tokenized list of all comments
    results: List of all result word for searching.
    stopword_path: The path of stopwords file
    
    cleaned: The cleaned source file from stopwords and other words that aren't in esult     list
    """
    
    cleaned = []
    #reading the stopwords file
    doc = docx.Document(stopwords_path)
    #creating a list of all stopwords
    stopwords = [f'{p.text}' for p in doc.paragraphs]
    
    for i in range(len(sents)):
        for word in sents[i]:
            if word not in stopwords:
                if word in results:
                     cleaned.append(word)
    return cleaned
  
    
    


def sorted_count_frequency(list_in): 
    
    """
    This function takes a list of words and returns a dictionary that sorted by number       of each word.
    
    list_in: List for sorting
    sorted_result: Output sorted dictionary
    """
    
   # Creating an empty dictionary 
    freq = {} 
    for item_i in list_in:
        if (item_i in freq): 
            freq[item_i] += 1
        else: 
                freq[item_i] = 1
    sorted_result = sorted(freq.items(),reverse=True, key=lambda item: item[1])
    
    return sorted_result




def cleaned_sorted_count_frequency(sents, results, stopwords_path):
    """
    This function takes tokenized list of all comments and result list.
    calls  result_clean_stopwords() to cleans the source file from stopwords and other words that aren't in result list.Then sends the result list to sorted_count_frequency() for counting the result words in list. At the end gives the sorted dictionary.
    
    sents: Tokenized list of all comments
    results: List of all result word for searching.
    stopword_path: The path of stopwords file
    
    all_sorted: Sorted dictionary
    
    """
    
    temp = result_clean_stopwords(sents, results, stopwords_path)
    all_sorted = sorted_count_frequency(temp)

    return all_sorted
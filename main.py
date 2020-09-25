import csv
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Full text in category ham
category_ham = ''
# Full text in category spam
category_spam = ''
# List of each word in category spam
words_spam = []
# List of words in category spam
word_spam_count = []
# List of each word in category ham
words_ham = []
# List of words in category ham
word_ham_count = []
# List of each sentence in category spam
sentences_spam = []
# List of each sentence in category ham
sentences_ham = []
# Count of all words in category spam
count_of_all_words_spam = 0
# Count of all words in category ham
count_of_all_words_ham = 0
# List of numbers to delete
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# List of special symbols to delete
special_symbols = {'\n', '\b', '\f', '\r', '\t', '\v', '\a', '$', '\0', '^', '|', '[', ']', '(', ')', '*', '.', '"',
                   '\\', '/', '&', ';', '#', '@', '!', '`', '`', '%', '_', '-', '+', '=', '{', '}', '<', '>', '?', ':',
                   '№', '	', "'", ',', '‰', '©'}
# List of stop words to delete
stop_words = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
              'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
              'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
              'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me',
              'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both',
              'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and',
              'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
              'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too',
              'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my',
              'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}


# Function deletes numbers
def delete_numbers(text):
    return ''.join([char for char in text if char not in numbers])


# Function deletes special symbols
def delete_special_symbols(text):
    return ''.join([char for char in text if char not in special_symbols])


# Function deletes stop words
def delete_stop_words(text):
    tokenized_row = word_tokenize(text)

    return ''.join(' '.join([char for char in tokenized_row if char not in stop_words]))


# Function do stemming
def porter_stammer(text):
    porter = PorterStemmer()
    tokenized_row = word_tokenize(text)
    result = ''

    for w in tokenized_row:
        result = result + ' ' + porter.stem(w)

    return result


# Function find frequency of each words
def frequency_of_words(text):
    text_split = text.split()
    frequency_text = []

    for w in text_split:
        if w not in frequency_text:
            frequency_text.append(w)

    # for word in range(0, len(frequency_text)):
    # print('Frequency of', frequency_text[word], 'is :', text.count(frequency_text[word]))

    return frequency_text, text_split


# Finding length of each word in the list
def length_of_words(t_list):
    words_lengths = []

    for w in range(0, len(t_list)):
        words_lengths.append(len(t_list[w]))

    return words_lengths


# Finding length of each sentence in the list
def length_of_sentences(t_list):
    sentences_lengths = []

    for w in range(0, len(t_list)):
        sentences_lengths.append(len(t_list[w]))

    return sentences_lengths


# Function find most frequent words
def most_frequent_word(list_of_words, top_list):
    counter = 0
    curr_most_frequent_word = list_of_words[0]

    for w in list_of_words:
        curr_frequency = list_of_words.count(w)
        if curr_frequency > counter:
            if w not in top_list:
                counter = curr_frequency
                curr_most_frequent_word = w

    return curr_most_frequent_word


# Function find average length of words in the list
def average_length_of_words(t_list):
    value = 0
    count = 0

    for w in range(0, len(t_list)):
        value = value + len(t_list[w])
        count = count + 1

    return value / count


# Function find average length of sentences in the list
def average_length_of_sentences(t_list):
    value = 0
    count = 0

    for w in range(0, len(t_list)):
        value = value + len(t_list[w])
        count = count + 1

    return value / count

def open_file_for_analyze():
    file_dialog = tk.filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"),
                                                                                                ("all files", "*.*")))
    global category_ham, category_spam, sentences_spam, sentences_ham
    with open(file_dialog, "r", newline='') as csvFileRead:
        next(csvFileRead)
        reader = csv.reader(csvFileRead)
        for row in reader:
            rowText = delete_numbers(row[1])
            rowText = delete_special_symbols(rowText)
            rowText = delete_stop_words(rowText)
            rowText = rowText.lower()
            rowText = porter_stammer(rowText)
            if row[0] == 'ham':
                sentences_ham.append(rowText)
                category_ham = category_ham + ' ' + rowText
            else:
                if row[0] == 'spam':
                    sentences_spam.append(rowText)
                    category_spam = category_spam + ' ' + rowText


def analyze():
    p_spam = len(sentences_spam) / (len(sentences_spam) + len(sentences_ham))
    p_ham = len(sentences_ham) / (len(sentences_spam) + len(sentences_ham))
    result = 1.0
    count_not_in = 0

    text = text_field.get('1.0', 'end-1c')

    text = delete_numbers(text)
    text = delete_special_symbols(text)
    text = delete_stop_words(text)
    text = text.lower()
    text = porter_stammer(text)
    text_edited = word_tokenize(text)

    for word in text_edited:
        count = category_spam.split().count(word)
        if count != 0:
            result = result * (count / len(category_spam.split()))
        else:
            count_not_in = count_not_in + 1
            result = result * ((count + 1) / (len(category_spam.split()) + count_not_in))
    result_spam = result * p_spam
    result = 1.0
    count_not_in = 0
    for word in text_edited:
        count = category_ham.split().count(word)
        if count != 0:
            result = result * (count / len(category_ham.split()))
        else:
            count_not_in = count_not_in + 1
            result = result * ((count + 1) / (len(category_ham.split()) + count_not_in))
    result_ham = result * p_ham

    normalize = result_spam + result_ham
    result_spam = result_spam / normalize
    result_ham = result_ham / normalize

    label['text'] = 'Ham: ' + str('%.0f' % (result_ham*100)) + '% Spam: ' + str('%.0f' % (result_spam * 100)) + '%'


# Window GUI
window = tk.Tk()
label = tk.Label(window, text="", fg='black', font=("Consolas", 11))
label.place(x=0, y=0)
text_field = tk.Text(window, bd=3)
text_field.place(x=0, y=30, height=60, width=300)
open_file_for_analyze_button = tk.Button(window, text="Select file", fg='black', command=open_file_for_analyze)
open_file_for_analyze_button.place(x=150, y=100)
analyze_button = tk.Button(window, text="Analyze", fg='black', command=analyze)
analyze_button.place(x=90, y=100)
window.title('Bayes')
width = window.winfo_width() + (2 * window.winfo_rootx() - window.winfo_x())
height = window.winfo_height() + (window.winfo_rooty() - window.winfo_y() + window.winfo_rootx() - window.winfo_x())
window.geometry('300x130')
window.eval('tk::PlaceWindow . center')
window.resizable(width=False, height=False)
window.mainloop()
# END Window GUI

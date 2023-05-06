ham_1 = open("data\myham\ham_train1.txt").readlines()
ham_2 = open("data\myham\ham_train2.txt").readlines()
ham_3 = open("data\myham\ham_train3.txt").readlines()
spam_1 = open("data\myspam\spam_train1.txt").readlines()
spam_2 = open("data\myspam\spam_train2.txt").readlines()
spam_3 = open("data\myspam\spam_train3.txt").readlines()
test = open("data\mytest\ham_test.txt").readlines()

ham = ham_1 + ham_2 + ham_3
spam = spam_1 + spam_2 + spam_3



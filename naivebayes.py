from sklearn.feature_extraction.text import CountVectorizer
from datasets import *
import math

bag = CountVectorizer()
bag.fit(ham + spam)
bag_list = [0 for i in range(len(bag.get_feature_names_out()))]
for i in range(len(ham)):
    for j in range(len(bag_list)):
        bag_list[j] += bag.transform([ham[i]]).toarray()[0][j]
bag_words = sum(bag_list)
ham_list = [0 for i in range(len(bag.get_feature_names_out()))]
spam_list = [0 for i in range(len(bag.get_feature_names_out()))]
for i in range(len(ham)):
    for j in range(len(bag_list)):
        ham_list[j] += bag.transform([ham[i]]).toarray()[0][j]
ham_words = sum(ham_list)
ham_likelihood = [0 for i in range(len(bag.get_feature_names_out()))]

for i in range(len(spam)):
    for j in range(len(bag_list)):
        spam_list[j] += bag.transform([spam[i]]).toarray()[0][j]
spam_words = sum(spam_list)
spam_likelihood = [0 for i in range(len(bag.get_feature_names_out()))]

test_bag = CountVectorizer()
test_bag.fit(test)
test_list = [0 for i in range(len(test_bag.get_feature_names_out()))]
for i in range(len(test)):
    for j in range(len(test_list)):
        test_list[j] += test_bag.transform([test[i]]).toarray()[0][j]
test_words = sum(test_list)

test_is_ham = math.log10((ham_words + test_words)/(bag_words + 2*test_words))
test_is_spam = math.log10((spam_words + test_words)/(bag_words + 2*test_words))
for i in range(len(test_list)):
    try:
        test_is_ham += math.log10((ham_list[bag.vocabulary_[test_bag.get_feature_names_out()[i]]] + 1)/(ham_words + 2))*test_list[i]
        test_is_spam += math.log10((spam_list[bag.vocabulary_[test_bag.get_feature_names_out()[i]]] + 1)/(spam_words + 2))*test_list[i]
    except KeyError:
        test_is_ham += math.log10(1/(ham_words + 2)) * test_list[i]
        test_is_spam += math.log10(1/(spam_words + 2)) * test_list[i]
        continue


if test_is_ham > test_is_spam:
    print("ham_test.txt is a ham mail.")
else:
    print("ham_test.txt is a spam mail.")

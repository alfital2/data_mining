import pandas as pd
import Preprocessing_for_knn_and_k_means
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

###################### FILES READER
tmp = open("Structure.txt", "r")
structure_file = []
for line in tmp:
    structure_file.append(line)
tmp.close()
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
########################
preprocessor = Preprocessing_for_knn_and_k_means.Preprocessing_for_knn_and_k_means(train, test, structure_file, 3)
X = train.iloc[:, :-1].values
y = train.iloc[:, 4].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)




#
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#
# print("preprocessing done")

ignored = ["job", "marital", "education", "default", "housing", "loan", "contact", "month", "poutcome", "class",
'admin', 'unknown', 'unemployed', 'management', 'housemaid', 'entrepreneur', 'student', 'blue-collar', 'self-employed', 'retired', 'technician', 'services',
'married', 'divorced', 'single', 'widowed',
'unknown', 'secondary', 'primary', 'tertiary',
'yes', 'no',
'unknown', 'telephone', 'cellular',
'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec',
'unknown', 'other', 'failure', 'success',]
# {
# 'age': 'NUMERIC',
#  'job': ['admin', 'unknown', 'unemployed', 'management', 'housemaid', 'entrepreneur', 'student', 'blue-collar', 'self-employed', 'retired', 'technician', 'services'],
#  'marital': ['married', 'divorced', 'single', 'widowed'],
#  'education': ['unknown', 'secondary', 'primary', 'tertiary'],
#  'default': ['yes', 'no'],
#  'balance': 'NUMERIC',
#  'housing': ['yes', 'no'],
#  'loan': ['yes', 'no'],
#  'contact': ['unknown', 'telephone', 'cellular'],
#  'day': 'NUMERIC',
#  'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'],
#  'duration': 'NUMERIC',
#  'campaign': 'NUMERIC',
#  'previous': 'NUMERIC',
#  'poutcome': ['unknown', 'other', 'failure', 'success'],
#  'class': ['yes', 'no']
#  }

import pandas
url = "https://datahub.io/machine-learning/diabetes/r/diabetes.csv"
data = pandas.read_csv(url)
print(data)
data.tail()

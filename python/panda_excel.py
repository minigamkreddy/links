import pandas as pd

df = pd.DataFrame({'Names':['Andreas', 'George', 'Steve',
		'Sarah', 'Joanna', 'Hanna'],
		'Age':[21, 22, 20, 19, 18, 23]})
df.to_excel('manoj.xlsx')

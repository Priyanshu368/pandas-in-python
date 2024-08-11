import pandas as pd
dict1 ={
    'name':['priyanshu','rohan','shyam','ram'],
    'marks':[100,34,56,87],
    'roll_no.':[2022031056,2022031057,2022031058,2022031060]


}
df =pd.DataFrame(dict1)
print(df)
# how to change the index number
#method-1 by directly in df =pd.DataFrame(dict1,index =['first','second','third','fourth'])
#method -2
df.index=['first','second','third','fourth']
print(df)
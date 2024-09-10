
import pandas as pd
df=pd.read_csv(r"C:\Users\thehe\Downloads\Absenteeism_data.csv")
print(df)

pd.options.display.max_rows = None
pd.options.display.max_columns = None
df.info()
df=df.drop(['ID'],axis=1)
print(df.head())

pd.unique(df['Reason for Absence'])
df_col=df['Reason for Absence'].unique()
print('Reason for Absence:' ,df_col)

sor_list=sorted(df_col)
print('sorted_list:',sor_list)
print(sor_list,df_col)

reason_col=pd.get_dummies(df)
print(reason_col)
column_val=df.columns.values
print('column_val:',column_val)
reason_colvalues=reason_col.columns.values
print(reason_colvalues)
df=df.drop(["Reason for Absence"],axis=1)
print(df)

column_value=df.columns.values
print('column_value:',column_value)


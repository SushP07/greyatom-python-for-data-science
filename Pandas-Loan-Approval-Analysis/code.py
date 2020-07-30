# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

#step1
#Code starts here
bank=pd.DataFrame(bank_data)
#print(bank)

categorical_var=bank.select_dtypes(include='object')
#print(categorical_var)

numerical_var=bank.select_dtypes(include='number')
#print(numerical_var)
#step2
banks=bank.drop(['Loan_ID'],axis=1)

#banks.isnull().sum()

bank_mode=banks.mode().iloc[0]
#print(bank_mode)

banks.fillna(bank_mode,inplace=True)
banks.isnull().sum().values.sum()
#step3

avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values=["LoanAmount"])
#print(avg_loan_amount)

#step4
loan_approved_se = len(banks[(banks.Self_Employed=='Yes') & (banks.Loan_Status=='Y')])
loan_approved_nse = len(banks[(banks.Self_Employed=='No') & (banks.Loan_Status=='Y')])
percentage_se = (loan_approved_se*100)/614
percentage_nse =  (loan_approved_nse*100)/614



#step5
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )


big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)



mean_values=round(banks.groupby('Loan_Status')['ApplicantIncome','Credit_History'].mean(),2)
print(mean_values.iloc[1,0],2)









Name=input("Enter employee's name:")

Hours_Worked=eval(input("Enter number of hours worked in a week:"))

Pay_Rate=eval(input("Enter hourly pay rate:"))

Federal_Tax_Withholding_Rate=(100*(eval(input("Enter federal tax withholding rate:"))))

state_Tax_Withholding_Rate=(100*(eval(input("Enter state tax withholding rate:"))))

Gross_Pay=Hours_Worked*(float(Pay_Rate))

Federal_Withholding=(Gross_Pay*Federal_Tax_Withholding_Rate)/100

State_Withholding=(Gross_Pay*state_Tax_Withholding_Rate)/100

Total_Deduction=State_Withholding+Federal_Withholding

Net_Pay=(Gross_Pay)-(Total_Deduction)

print("Employee Name:",str(Name))

print("Hours Worked:",float(Hours_Worked))

print("Pay Rate:",'$'+str(Pay_Rate))            

print("Gross Pay:",'$'+str(Gross_Pay))

print("Deductions:\n",
      "\t Federal Withholding ("+str(Federal_Tax_Withholding_Rate)+'%'+'):',"$"+str(Federal_Withholding)+"\n",
      "\t State Withholding ("+str(state_Tax_Withholding_Rate)+'%'+'):',"$"+str((int(State_Withholding*100))/100)+"\n",
      "\t Total Deduction:",'$'+str((int(Total_Deduction*100))/100)+"\n",
      "Net Pay:",'$'+str((int(Net_Pay*100))/100))
      

            

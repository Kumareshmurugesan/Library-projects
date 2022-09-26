Days =int(input("total no of days books kept"))
if Days==0:
   print("No fine")
elif Days>1 and Days<5:
   print("you fine amount is :" ,Days*0.5)
elif Days>5 and Days<10:
   print("your fine amount is:" ,Days*1)
elif Days>10 and Days<30:
   print("your fine amount is :",Days*5)
elif Days>30:
   print("your membership is canceled")
else:
   print("Enter valid no.")
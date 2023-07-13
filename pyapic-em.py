import requests
import json


url='https://10.215.26.60/api/v1'
account={
    'username':'admin',
    'password':'vnpro@123'
}
def get_ticket():
    urlticket=url+'/ticket'
    print(urlticket)
    header={
        'Content-type':'application/json'
    }
    response=requests.post(url=urlticket,headers=header,data=json.dumps(account),verify=False)
    print(response.json())
    ticket=response.json()['response']['serviceTicket']
    return ticket
def get_list_devices():
    urlldevice=url+'/network-device'
    header={
        'X-Auth-Token':get_ticket()
    }
    response=requests.get(url=urlldevice,headers=header,verify=False)
    print(response.json())
    return response.json()


# get_list_devices()


# get_ticket()

# demoticket=get_ticket()
# print(demoticket)


def get_id(ip):
    response=get_list_devices()
    for i in response['response']:
        # print(i['managementIpAddress'])
        if i['managementIpAddress']==ip:
            return i['id']
    return None

id=get_id('10.215.26.76')
print(id)


def get_device(id):
    urlldevice=url+'/network-device/{}'.format(id)
    header={
        'X-Auth-Token':get_ticket()
    }
    response=requests.get(url=urlldevice,headers=header,verify=False)
    print(response.json())
    return response.json()
get_device(id=id)
data ={'form': {'name': None, 'email': None, 'total': '700.00'}, 'shipping': {'address': '111111', 'city': '111111', 'state': '111111', 'phonenumber': '08033717850'}}

address=data['shipping']['address']
city=data['shipping']['city']
state=data['shipping']['state']
phonenumber=data['shipping']['phonenumber']


print(address)
print(phonenumber)
print (str(address))
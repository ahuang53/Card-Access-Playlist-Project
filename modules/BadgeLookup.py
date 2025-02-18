import json
import requests

# Function used to register a client to ARTS and save the credentials to file "client_creds.json"
# To Regsiter:
#       1. Go to the ARTS event page, edit the event, select "ORDS Clients", and click "create"
#       2. Call the Register function with the 'badge_num' associated with the user who did step (1)
def Register(badge_num):
    response = requests.post('https://apex.cct.rpi.edu/apex/simon_ords/prox_enroll/apex/{}'.format(badge_num))
    if response.status_code == 200:
        client_creds = response.json()
        with open('client_creds.json','w') as f:
            json.dump(client_creds,f)
        return client_creds
    else:
        return response.status_code

# Function used to lookup a badge ID and return the json information provided by the ARTS interface
# This function will not work without the system having the Register function successfully complete
def Lookup(badge_num,client_creds=0):
    if client_creds == 0:
        try:
            with open('client_creds.json') as f:
                client_creds = json.load(f)
        except FileNotFoundError:
            print('Error: No credential provided and no credentials file client_creds.json found')
            return -1

    cid = client_creds['client_id']
    csec = client_creds['client_secret']
    auth_url = client_creds['auth_url']
    arts_url = client_creds['arts_url']
        
    response = requests.post(auth_url,data={"grant_type":"client_credentials"},auth=(cid,csec),)

    token = response.json()['access_token']

    res = requests.post('{}{}{}'.format(arts_url,'tap/',badge_num),headers={'Authorization':'Bearer {}'.format(token)})
    if response.status_code == 200:
        return res.json()
    else:
        return res.status_code


#print(Register("AE5195F7"))
#print(Lookup("AE5195F7"))


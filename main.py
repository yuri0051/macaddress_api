'''Macaddress Api'''
from argparse import ArgumentParser
import requests

URL = 'https://api.macaddress.io/v1'
API_KEY = ''

def get_company_name(args_):
    '''Returns Company name'''
    payload = {'apiKey': API_KEY, 'output': args_.output, 'search': args_.macaddress}
    resp = requests.get(URL, params=payload)
    status_code = resp.status_code
    if status_code != 200:
        raise ValueError(f'Status code: {status_code}')

    json_resp = resp.json()
    return json_resp['vendorDetails']['companyName']


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--macaddress', help='Enter MAC address', required=True)
    parser.add_argument('--output', default='json')
    args = parser.parse_args()

    company_name = get_company_name(args)
    print(f'Company name: {company_name}')

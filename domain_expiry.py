import sys
from socket import socket
from datetime import datetime


whois_server = 'whois.internic.net'


def get_whois_data(server, domain):
    s = socket()
    s.connect((server, 43))
    with s:
        s.send(bytes(domain + '\r\n', encoding='utf-8'))
        data = ''
        while len(data) < 10000:
            chunk = s.recv(100).decode('utf-8')
            if(chunk == ''):
                break
            data += chunk
        return data
    return None


def parse_whois_data_for_entry(data, field_name):
    '''
    searches a ``data`` string for a line like '``field_name``: value'

    returns value or None if no matching field name could be found
    '''
    entries = data.splitlines()
    for entry in entries:
        if field_name in entry:
            return entry.split(':', 1)[1].strip()
    return None


def get_registrar_whois_server(domain):
    whois_data = get_whois_data(whois_server, domain)
    if whois_data is None:
        print('couldn\'t successfully query whois')
        return None
    else:
        return parse_whois_data_for_entry(whois_data, 'Registrar WHOIS Server')


def convert_to_datetime(date):
    # fromisoformat can't handle a full ISO 8601 string, remove the Z.
    if date[-1] == 'Z':
        date = date[:-1]
    # FIXME: expiration dates with offsets like fart.com, don't ask why I
    # tried that one, and wag.com, cant be converted. It looks like they
    # can be fixed by manually inserting colons in their offsets.
    try:
        date_time = datetime.fromisoformat(date)
    except ValueError:
        print('could not parse datetime, returning date string')
        date_time = date
    return date_time


def domain_expiry_date(domain):
    registrar_server = get_registrar_whois_server(domain)
    whois_data = get_whois_data(registrar_server, domain)
    # now find the expiration date
    date = parse_whois_data_for_entry(
        whois_data, 'Registrar Registration Expiration Date')

    if date is not None:
        return convert_to_datetime(date)
    else:
        print('could not find date in data below:\n{}'.format(whois_data))


if __name__ == "__main__":
    domain = sys.argv[1]
    print(domain_expiry_date(domain))

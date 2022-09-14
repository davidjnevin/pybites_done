import requests

IPINFO_URL = "http://ipinfo.io/{ip}/json"


def get_ip_country_2(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
    parse the json response returning the country code of the IP"""
    ip_info_url = IPINFO_URL.replace("{ip}", ip_address)
    with requests.Session() as sess:
        r = sess.get(ip_info_url).json()
    return r["country"]


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
    parse the json response returning the country code of the IP"""
    ip_info_url = IPINFO_URL.replace("{ip}", ip_address)
    r = requests.get(ip_info_url).json()
    return r["country"]

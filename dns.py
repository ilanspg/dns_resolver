#!/usr/bin/env python

import dns.resolver
import validate

try:
    domain = input("Please type domain name: ")

    print("**************************************")

    answers = dns.resolver.query(domain, 'NS')
    for rdata in answers:
        print('NS Server: ', rdata)

    print("**************************************")

    answers = dns.resolver.query(domain, 'MX')
    for rdata in answers:
        print('MX Record: ', rdata.exchange, 'Priority: ', rdata.preference)

    print("**************************************")

    answers = dns.resolver.query('autodiscover.' + domain, 'CNAME')
    for rdata in answers:
        #if ("autodiscover.outlook.com" not in str(rdata)):
            print('Autodiscover: ', rdata)

    print("**************************************")
    
    answers = dns.resolver.query(domain, 'TXT')
    for rdata in answers:
        if ("v=spf1 " in str(rdata)):
            print('TXT: ', rdata)
            validate.validateRecord(domain,"TXT", str(rdata))

    print("**************************************")
        
    answers = dns.resolver.query('msoid.' + domain, 'CNAME')
    for rdata in answers:
        print('MSOID: ', rdata)

    print("**************************************")
    
except dns.resolver.NoAnswer as err:
    print(err)

except dns.resolver.NXDOMAIN as err:
    print(err)

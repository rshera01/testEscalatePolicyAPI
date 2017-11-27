# testEscalatePolicyAPI
#Python based Restful API  testing call

#!/usr/bin/env python

import urllib
import urllib2
import json, sys
import datetime

API_SERVER = "api.vistara.io"
#API_KEY    = "hbV8Jf4RrCDUW9Sb4PA5CFWh5r3yhXkK"
API_KEY = "wqpeytPsHdKPCVuMSF82PQbt4JT257Hj"

## API_SECRET = "jVpj7XHHsvUUjSxBAv6BdhuquW66TR8Ujg4va2c2TUWjWhyfquSCsPkeQjmskKfZ"
API_SECRET = "ZbAATXmg2DDTeBvkTCPpvtAPyZvWgWDx2rXra87u4scGbekkTuubpE2yr7365RGX"


''' Python HTTP client to make GET/POST requests '''
def httpRequest(url, data=None, headers={}, method='GET',user=None, passwd=None):
    try: 
        http_headers = {
            'Accept'       : 'text/html, */*',
        }
        http_headers.update(headers)
        req = urllib2.Request(url, data, http_headers)
        req.get_method = lambda: method
        if user and passwd:
            passReq = urllib2.HTTPPasswordMgrWithDefaultRealm()
            passReq.add_password(None, url, user, passwd)
            authhandler = urllib2.HTTPBasicAuthHandler(passReq)
            opener = urllib2.build_opener(authhandler)
            urllib2.install_opener(opener)

        request = urllib2.urlopen(req)
        return request.read()
    except urllib2.HTTPError, emsg:
        _msg = emsg.read()
        print emsg.getcode()
        if emsg.getcode() == 500:
            print _msg
            return _msg
        else:
            print emsg.read()
            raise Exception(emsg.reason)
        raise Exception('httpRequest: HTTPError - ' + str(emsg))
    except urllib2.URLError, emsg:
        raise Exception('httpRequest: URLError - ' + str(emsg))
    except Exception, emsg:
        raise Exception('httpRequest: Exception - ' + str(emsg))


''' Get vistara access token using api key/secret for further communication '''
def get_access_token():
    url = "https://%s/auth/oauth/token" % (API_SERVER)

    data = urllib.urlencode({
        "client_id"     : API_KEY,
        "client_secret" : API_SECRET,
        "grant_type"    : "client_credentials"
    })

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept" : "application/json"}
    try:
        result = json.loads(httpRequest(url, data, headers, 'POST'))
        return result['access_token']
    except Exception as emsg:
        raise Exception("Error while getting access token - " + str(emsg))
        sys.exit(2)

print get_access_token()

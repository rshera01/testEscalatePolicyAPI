__author__ = 'cheetah'

import urllib
import urllib2
import json, sys
import datetime


''' Python HTTP client to make GET/POST requests '''
def httpRequest(url, data=None, headers={}, method='POST',user=None, passwd=None):
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
            print "This is 500 error"
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


def create_escalate_alert_policy(data):
    try:
        #url = "https://{0}/api/v2/tenants/{1}/scheduleMaintenances".format(API_SERVER, CLIENT_ID)
        url = "https://api.vistara.io/api/v2/tenants/msp_588058/escalations"
        headers = {'Content-Type': 'application/json', "Authorization" : "Bearer " + "9796d277-rtrt-49c8-trtt-8175d574b038"}
        #result = httpRequest(url, policy_payload(), headers, 'POST')
        #print(result)
        data = policy_payload()
        print data
        result = json.loads(httpRequest(url, data, headers, 'POST'))
        if result.has_key('id'):
            print result['id']
    except Exception as e:
        print ("Failed to create Alert escalate  policy: " +str(e))

def policy_payload():

    policy_data = {
 "name": "SJ Network Maintenance -1 ",
  "description": "API alert policy.",
  "resources": [{
      "id": "bb97b96a-8013-4806-af82-d2504e071910",
      "type": "RESOURCE"
    },
    {
      "id": "11511f16-1933-437e-a0da-81793665c384",
      "type": "RESOURCE"
    }
  ],

  "escalationType": "MANUAL",
  "escalations": [{
    "recipients": [{
        "id": "23744",
        "name": "Test roster - One time - pico",
        "type": "ROASTER"
      }
    ]
  }]
}
    print(policy_data)
    return json.dumps(policy_data)
## create_escalate_alert_policy(policy_payload())
create_escalate_alert_policy(None)

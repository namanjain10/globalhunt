from django.shortcuts import render
from django.views import View
from json import dumps
import requests

class form (View) :
    def get (self, request) :
        return render(request, 'mindful/form.html')

    def post  (self, request) :
        data = request.POST
        dic = {}

        for d in data :
            s = d.split('@')
            if len(s) == 1 :
                dic[s[0]] =  data[d]

            elif len(s) == 2 :
                try :
                    dic[s[0]][s[1]] = data[d]
                except :
                    dic[s[0]] = {}
                    dic[s[0]][s[1]] = data[d]

            elif len(s) == 3 :
                try :
                    dic[s[0]][s[1]][s[2]] = data[d]

                except :
                    try :
                        dic[s[0]][s[1]] = {}
                        dic[s[0]][s[1]][s[2]] = data[d]

                    except :
                        dic[s[0]] = {}
                        dic[s[0]][s[1]] = {}
                        dic[s[0]][s[1]][s[2]] = data[d]

        del(dic['csrfmiddlewaretoken'])
        auth_url  = 'http://awsdev.globalhuntindia.com/Candi/Post/'
        headers = {'content-type':'application/json'}
        r = requests.post(auth_url, headers=headers, data= dumps(dic))
        print (r)
        return render(request, 'mindful/submit.html')

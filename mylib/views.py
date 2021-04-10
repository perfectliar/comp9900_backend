from django.http import HttpResponse
from . import models
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


def show_all(request):
    data = json.loads(request.body)
    key = data['key']
    data = serializers.serialize('python', models.MyLib.objects.filter(lib_user_id=key))
    count = len(data)
    items = []
    for i in range(count):
        items.append(data[i]['fields'])
    print(type(items))
    res = {
        'data': items,
        'success': True,
        'message': 'Got data.',
    }

    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')

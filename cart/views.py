from django.http import HttpResponse
from . import models
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

def show_all(request):
    data = json.loads(request.body)
    key = data['key']
    data = serializers.serialize('python', models.Cart.objects.filter(cart_user_id=key))
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

def add(request):
    data = json.loads(request.body)
    # cart_user_id = data['cart_user_id']
    # cart_goods_id = data['cart_goods_id']

    models.Cart.objects.get_or_create(**data)
    res = {
        'success': True,
        'message': 'Already add to your cart.',
    }

    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')


def remove(request):
    data = json.loads(request.body)
    cart_user_id = data['cart_user_id']
    cart_goods_id = data['cart_goods_id']
    item = models.Cart.objects.get(cart_user_id=cart_user_id, cart_goods_id=cart_goods_id)
    item.delete()
    res = {
        'success': True,
        'message': 'Already remove from your cart.',
    }
    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')


def clear(request):
    data = json.loads(request.body)
    key = data['key']
    item = models.Cart.objects.get(cart_user_id=key)
    item.delete()
    res = {
        'success': True,
        'message': 'Already clear from your cart.',
    }
    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')

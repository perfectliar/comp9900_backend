from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


def item_list(request):
    data = serializers.serialize('python', models.GoodsInfo.objects.all())
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


def add_item(request):
    data = json.loads(request.body)
    item_info = {'item_name': data['name'],
                 'item_price': data['price'],
                 'item_des': data['description']
                 }
    models.GoodsInfo.objects.create(**item_info)
    book_cate = serializers.serialize('python', models.Category.objects.filter(cag_name=data['category']))

    res = {
        'success': True,
        'message': 'Add a book successfully.',
    }
    return HttpResponse(json.dumps(res), content_type='application/json')


def item_detail(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    item_info = serializers.serialize('python', models.GoodsInfo.objects.filter(id=item_id))
    cate_info = serializers.serialize('python', models.GoodsCategory.objects.filter(good_id=item_id))
    categories = []
    if cate_info:
        cate_id = []
        for index in range(len(cate_info)):
            cate_id.append(cate_info[index]['fields']['cate_id'])
        cate_name = serializers.serialize('python', models.Category.objects.filter(id=cate_id))
        if cate_name:
            for index in range(len(cate_name)):
                categories.append(cate_name[index]['fields']['cag_name'])
#  Mark
    if categories:
        res = {
            'data': item_info,
            'cate': categories,
            'success': True,
            'message': 'These are book details.',
        }
    else:
        res = {
            'data': item_info,
            'cate': None,
            'success': True,
            'message': 'These are book details.',
        }
    return HttpResponse(json.dumps(res), content_type='application/json')


def all_cate():

    cate_info = serializers.serialize('python', models.Category.objects.all())
    cate_list = {}
    if cate_info:
        for index in range(len(cate_info)):
            cate_list[cate_info[index]['fields']['cag_name']] = cate_info[index]['fields']['id']

    res = {
        'category': cate_list,
        'success': True,
        'message': 'Show all categories.',
    }

    return HttpResponse(json.dumps(res), content_type='application/json')
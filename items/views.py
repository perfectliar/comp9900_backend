from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


def item_list(request):
    data = serializers.serialize('python', models.ItemInfo.objects.all())
    count = len(data)
    items = []
    item_info = {}
    for i in range(count):
        item_info = data[i]['fields']
        item_info['item_key'] = data[i]['pk']
        items.append(item_info)
        print('\n')

    res = {
        'data': items,
        'success': True,
        'message': 'Got data.',
    }

    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')


def add_item(request):
    data = json.loads(request.body)
    print(data)
    item_info = {'item_name': data['name'],
                 'item_price': data['price'],
                 'item_des': data['description']
                 }
    models.ItemInfo.objects.get_or_create(**item_info)
    new_item = serializers.serialize('python', models.ItemInfo.objects.filter(**item_info))

    cate_list = serializers.serialize('python', models.Category.objects.filter(cag_name__in=data['category']))
    for index in range(len(cate_list)):
        print(cate_list[index]['pk'])
        models.ItemCategory.objects.get_or_create(item_id_id=new_item[0]['pk'], cate_id_id=cate_list[index]['pk'])

    author_res = serializers.serialize('python', models.Author.objects.filter(author_name__in=data['author']))
    author_list = []
    for index in range(len(author_res)):
        author_list.append(author_res[index]['fields']['author_name'])
    print(set(data['author']))
    print(set(author_list))
    new_author = list(set(data['author']) - set(author_list))
    if new_author:
        for index in range(len(new_author)):
            models.Author.objects.create(author_name=new_author[index])

    author_list = serializers.serialize('python', models.Author.objects.filter(author_name__in=data['author']))
    for index in range(len(author_list)):
        print(author_list[index]['pk'])
        models.ItemAuthor.objects.get_or_create(item_id_id=new_item[0]['pk'], author_id_id=author_list[index]['pk'])

    res = {
        'success': True,
        'message': 'Add a book successfully.',
    }

    return HttpResponse(json.dumps(res), content_type='application/json')


def item_detail(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    item_info = serializers.serialize('python', models.ItemInfo.objects.filter(id=item_id))
    cate_info = serializers.serialize('python', models.ItemCategory.objects.filter(good_id=item_id))
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


def all_cate(request):
    cate_info = serializers.serialize('python', models.Category.objects.all())
    cate_list = {}
    if cate_info:
        for index in range(len(cate_info)):
            cate_list[cate_info[index]['fields']['cag_name']] = cate_info[index]['pk']

    res = {
        'category': cate_list,
        'success': True,
        'message': 'Show all categories.',
    }

    return HttpResponse(json.dumps(res), content_type='application/json')

def search_item(request):
    data = json.loads(request.body)
    search_input = data['search']
    search_result = serializers.serialize('python', models.ItemInfo.objects.filter(item_name__contains=search_input))

    # The code below is same as item_list
    count = len(search_result)
    items = []
    item_info = {}
    for i in range(count):
        item_info = search_result[i]['fields']
        item_info['item_key'] = search_result[i]['pk']
        items.append(item_info)
        print('\n')

    res = {
        'data': items,
        'success': True,
        'message': 'Got data.',
    }

    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')

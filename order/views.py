from django.http import HttpResponse
from . import models
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from items import models as item_models


def show_all(request):
    # data = json.loads(request.body)
    # key = data['key']
    # data = serializers.serialize('python', models.MyOrder.filter(lib_user_id=key))
    data = serializers.serialize('python', models.MyOrder.exclude(total_price=-1))
    order_list = {}
    if data:
        for index in range(len(data)):
            order_id = data[index]['fields']['id']
            order_items = serializers.serialize('python', models.OrderItems.filter(order_id=order_id))
            if order_items:
                item_list = []
                price_count = 0
                for i in range(len(order_items)):
                    info = {}
                    item_info = serializers.serialize('python', item_models.GoodsInfo.filter(
                        id=order_items[i]['fields']['order_item_id']))
                    info['name'] = item_info[0]['fields']['goods_name']
                    info['price'] = item_info[0]['fields']['goods_price']
                    price_count += info['price']
                    item_list.append(info)
                order_list[index] = {}
                order_list[index]['item_list'] = item_list.copy()
                order_list[index]['total_price'] = price_count
                order_list[index]['order_time'] = data[index]['fields']['order_time']
    res = {
        'order_list': order_list,
        'success': True,
        'message': 'Got data.',
    }
    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')

'''
order_list = {1: {'item_list': [],
                  'total_price': ...,
                  'order_time': ...
                  },
              2: {'item_list': [],
                  'total_price': ...,
                  'order_time': ...
                  },
              3: {'item_list': [],
                  'total_price': ...,
                  'order_time': ...
                  },
              }

order_list[1]['item_list'] = [{'name': 'Book A', 'price': 15},
                              {'name': 'Book B', 'price': 25},
                              {'name': 'Book C', 'price': 35}]
order_list[1]['total_price'] = 75   # 15 + 25 + 35
order_list[1]['order_time'] = '2021-04-11  12:23:53'
'''
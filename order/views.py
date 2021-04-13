from django.http import HttpResponse
from . import models
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from items import models as item_models
from user import models as user_models

def show_all(request):
    # data = json.loads(request.body)
    # key = data['key']
    # data = serializers.serialize('python', models.MyOrder.filter(lib_user_id=key))
    data = serializers.serialize('python', models.MyOrder.objects.exclude(total_price=-1))
    order_list = []
    if data:
        for index in range(len(data)):
            order_id = data[index]['pk']
            order_items = serializers.serialize('python', models.OrderItems.objects.filter(order_id=order_id))
            if order_items:
                item_list = []
                price_count = 0
                for i in range(len(order_items)):
                    info = {}
                    item_info = serializers.serialize('python', item_models.ItemInfo.objects.filter(
                        id=order_items[i]['fields']['order_item_id']))
                    info['item_id'] = item_info[0]['pk']
                    info['name'] = item_info[0]['fields']['item_name']
                    info['price'] = item_info[0]['fields']['item_price']
                    price_count += info['price']
                    item_list.append(info)

                user_id = data[index]['fields']['order_user_id']
                user_info = serializers.serialize('python', user_models.Myuser.objects.filter(id=user_id))

                order_time = data[index]['fields']['order_time']
                print(order_time)
                order_time = order_time.strftime('%Y-%m-%d %H:%M:%S')
                order_info = {'item_list': item_list.copy(),
                              'total_price': price_count,
                              'order_time': order_time,
                              'order_status': data[index]['fields']['order_status'],
                              'order_id': data[index]['pk'],
                              'user_id': user_id,
                              'user_name': user_info[0]['fields']['username']}
                order_list.append(order_info)

    res = {
        'order_list': order_list,
        'success': True,
        'message': 'Got data.',
    }
    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')


'''
order_list = {1: {'item_list': [],
                  'total_price': ...,
                  'order_time': ...,
                  'order_status': ...
                  },
              2: {'item_list': [],
                  'total_price': ...,
                  'order_time': ...,
                  'order_status': ...
                  },
              3: {'item_list': [],
                  'total_price': ...,
                  'order_time': ...,
                  'order_status': ...
                  },
              }

order_list[1]['item_list'] = [{'name': 'Book A', 'price': 15},
                              {'name': 'Book B', 'price': 25},
                              {'name': 'Book C', 'price': 35}]
order_list[1]['total_price'] = 75  # 15 + 25 + 35
order_list[1]['order_time'] = '2021-04-11  12:23:53'
order_list[1]['order_status'] = 'Waiting for payment'
'''

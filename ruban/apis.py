import json
from rest_framework.response import Response
from . import models
from rest_framework.decorators import api_view


@api_view(['POST'])
def login(request):
    # import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if data["username"] == "ruban" and data["password"] == "ruban123":
            message = {"message": "success", "status": 1}
        else:
            message = {"message": "Enter valid username", "status": 0}
        return Response(message)
    else:
        return Response({'message': 'wrong method', "status": 0})


@api_view(['GET'])
def product_list(request):
    products = models.Product.objects.all()
    product_list = []
    for product in products:
        product_dict = {}
        product_dict.update({"product_code": product.product_code or ''})
        product_dict.update({"product_name": product.product_name or ''})
        product_dict.update({"product_price": product.product_price or ''})
        product_dict.update({"product_quantity": product.product_quantity or ''})
        product_dict.update({"product_img_url": product.product_img_url or ''})
        product_list.append(product_dict)
    if product_list:
        data = {"product_list": product_list,
                "status": 1}
    else:
        data = {"data": "No products available",
                "status": 0}
    return Response(data)


@api_view(['POST'])
def bid(request):
    product = json.loads(request.body.decode('utf-8'))
    data = {}
    try:
        id = models.Product.objects.get(product_code=product["product_code"])
        percent = round(id.bid_value/100 * float(id.product_price))
        old_price = id.product_price
        id.product_price = (float(id.product_price) + percent)
        id.save()
        data = {"message": "Product price has increased by {} % and old price was {} ".
            format(id.bid_value, old_price), "status": 1,
                "updated_price": id.product_price}
    except models.Product.DoesNotExist:
        data = {"message": "Product is not available", "status": 0}
    return Response(data)


@api_view(['POST'])
def place_order(request):
    product = json.loads(request.body.decode('utf-8'))
    try:
        id = models.Product.objects.get(product_code=product["product_code"])
        if int(id.product_quantity) > 0:
            id.product_quantity = int(id.product_quantity) - 1
            id.save()
            message = {"message": "Success", "status": 1}
        else:
            message = {"message": "Product stock is not available", "status": 0}
    except models.Product.DoesNotExist:
        message = {"message": "No Product", "status": 0}
    return Response(message)
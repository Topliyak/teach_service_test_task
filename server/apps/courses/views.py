from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .services.product_lessons import get_product_lessons
from .services.products_lessons import get_products_lessons
from .services.all_products_statistic import get_all_products_statistic


@api_view(['GET'])
def product_lessons(request, product_id: int):
    try:
        lessons = get_product_lessons(request.user, product_id)
    except PermissionError:
        return Response(status=403)
    
    return Response(lessons)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products_lessons(request):
    lessons = get_products_lessons(request.user)
    
    return Response(lessons)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def all_products_statistic(request):
    statistic = get_all_products_statistic()

    return Response(statistic)

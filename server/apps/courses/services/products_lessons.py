from django.contrib.auth.models import User
from django.db.models import F
from ..models import Product, ProductPurchase


def get_products_lessons(user: User):
    lessons_queryset = ProductPurchase.objects.filter(buyer=user)\
                                                .select_related('product')\
                                                .prefetch_related('lessoninproduct_set')\
                                                .prefetch_related('lessoninproduct__lesson')\
                                                .prefetch_related('lesson__lessonlearning_set')\
                                                .select_related('lessonlearning__status')\
                                                .filter(product__lessons__lessonlearning__student=user)\
                                                .annotate(
                                                    lesson_id=F('product__lessons__pk'),
                                                    lesson_order=F('product__lessoninproduct__lesson_order'),
                                                    duration_sec=F('product__lessons__duration_sec'),
                                                    watched_sec=F('product__lessons__lessonlearning__watched_sec'),
                                                    status=F('product__lessons__lessonlearning__status__name'),
                                                )\
                                                .order_by('product_id', 'lesson_order')\
                                                .values(
                                                    'product_id',
                                                    'lesson_id',
                                                    'lesson_order',
                                                    'duration_sec',
                                                    'watched_sec',
                                                    'status'
                                                )

    return lessons_queryset

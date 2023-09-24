from django.contrib.auth.models import User
from django.db.models import F, Q, Max

from ..models import Product, ProductPurchase


def get_product_lessons(user: User, product_id: int):
    product = Product.objects.get(pk=product_id)

    if has_permission(product, user) is False:
        raise PermissionError()

    lessons_queryset = product.lessons\
                                    .prefetch_related(
                                        'lessonlearning_set',
                                        'learningsession_set')\
                                    .filter(
                                        Q(learningsession__student=user) | Q(learningsession__isnull=True),
                                        lessonlearning__student=user)\
                                    .order_by('lessoninproduct__lesson_order')\
                                    .annotate(
                                        lesson_id=F('id'),
                                        watched_sec=F('lessonlearning__watched_sec'),
                                        status=F('lessonlearning__status__name'),
                                        last_watching_at=Max('learningsession__started_at')
                                    )\
                                    .values(
                                        'lesson_id',
                                        'title',
                                        'watched_sec',
                                        'duration_sec',
                                        'status',
                                        'last_watching_at'
                                    )

    return lessons_queryset


def has_permission(product: Product, user: User):
    if user.is_authenticated is False:
        return False
    
    if user.is_staff:
        return True

    if product.owner == user:
        return True

    product_buyers = ProductPurchase.objects.filter(product=product)

    return user in product_buyers

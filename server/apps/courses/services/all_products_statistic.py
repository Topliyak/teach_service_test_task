from ..models import Product
from django.contrib.auth.models import User
from django.db.models import Count, Sum, F, Q


def get_all_products_statistic():
    stats = {
        'watching_stats': get_all_products_watching_stats(),
        'purchase_stats': get_all_products_purchasing_stats(),
    }

    return stats


def get_all_products_watching_stats():
    products_and_watch_info = (
        Product.objects.all()\
            .prefetch_related('productpurchase_set')\
            .select_related('productpurchase__buyer')\
            .prefetch_related('lessons')\
            .prefetch_related('lesson__lessonlearning_set')\
            .filter(
                lessons__lessonlearning__student_id=F('productpurchase__buyer_id'),
            )\
            .annotate(
                product_id=F('id'),
                watched_lessons_count=Count(
                    'lessons__lessonlearning', 
                    filter=Q(lessons__lessonlearning__status_id=2)
                ),
                total_watched_sec=Sum('lessons__lessonlearning__watched_sec')
            )\
            .values(
                'product_id',
                'watched_lessons_count',
                'total_watched_sec'
            )
    )

    return products_and_watch_info


def get_all_products_purchasing_stats():
    users_count = User.objects.count()
    
    purchase_stat = (
        Product.objects.all()\
            .prefetch_related('productpurchase_set')\
            .annotate(
                product_id=F('id'),
                purchases_count=Count('productpurchase'),
                purchase_percent=F('purchases_count') * 100.0 / users_count
            )\
            .values(
                'product_id',
                'purchases_count',
                'purchase_percent'
            )
    )

    return purchase_stat

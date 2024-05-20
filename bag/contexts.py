from django.shortcuts import get_object_or_404
from gemstones.models import Gemstone


def bag_contents(request):

    bag_items = []
    total = 0
    gemstone_count = 0
    bag = request.session.get('bag', {})

    for item_id in bag.keys():
        gemstone = get_object_or_404(Gemstone, pk=item_id)
        item_total = gemstone.price
        total += item_total
        gemstone_count += 1
        bag_items.append({
            'item_id': item_id,
            'gemstone': gemstone,
            'item_total': item_total,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'gemstone_count': gemstone_count,
        'grand_total': grand_total,
    }

    return context

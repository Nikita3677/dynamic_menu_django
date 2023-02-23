from menu.models import SubCategory


def menu(request):
    sub_categorys = SubCategory.objects.select_related('category').all()
    categorys = []
    for sub_category in sub_categorys:
        categorys.append(sub_category.category)
    categorys = set(categorys)
    context = {
        'sub_categorys': sub_categorys,
        'categorys': categorys
    }
    return (context)
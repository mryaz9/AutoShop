
from tgc.models import Categories

menu = [{'title': "О сайте"},
        {'title': "Обратная связь"},
        ]


class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Categories.objects.all()

        user_menu = menu.copy()

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


from django.shortcuts import render
from django.contrib.messages import error, success, info, warning
from django.http.response import HttpResponse


from .models import Filter
from .form import FilterForm
from .settings import lorem
from .utils import form_handler, create_uu_slug



def main_view(request):
    ctx = {}

    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            slug = data['slug']
            qs = Filter.objects.filter(
                key_word = data['key_word'],
                content = data['content'],
                case = data['case'],
                search_type = data['search_type'],
                search_behavior = data['search_behavior'],
                num_keys = data['num_keys'],
                slug = slug
            )

            if qs.exists():
                warning(request, 'Task already accomplished.')
                return HttpResponse(status=204)

            if form_handler(data):
                content, matches_count = form_handler(data)
                ctx.__setitem__('content_matches', content)
                ctx.__setitem__('matches_count', matches_count)

                qs = Filter.objects.filter(slug=slug)
                if qs.exists():
                    qs.delete()

                instance = form.save(commit=False)
                instance.slug = slug
                form.save()

                success(request, 'Task accomplished.')
            else:
                info(request, 'Nothing located yet.')

        else:
            error(request, 'Invalid form data.')

    else:
        slug_form = create_uu_slug()
        form = FilterForm(initial={'key_word':'lorem', 'content': lorem, 'slug': slug_form})

    ctx.__setitem__('form', form)
    template = 'main/main.html'
    if request.htmx:
        template = 'main/form/main-form.html'
    return render(request, template, ctx)

def info_view(request):
    ctx = {}
    template = 'main/info.html'
    if request.htmx:
        return
    return render(request, template, ctx)


def contact_view(request):
    ctx = {}
    template = 'main/contact.html'
    if request.htmx:
        return
    return render(request, template, ctx)

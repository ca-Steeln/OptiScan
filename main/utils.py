
from django.utils.safestring import mark_safe
from .settings import repl, DEFAULT_SEARCH_TYPE, DEFAULT_SEARCH_BEHAVIOR

from re import compile, escape, IGNORECASE, MULTILINE
from itertools import islice
from string import ascii_lowercase, ascii_uppercase, digits,punctuation
from random import shuffle, randint
from uuid import uuid4


def form_handler(data:dict = {}):

    pattern = escape(data.get('key_word'))
    content = data.get('content')
    case = data.get('case')
    search_type = data.get('search_type', DEFAULT_SEARCH_TYPE)
    search_behavior = data.get('search_behavior', DEFAULT_SEARCH_BEHAVIOR)
    num_keys = int(data.get('num_keys')) if data.get('num_keys') is not None else 0
    behaviors = {
        'full_match': fr'\b{pattern}\b',
        'start_match': fr'\b{pattern}',
        'end_match': fr'{pattern}\b',
            # beta
        'all_match': pattern,
    }

    flags = {
        'case': IGNORECASE if not case else 0
    }
    compile_pattern = compile(behaviors[search_behavior], flags['case'])

    if compile_pattern.search(content):
        types = {
            'search_all': compile_pattern.findall(content),
            'search_first': [compile_pattern.search(content).group()],
            'custom_search': list(islice(compile_pattern.findall(content), num_keys)),
                # beta
            'search_last': '',
        }
        search_resualt = types.get(search_type)
        matches_count = len(search_resualt)
        if search_resualt:
            content_matches = add_span_tags(compile_pattern, content, matches_count)
            return mark_safe(content_matches), matches_count
    return

def add_span_tags(pattern=None, content:str='', count:int = 0) -> str:
    return pattern.sub(repl , content, count)


def create_uu_slug(characters_number : int = randint(8, 12)) -> str:
    s1 = list(ascii_lowercase)
    s2 = list(ascii_uppercase)
    s4 = list(str(uuid4()).split('-'))

    shuffle(s1)
    shuffle(s2)
    shuffle(s4)

    slug = []

    for i in range(round(characters_number * (60/100))):
        slug.append(s1[i])
        slug.append(s2[i])

    for i in range(round(characters_number * (40/100))):
        slug.append(s4[i])

    shuffle(slug)
    slug = "".join(slug)
    return slug


def slugify_instance(instance, save=False, new_slug=None):
    slug = create_uu_slug()
    klass = instance.__class__
    qs = klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = create_uu_slug()
        return slugify_instance(instance, save, slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance

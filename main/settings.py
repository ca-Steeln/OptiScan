

# search type-------- /

DEFAULT_SEARCH_TYPE = 'search_all'

SEARCH_TYPE_CHOICES = [
    ('search_all', 'search for all'),
    ('search_first', 'search for first'),
    ('search_last', 'search for last'),
    ('custom_search', 'custom search'),
]

# random Lorem text
lorem = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Lorem Deserunt Lorem provident lorem tenetur molestias ipsam, lorem atque Lorem voluptatum Lorem voluptates Lorem totam, obcaecati similique, veniam lorem repellat lorem repellendus Lorem facilis lorem itaque lorem ad fuga ipsa quisquam Lorem eum dolor"

# repl span
repl_regex = '\g<0>'
repl_span_class = 'match'
repl = f'<span class="{repl_span_class}">{repl_regex}</span>'

# Filter Behavior -------------------

DEFAULT_SEARCH_BEHAVIOR = 'full_match'

SEARCH_BEHAVIOR_CHOICES = [
    ('full_match', 'Full Match'),
    ('start_match', 'Start Match'),
    ('end_match', 'End Match'),
    ('all_match', 'All Match')
]
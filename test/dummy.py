text = 'He and me went too the stor.'
output = "He and I went to the store."

api_response = [
    {
        'context': {
            'length': 2,
            'offset': 7,
            'text': 'He and me went too the stor.'
        },
        'length': 2,
        'message': 'Did you mean “I”?',
        'offset': 7,
        'replacements': [{'value': 'I'}],
    },
    {
        'context': {'length': 7,
                'offset': 15,
                'text': 'He and me went too the stor.'},
        'length': 7,
        'message': 'Did you mean “to the”?',
        'offset': 15,
        'replacements': [{'value': 'to the'}],
    },
    {
        'context': {
            'length': 4,
            'offset': 23,
            'text': 'He and me went too the stor.'
        },
        'length': 4,
        'message': 'Possible spelling mistake found.',
        'offset': 23,
        'replacements': [{'value': 'story'},
                        {'value': 'stop'},
                        {'value': 'store'},
                        {'value': 'storm'}]
    }
]

prompts = [
"""
He and me went too the stor.
       ^^
Did you mean “I”?
1: I
0: (Skip)
""",
"""
He and me went too the stor.
               ^^^^^^^
Did you mean “to the”?
1: to the
0: (Skip)
""",
"""
He and me went too the stor.
                       ^^^^
Possible spelling mistake found.
1: story
2: stop
3: store
4: storm
0: (Skip)
"""
]


def api_query(text):
    return api_response


def fake_input(vals):
    i = iter(vals)

    def input(_):
        return next(i)

    return input

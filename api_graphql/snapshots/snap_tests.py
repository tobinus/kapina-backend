# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_post_by_slug 1'] = {
    'data': {
        'post': {
            'categories': [
                {
                    'backgroundColor': '#ECB61C',
                    'name': 'Radio',
                    'textColor': '#000000'
                }
            ],
            'content': '<p><b>Her</b> har vi teksten!</p>',
            'createdBy': {
                'fullName': 'Peder Ås'
            },
            'episodes': [
                {
                    'id': 1,
                    'lead': 'Dette er en episode',
                    'title': 'Program1 23.02.2018'
                }
            ],
            'id': 1,
            'publishAt': '2018-02-23 21:31:29+00:00',
            'show': None,
            'title': 'Den første artikkelen'
        }
    }
}

snapshots['test_frontpage 1'] = {
    'data': {
        'frontPagePosts': [
            {
                'categories': [
                    {
                        'backgroundColor': '#ECB61C',
                        'name': 'Radio',
                        'textColor': '#000000'
                    }
                ],
                'croppedImages': {
                    'large': '/media/cache/bf/0c/bf0c64d01f8854de77f44e8995bb6263.jpg',
                    'medium': '/media/cache/b3/9c/b39c21c911d5cbfe60192fe818985a7e.jpg',
                    'small': '/media/cache/8f/11/8f11ece1c53c8e55aadaa2cd700edcda.jpg'
                },
                'id': 2,
                'lead': 'Enda en ingress',
                'publishAt': '2018-02-23 21:32:30+00:00',
                'slug': 'den-andre-artikkelen',
                'title': 'Den andre artikkelen'
            },
            {
                'categories': [
                    {
                        'backgroundColor': '#ECB61C',
                        'name': 'Radio',
                        'textColor': '#000000'
                    }
                ],
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg'
                },
                'id': 1,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:31:29+00:00',
                'slug': 'den-forste-artikkelen',
                'title': 'Den første artikkelen'
            }
        ]
    }
}

snapshots['test_episode_by_id 1'] = {
    'data': {
        'episode': {
            'id': 1,
            'show': {
                'episodes': [
                    {
                        'id': 1,
                        'onDemandUrl': 'http://example.com/lyd.mp3',
                        'title': 'Program1 23.02.2018'
                    }
                ],
                'name': 'Program1'
            }
        }
    }
}

snapshots['test_show_by_slug 1'] = {
    'data': {
        'show': {
            'archived': False,
            'content': '<p>Program2 lenger beskrivelse!</p>',
            'episodes': [
                {
                    'id': 2,
                    'lead': 'Beskrivelse av episode2',
                    'publishAt': '2018-02-23 21:30:51+00:00',
                    'title': 'Episode2'
                }
            ],
            'id': 2,
            'image': '/media/uploads/images/300x300_9U7yu4U.png',
            'lead': 'Program2 beskrivelse',
            'name': 'Program2',
            'posts': [
                {
                    'createdBy': {
                        'fullName': 'Peder Ås'
                    },
                    'croppedImages': {
                        'large': '/media/cache/bf/0c/bf0c64d01f8854de77f44e8995bb6263.jpg',
                        'medium': '/media/cache/b3/9c/b39c21c911d5cbfe60192fe818985a7e.jpg',
                        'small': '/media/cache/8f/11/8f11ece1c53c8e55aadaa2cd700edcda.jpg'
                    },
                    'id': 2,
                    'lead': 'Enda en ingress',
                    'publishAt': '2018-02-23 21:32:30+00:00',
                    'slug': 'den-andre-artikkelen',
                    'title': 'Den andre artikkelen'
                }
            ]
        }
    }
}

snapshots['test_all_shows 1'] = {
    'data': {
        'allShows': [
            {
                'archived': False,
                'id': 1,
                'image': '/media/uploads/images/300x300.png',
                'lead': 'Program1 beskrivelse',
                'name': 'Program1',
                'slug': 'program1'
            },
            {
                'archived': False,
                'id': 2,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program2 beskrivelse',
                'name': 'Program2',
                'slug': 'program2'
            }
        ]
    }
}

snapshots['test_url_all_shows 1'] = b'{"data":{"allShows":[{"id":1},{"id":2}]}}'

snapshots['test_settings 1'] = {
    'data': {
        'settings': {
            'about': '<p>About text</p>'
        }
    }
}

snapshots['test_all_categories 1'] = {
    'data': {
        'allCategories': [
            {
                'backgroundColor': '#ECB61C',
                'id': 1,
                'name': 'Radio',
                'textColor': '#000000'
            }
        ]
    }
}

snapshots['test_category_by_id 1'] = {
    'data': {
        'category': {
            'backgroundColor': '#ECB61C',
            'id': 1,
            'name': 'Radio',
            'textColor': '#000000'
        }
    }
}

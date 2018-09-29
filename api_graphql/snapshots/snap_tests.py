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

snapshots['test_settings 1'] = {
    'data': {
        'settings': {
            'about': '<p>About text</p>'
        }
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
                    'publishAt': '2018-02-23 21:30:30+00:00',
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

snapshots['test_url_all_shows 1'] = b'{"data":{"allShows":[{"id":1},{"id":2}]}}'

snapshots['test_paginated_posts 1'] = {
    'data': {
        'paginatedPosts': {
            'hasNext': False,
            'hasPrev': False,
            'pages': 1,
            'posts': [
                {
                    'categories': [
                        {
                            'backgroundColor': '#ECB61C',
                            'name': 'Radio',
                            'textColor': '#000000'
                        }
                    ],
                    'id': 1,
                    'lead': 'Ingressen her',
                    'publishAt': '2018-02-23 21:31:29+00:00',
                    'slug': 'den-forste-artikkelen',
                    'title': 'Den første artikkelen'
                },
                {
                    'categories': [
                        {
                            'backgroundColor': '#ECB61C',
                            'name': 'Radio',
                            'textColor': '#000000'
                        }
                    ],
                    'id': 3,
                    'lead': 'Ingressen her',
                    'publishAt': '2018-02-23 21:29:29+00:00',
                    'slug': 'den-3rd-artikkelen',
                    'title': 'Den tredje artikkelen'
                },
                {
                    'categories': [
                        {
                            'backgroundColor': '#ECB61C',
                            'name': 'Radio',
                            'textColor': '#000000'
                        }
                    ],
                    'id': 7,
                    'lead': 'Ingressen her',
                    'publishAt': '2018-02-23 21:25:29+00:00',
                    'slug': 'den-7th-artikkelen',
                    'title': 'Den syvende artikkelen'
                }
            ]
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
                'publishAt': '2018-02-23 21:30:30+00:00',
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
                'id': 3,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:29:29+00:00',
                'slug': 'den-3rd-artikkelen',
                'title': 'Den tredje artikkelen'
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
                'id': 4,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:28:29+00:00',
                'slug': 'den-4th-artikkelen',
                'title': 'Den fjerde artikkelen'
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
                'id': 5,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:27:29+00:00',
                'slug': 'den-5th-artikkelen',
                'title': 'Den femte artikkelen'
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
                'id': 6,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:26:29+00:00',
                'slug': 'den-6th-artikkelen',
                'title': 'Den sjette artikkelen'
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
                'id': 7,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:25:29+00:00',
                'slug': 'den-7th-artikkelen',
                'title': 'Den syvende artikkelen'
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
                'id': 8,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:24:29+00:00',
                'slug': 'den-8th-artikkelen',
                'title': 'Den attende artikkelen'
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
                'id': 9,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:23:29+00:00',
                'slug': 'den-9th-artikkelen',
                'title': 'Den niende artikkelen'
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
                'id': 10,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:22:29+00:00',
                'slug': 'den-10th-artikkelen',
                'title': 'Den tiende artikkelen'
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
                'id': 11,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:21:29+00:00',
                'slug': 'den-11th-artikkelen',
                'title': 'Den ellevte artikkelen'
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
                'id': 12,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:20:29+00:00',
                'slug': 'den-12th-artikkelen',
                'title': 'Den tolvte artikkelen'
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
                'id': 13,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:19:29+00:00',
                'slug': 'den-13th-artikkelen',
                'title': 'Den trettende artikkelen'
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
                'id': 14,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:18:29+00:00',
                'slug': 'den-14th-artikkelen',
                'title': 'Den fjortende artikkelen'
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
                'id': 15,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:17:29+00:00',
                'slug': 'den-15th-artikkelen',
                'title': 'Den femtende artikkelen'
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
                'id': 16,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:16:29+00:00',
                'slug': 'den-16th-artikkelen',
                'title': 'Den sekstende artikkelen'
            }
        ]
    }
}

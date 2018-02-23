from django.core.management import call_command
from graphene.test import Client
from api_graphql.schema import schema
import pytest


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'test_fixtures.json')


@pytest.mark.django_db
def test_frontpage(snapshot):
    client = Client(schema)

    executed = client.execute('''query {
        frontPagePosts {
            id,
            title,
            slug,
            croppedImages {
                large,
                medium,
                small
            },
            lead,
            publishAt,
            categories {
                name,
                textColor,
                backgroundColor
            }
        }
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_post_by_slug(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        post(slug:"den-forste-artikkelen") {
        id,
        title,
        content,
        publishAt,
        createdBy {
            fullName
        },
        show{
            name,
            slug
        },
        categories{
            name,
            textColor,
            backgroundColor
        },
        episodes {
            id,
            title,
            lead,
        }
        }
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_episode_by_id(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        episode(id:1) {
        id,
        show {
            name,
            episodes {
            id,
            title,
            onDemandUrl
            }
        }
        }
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_show_by_slug(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        show(slug:"program2") {
        id,
        name,
        image,
        content,
        lead,
        archived,
        episodes {
            id,
            title,
            lead,
            publishAt,
        },
        posts {
            id,
            title,
            slug,
            croppedImages {
            large,
            medium,
            small
            },
            publishAt,
            lead,
            createdBy {
            fullName
            }
        }
        }
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_shows(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allShows {
        id,
        name,
        image,
        lead,
        slug,
        archived
        }
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_url_all_shows(client, snapshot):
    response = client.get(
        '/graphql?query=query%20{%20allShows%20{%20id%20}%20}'
    )

    assert response.status_code == 200
    snapshot.assert_match(response.content)

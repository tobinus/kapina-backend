import graphene

from django.contrib.auth.models import User
from django.utils import timezone

from data_models.models import Post, Episode, Show, Category
from data_models.crop import CropImages


class CategoryType(graphene.ObjectType):
    """
    Category description
    """

    id = graphene.Int()
    name = graphene.String()
    text_color = graphene.String()
    background_color = graphene.String()


class PostType(graphene.ObjectType):
    """
    Post description
    """

    id = graphene.Int()
    title = graphene.String()
    slug = graphene.String()
    image = graphene.String()
    cropped_images = graphene.Field('CroppedImagesType')
    lead = graphene.String()
    content = graphene.String()
    categories = graphene.List('CategoryType')
    deleted = graphene.Boolean()
    episodes = graphene.List('EpisodeType')

    show = graphene.Field('ShowType')

    publish_at = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()
    created_by = graphene.Field('UserType')

    @staticmethod
    def resolve_show(post, args, info):
        return post.show

    @staticmethod
    def resolve_categories(post, args, info):
        return post.categories.all()

    @staticmethod
    def resolve_episodes(post, args, info):
        return post.episodes.all()

    @staticmethod
    def resolve_created_by(post, args, info):
        return post.created_by

    @staticmethod
    def resolve_cropped_images(post, args, info):
        return CropImages(post.image, post.cropping)


class ShowType(graphene.ObjectType):
    """
    Show description
    """

    id = graphene.Int()
    name = graphene.String()
    digas_show_id = graphene.Int()
    image = graphene.String()
    lead = graphene.String()
    content = graphene.String()
    categories = graphene.List('CategoryType')

    slug = graphene.String()
    archived = graphene.Boolean()

    created_at = graphene.String()
    updated_at = graphene.String()
    created_by = graphene.Field('UserType')

    episodes = graphene.List('EpisodeType')

    posts = graphene.List('PostType')

    @staticmethod
    def resolve_created_by(show, args, info):
        return show.created_by

    @staticmethod
    def resolve_categories(show, args, info):
        return show.categories.all()

    @staticmethod
    def resolve_episodes(show, args, info):
        return show.episodes \
            .order_by('-publish_at') \
            .filter(publish_at__lte=timezone.now())

    @staticmethod
    def resolve_posts(show, args, info):
        return show.posts.order_by('-created_at')

    @staticmethod
    def resolve_image(show, args, info):
        return show.image.url


class EpisodeType(graphene.ObjectType):
    """
    Episode description
    """

    id = graphene.Int()
    title = graphene.String()
    lead = graphene.String()
    digas_broadcast_id = graphene.Int()
    digas_show_id = graphene.Int()
    categories = graphene.List('CategoryType')

    show = graphene.Field('ShowType')

    created_at = graphene.String()
    updated_at = graphene.String()
    publish_at = graphene.String()
    created_by = graphene.Field('UserType')

    podcast_url = graphene.String()
    on_demand_url = graphene.String()

    @staticmethod
    def resolve_title(episode, args, info):
        if episode.use_title:
            return episode.title
        else:
            return '{} {}'.format(
                episode.show.name, episode.created_at.strftime('%d.%m.%Y')
            )

    @staticmethod
    def resolve_created_by(episode, args, info):
        return episode.created_by

    @staticmethod
    def resolve_categories(episode, args, info):
        return episode.categories.all()

    @staticmethod
    def resolve_show(episode, args, info):
        return episode.show


class UserType(graphene.ObjectType):
    """
    User description
    """

    id = graphene.Int()
    full_name = graphene.String()

    publications = graphene.List('PostType')

    @staticmethod
    def resolve_publications(user, args, info):
        return user.publications.order_by('-created_at')

    @staticmethod
    def resolve_full_name(user, args, info):
        return user.get_full_name()


class CroppedImagesType(graphene.ObjectType):
    """
    Cropped versions of an image
    """

    large = graphene.String()
    medium = graphene.String()
    small = graphene.String()
    thumbnail = graphene.String()


class Query(graphene.ObjectType):
    """
    Radio Revolt query description
    """
    name = 'Query'

    category = graphene.Field(
        CategoryType,
        id=graphene.Int()
    )

    all_categories = graphene.List(
        CategoryType
    )

    show = graphene.Field(
        ShowType,
        id=graphene.Int(),
        slug=graphene.String()
    )

    all_shows = graphene.List(
        ShowType
    )

    episode = graphene.Field(
        EpisodeType,
        id=graphene.Int()
    )

    all_episodes = graphene.List(
        EpisodeType
    )

    post = graphene.Field(
        PostType,
        id=graphene.Int(),
        slug=graphene.String()
    )

    all_posts = graphene.List(
        PostType
    )

    front_page_posts = graphene.List(
        PostType
    )

    user = graphene.Field(
        UserType,
        id=graphene.Int()
    )

    all_users = graphene.List(
        UserType
    )

    cropped_images = graphene.Field(CroppedImagesType)

    @staticmethod
    def resolve_category(root, args, info):
        id = args.get('id')
        return Category.objects.get(pk=id)

    @staticmethod
    def resolve_all_categories(root, args, info):
        return Category.objects.all()

    @staticmethod
    def resolve_show(root, args, info):
        id = args.get('id')
        slug = args.get('slug')
        if id:
            return Show.objects.get(pk=id)
        return Show.objects.filter(slug=slug)[0]

    @staticmethod
    def resolve_all_shows(root, args, info):
        return Show.objects.all()

    @staticmethod
    def resolve_episode(root, args, info):
        id = args.get('id')
        episode = Episode.objects.get(pk=id)
        if episode.publish_at >= timezone.now():
            raise Episode.DoesNotExist(
                'Episode matching query does not exist.'
                )
        else:
            return episode

    @staticmethod
    def resolve_all_episodes(root, args, info):
        return Episode.objects \
            .order_by('-publish_at') \
            .filter(publish_at__lte=timezone.now())

    @staticmethod
    def resolve_post(root, args, info):
        id = args.get('id')
        slug = args.get('slug')
        if id:
            return Post.objects.get(pk=id)
        return Post.objects.filter(slug=slug)[0]

    @staticmethod
    def resolve_all_posts(root, args, info):
        return Post.objects.order_by('-created_at')

    @staticmethod
    def resolve_front_page_posts(root, args, info):
        return Post.objects.order_by('-created_at')[:30]

    @staticmethod
    def resolve_all_users(root, args, info):
        return User.objects.all()

    @staticmethod
    def resolve_user(root, args, info):
        id = args.get('id')
        return User.objects.get(pk=id)


schema = graphene.Schema(name='Radio Revolt GraphQL Schema')
schema.query = Query

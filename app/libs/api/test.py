from werkzeug.datastructures import ImmutableMultiDict
from tests import BaseTestCase
from .. import api
from app.libs.errors import NotFound
import config


if not hasattr(config, 'DEFAULT_PAGE_SIZE'):
    config.DEFAULT_PAGE_SIZE = 20


def stub_serializer(resource, fields):
    return resource


def stub_url_for(**kwargs):
    kwargs = ['='.join([k, str(v)]) for k, v in kwargs.items()]
    return 'someurl?{0}'.format('&'.join(kwargs))


class StubRequest():
    def __init__(self, **kwargs):
        # Flask `request.args` has type of ImmutableMultiDict
        # Need to use that here so that request.args.getlist will work
        self.args = ImmutableMultiDict(kwargs)


class BaseQuerySet():
    def __init__(self, size):
        self.items = list(range(0, size))

    def skip(self, amount):
        self.items = self.items[amount:]
        return self

    def limit(self, amount):
        self.items = self.items[:amount]
        return self

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return (x for x in self.items)


class TestAPI(BaseTestCase):

    def test_format_single_document(self):
        request = StubRequest()
        response = api.format('resource', request, stub_serializer, 'api.user')
        self.assertTrue(response['data'] == 'resource')

    def test_error_not_found(self):
        error = NotFound
        response = api.error(error)
        self.assertTrue((
            response['type'] == 'NOT_FOUND',
            response['code'] == 404,
            response['message']
        ))

    def test_format_many_documents(self):
        request = StubRequest(page=2)
        document_count = config.DEFAULT_PAGE_SIZE * 3 + 1
        documents = BaseQuerySet(document_count)
        response = api.format(documents, request, stub_serializer, stub_url_for)
        self.assertTrue(len(response['data']) == config.DEFAULT_PAGE_SIZE)
        self.assertTrue(response['next_page'] == stub_url_for(page=3))
        self.assertTrue(response['prev_page'] == stub_url_for(page=1))
        self.assertTrue(response['page'] == 2)
        self.assertTrue(response['count'] == document_count)

    def test_get_users_custom_page_size(self):
        document_count = config.DEFAULT_PAGE_SIZE * 3 + 1
        page_size = config.DEFAULT_PAGE_SIZE - 5
        request = StubRequest(page=1, page_size=page_size)
        documents = BaseQuerySet(document_count)
        response = api.format(documents, request, stub_serializer, stub_url_for)
        self.assertTrue(len(response['data']) == page_size)
        self.assertTrue(response['prev_page'] is None)

    def test_get_users_last_page(self):
        request = StubRequest(page=3)
        document_count = config.DEFAULT_PAGE_SIZE * 2 + 1  # 3 pages
        documents = BaseQuerySet(document_count)
        response = api.format(documents, request, stub_serializer, stub_url_for)
        self.assertTrue(response['next_page'] is None)

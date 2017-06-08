from nose.tools import *
import json
from xml.dom.minidom import parseString
from indeed import IndeedClient, IndeedClientException
from utils import Utils

class TestSearch:

    def setup(self):
        self.client = IndeedClient('8251007850639120')
        self.params = {
            'q' : "python",
            'l' : "austin",
            'userip' : "1.2.3.4",
            'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)",
        }
        self.utils = Utils()

    def teardown(self):
        self.client = None
        self.params = None

    @with_setup(setup, teardown)
    def test_search(self):
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict
        self.utils.output_to_file('sample',search_response )

    @with_setup(setup, teardown)
    def test_missing_one_required(self):
        del self.params['l']
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    @raises(IndeedClientException)
    def test_missing_both_required(self):
        del self.params['q']
        del self.params['l']
        search_esponse = self.client.search(**self.params)

    @with_setup(setup, teardown)
    @raises(IndeedClientException)
    def test_missing_userip(self):
        del self.params['userip']
        search_response = self.client.search(**self.params)

    @with_setup(setup, teardown)
    @raises(IndeedClientException)
    def test_missing_useragent(self):
        del self.params['useragent']
        search_response = self.client.search(**self.params)

    @with_setup(setup, teardown)
    def test_raw_json(self):
        self.params['raw'] = True
        search_response = self.client.search(**self.params)
        assert isinstance(search_response, basestring)
        assert type(json.loads(search_response)) is dict

    @with_setup(setup, teardown)
    def test_raw_xml_with_paramter(self):
        self.params['format'] = "xml"
        self.params['raw'] = True
        search_response = self.client.search(**self.params)
        assert isinstance(search_response, basestring)
        assert parseString(search_response)

    @with_setup(setup, teardown)
    def test_raw_xml_without_paramter(self):
        self.params['format'] = "xml"
        search_response = self.client.search(**self.params)
        assert isinstance(search_response, basestring)
        assert parseString(search_response)

    ''' Few Tests written by me '''
    @with_setup(setup, teardown)
    def test_search_extra(self):
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict
        assert len(self.utils.find_all_jobs_not_contains_job_parameter(search_response, 'city'
                                                                       , 'austin')) == 0
        assert len(self.utils.find_all_jobs_not_contains_job_parameter(search_response, 'country', 'US'))\
               == 0
        assert len(self.utils.find_all_jobs_not_contains_job_parameter(search_response, 'language', 'en')) \
               == 0
        assert self.utils.get_num_jobs(search_response) == 10

    @with_setup(setup, teardown)
    def test_sort(self):
        self.params['sort'] = "date"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    def test_start(self):
        self.params['start'] = "2"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    def test_limit(self):
        self.params['limit'] = "25"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict
        assert self.utils.get_num_jobs(search_response) == 25

    @with_setup(setup, teardown)
    def test_fromage(self):
        self.params['fromage'] = "2"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    def test_limit(self):
        self.params['limit'] = "25"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict
        assert self.utils.get_num_jobs(search_response) == 25

    @with_setup(setup, teardown)
    def test_highlight(self):
        self.params['highlight'] = "1"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    def test_duplicate(self):
        self.params['duplicate'] = "1"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    def test_co(self):
        self.params['co'] = "ca"
        self.params['l'] = "toronto"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    def test_invalid_limit(self):
        self.params['limit'] = '-100'
        search_response = self.client.search(**self.params)
        assert self.utils.get_num_jobs(search_response) == 0

    # trying a bunch of invalid parameters, I noticed that no error is thrown. Instead it seems to ignore. It this correct?
    # ie. negative fromage, string instead of ints and vs versa

    @with_setup(setup, teardown)
    def test_several_params(self):
        self.params['co'] = "ca"
        self.params['l'] = "toronto"
        self.params['duplicate'] = "1"
        self.params['highlight'] = "1"
        self.params['limit'] = "25"
        self.params['fromage'] = "10"
        self.params['start'] = "2"
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict
        assert self.utils.get_num_jobs(search_response) == 25
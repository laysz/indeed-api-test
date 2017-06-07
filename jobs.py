from nose.tools import *
import unittest
import json
from xml.dom.minidom import parseString
from indeed import IndeedClient, IndeedClientException
from utils import Utils

class TestJobs():


    def setup(self):
        self.utils = Utils()
        self.client = IndeedClient('8251007850639120')
        self.params = {
            'jobkeys' : ("7c398c74a8f22c72", "d7802e9ce3b4af7d"),
        }

    def teardown(self):
        self.client = None
        self.params = None

    @with_setup(setup, teardown)
    def test_jobs(self):
        jobs_response = self.client.jobs(**self.params)
        assert type(jobs_response) is dict
        print jobs_response
        self.utils.output_to_file('output', jobs_response)
        self.utils.open_with_subl('output')

        # self.utils.output_to_file('sample.json', str(j))
        # self.utils.open_with_subl('sample.json')

    @with_setup(setup, teardown)
    @raises(IndeedClientException)
    def test_missing_jobkeys(self):
        del self.params['jobkeys']
        jobs_response = self.client.jobs(**self.params)

    @with_setup(setup, teardown)
    def test_raw_json(self):
        self.params['raw'] = True
        jobs_response = self.client.jobs(**self.params)
        assert isinstance(jobs_response, basestring)
        assert type(json.loads(jobs_response)) is dict

    @with_setup(setup, teardown)
    def test_raw_xml_with_paramter(self):
        self.params['format'] = "xml"
        self.params['raw'] = True
        jobs_response = self.client.jobs(**self.params)
        assert isinstance(jobs_response, basestring)
        assert parseString(jobs_response)

    @with_setup(setup, teardown)
    def test_raw_xml_without_paramter(self):
        self.params['format'] = "xml"
        jobs_response = self.client.jobs(**self.params)
        assert isinstance(jobs_response, basestring)
        assert parseString(jobs_response)

    '''New test cases not included in GIT'''
    # @with_setup(setup, teardown)
    # def test_invalid_jobkey
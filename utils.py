from subprocess import call
import os
import pprint


class Utils (object):

    # write to file given name and the contents
    def output_to_file(self, name, contents):
        f = open(name, 'w')
        pprint.pprint(contents, f)
        f.close()

    def open_with_subl(self, name):
        os.system('subl ' + name)

    # return list of jobs that has value in paramter with results from search
    def find_all_jobs_not_contains_job_parameter(self, results, parameter, value):
        results = results['results']
        l = []
        for result in results:
            if value.lower() not in str(result[parameter]).lower():
                l.append(result)
        return l


    # return list of all the jobs that doesn't contain certain keyword
    def find_all_jobs_not_contain_keyword(self, results, keyword):
        results = results['results']
        l = []
        for result in results:
            if keyword.lower() not in str(result).lower():
                l.append(result)
        return l

    # gets the total number of results
    def get_num_jobs(self, results):
        results = results['results']
        return len(results)

    # don't see salary anywhere
    def find_jobs_within_pay_range(self):
        pass

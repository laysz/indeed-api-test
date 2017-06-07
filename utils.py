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

    def find_all_jobs_that_match_job_parameter(self):
        pass

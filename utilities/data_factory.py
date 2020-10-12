# Write a method to read json file. That method returned json object

import json

import config


class ReadFile:

    def json_reader(self, file_name):
        with open(config.project_root + '/' + file_name) as f:
            data = json.load(f)
            return data
    # we use return methods to use it for future data manipulations/ uses.
    # 19-22Lines are not neccessary and can be commented out and can be use for debugging


# #r = ReadFile()
# sample = r.json_reader("Testings.json")
# sample1 = r.json_reader("sample.json")
# print(sample, sample1)

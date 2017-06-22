import os
import time

class BaseFilter:
    def __init__(self, tree):
        self.tree = tree
        self.results = self.filter()

    def __call__(self):
        return self.results

class CDateFilter(BaseFilter):
    def __init__(self, tree, cdate):
        self.cdate = time.mktime(time.strptime(cdate, '%Y/%m/%d'))
        super().__init__(tree)

    def filter(self):
        for path, directories, files in self.tree:
            for file in files:
                ctime = os.stat(os.path.join(path, file)).st_ctime
                if ctime < self.cdate:
                    yield file

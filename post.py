import logging
logger = logging.getLogger(__file__)


class Post(object):

    def __init__(self, file_content):
        self.file_content = file_content

    @property
    def headers(self):
        try:
            pairs = self.file_content.split('---')[1].strip().split('\n')
            pairs = self._list_to_dict(pairs)
            return {k.strip(): v.strip() for k, v in pairs.iteritems()}
        except Exception:
            logger.error('unable to parse post header')

    @staticmethod
    def _list_to_dict(rlist):
        return dict(map(lambda s: s.split(':'), rlist))

    @property
    def content(self):
        return self.file_content.split('---')[2].strip()
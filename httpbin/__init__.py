import requests as r


class HttpBin(object):
    url = "http://httpbin.org"

    def __init__(self):
        pass

    def post_csv(self, filename: str):
        """ Create a new item from a CSV file """
        httpbin_url = '{}/post'.format(self.url)
        files = {'file': open(filename, 'r')}
        headers = {'Content-Type': 'text/csv'}
        return r.post(httpbin_url, files=files, headers=headers)

    def get(self):
        """ Get something -- no parameters """
        httpbin_url = '{}/get'.format(self.url)
        return r.get(httpbin_url)

    def delete(self):
        """
        Delete something
        This takes no parameters -- odd for a DELETE method
        """
        httpbin_url = '{}/delete'.format(self.url)
        return r.delete(httpbin_url)

    def patch(self):
        """
        Modify an existing item
        This takes no parameters -- odd for a PATCH method
        """
        httpbin_url = '{}/patch'.format(self.url)
        return r.patch(httpbin_url)

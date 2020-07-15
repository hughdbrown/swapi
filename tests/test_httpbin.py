import os

from httpbin import HttpBin


def test_get():
    result = HttpBin().get()
    assert result.status_code == 200
    data = result.json()
    assert data['args'] == {}
    assert data['headers']['Host'] == 'httpbin.org'
    assert data['headers']['Accept-Encoding'] == 'gzip, deflate'
    assert 'origin' in data
    assert data['url'] == "http://httpbin.org/get"


def test_post():
    csv_file = 'csv_test'
    with open(csv_file, 'w') as handle:
        handle.write('Date,Id,Num\n')
        handle.write('2020-07-15, 1, 42\n')
    result = HttpBin().post_csv(csv_file)
    assert result.status_code == 200
    os.remove(csv_file)


def test_patch():
    result = HttpBin().patch()
    assert result.status_code == 200


def test_delete():
    result = HttpBin().delete()
    assert result.status_code == 200


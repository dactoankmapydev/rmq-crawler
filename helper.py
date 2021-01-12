import pika, requests


def setup(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5673,
                                                                   credentials=pika.PlainCredentials(username='test',
                                                                                                     password='test')))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    return connection, channel


def scrape(url):
    proxies = {
        'http': 'http://127.0.0.1:3131',
        'https': 'http://127.0.0.1:3131',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers, proxies=proxies)
    return r.text

import time, os, urllib.request, shutil, datetime
from instabot import Bot


def clean():
    if os.path.exists('config'):
        try:
            shutil.rmtree('config')
        except OSError as e:
            print('Error: %s - %s.' % (e.filename, e.strerror))


num = 1
uriline = 1
def url_to_jpg(path, url):
    """
        args:
            -- path : where the file saves
            -- url : the url address of the picture
    """
    global num, uriline
    filename = 'image{}.jpg'.format(num)
    while filename in os.listdir('images/'):
        num += 1
        filename = 'image{}.jpg'.format(num)
    fullpath = '{}{}'.format(path, filename)
    try:
        urllib.request.urlretrieve(url, fullpath)
    except:
        print('Unable to download. Use a VPN or fix the uri (URL) in line {}'.format(uriline))
        pass
    else:
        print('{} saved !'.format(filename))
    uriline += 1


def download(file, path):
    with open(file) as f:
        for url in f.readlines():
            url_to_jpg(path, url.replace('\n', ''))


def upload(usr, pw, path):
    bot = Bot()
    bot.login(username=usr, password=pw)
    while True:
        for file in os.listdir(pics_path):
            print('uploading {}'.format(file))
            bot.upload_photo('{}{}'.format(path, file), caption='uploaded at {}:{} GMT'.format(datetime.datetime.now(datetime.timezone.utc).hour, datetime.datetime.now(datetime.timezone.utc).minute))
            print('-------------------------- file {} done ------------------------'.format(file))
        file = path + '*.REMOVE_ME'
        for a in os.listdir(path):
            if a.endswith('.REMOVE_ME'):
                os.remove(''.join([path,a]))
        seconds = 1
        loopTimes = 3
        for sleep in range(loopTimes):
            time.sleep(seconds)
            print(loopTimes - sleep, 'minutes left')
            file = os.listdir('images/')



pics_path = 'images/'
textFile = 'uris.txt'

clean()
# download(textFile, pics_path)


upload('USERNAME', 'PASSWORD', pics_path)



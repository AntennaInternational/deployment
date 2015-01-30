__author__ = 'brendan'
from fabric.api import cd, lcd, local

def download_redis():
    with lcd('/tmp'):
        local('curl -O http://download.redis.io/releases/redis-2.8.9.tar.gz')
        local('tar xzf redis-2.8.9.tar.gz')

def make_test_redis():
    with lcd('/tmp/redis*'):
        local('make')
        local('make test')
        local('make install')

def install_redis():
    with lcd('/tmp/redis*'):
        local('make install')

def install_redis_server():
    with lcd('/tmp/redis*/utils'):
        local('./install_server.sh')

def add_redis_to_startup():
    local('update-rc.d redis_6379 defaults')

def cleanup_redis():
    with lcd('/tmp'):
        local('rm -f -R redis*')


if __name__ == '__main__':
    download_redis()
    make_test_redis()
    install_redis()
    install_redis_server()
    add_redis_to_startup()
    cleanup_redis()
from nplatform.common.server import Server


def function1(server):
    server.LOGGER.debug('this is a debug message')


def function2(server: Server):
    server.LOGGER.warning('hello, world')

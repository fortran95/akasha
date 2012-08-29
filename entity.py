# -*- coding: utf-8 -*-

from account import byID_Protocol

class entity(object):
    def __init__(self,name):

        # To initialize, we need to supply a name, which is defined in config file.
        # The name does not relate to any specified account, but a group of accounts.
        # The user is actually talking with an entity, with program sending his messages
        # out via multiple accounts.

        self.name = name

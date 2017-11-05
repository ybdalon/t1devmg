# -*- coding: utf-8 -*-

handlers = []
sub_handlers = []

from handlers import user
from handlers import admin
from handlers import devlist
from handlers import index

            
handlers.extend(user.handlers)
handlers.extend(admin.handlers)
handlers.extend(devlist.handlers)
handlers.extend(index.handlers)

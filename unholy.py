#!/usr/bin/env python
# -*- coding: utf-8

# Copyright © 2018 Plotogandr
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

# - Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# - Neither the name of the Mumble Developers nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# `AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE FOUNDATION OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from mumo_module import MumoModule


class unholy(MumoModule):
    default_config = {'base64fixer': (
                                ('max_width', int, 100),
                                )
                      }

    def __init__(self, name, manager, configuration=None):
        MumoModule.__init__(self, name, manager, configuration)

    def connected(self):
        manager = self.manager()
        manager.subscribeServerCallbacks(self, manager.SERVERS_ALL)

#
# --- Server callback functions
#

    def userTextMessage(self, server, user, message, current=None):
        msg = None

        if message.text.startswith('!unholy'):
            msg += 'https://images-na.ssl-images-amazon.com/images/I/710VFY9wheL._SY606_.jpg'
            server.sendMessageChannel(user.channel, False, msg)

        def __getattr__(self, item):
            """Bypass method for getting rid of all the callbacks that are not
               handled by this module.

               :param item: item that is being queried for
               :return: an unused callable attribute that does not do anything
            """

        def unused_callback(*args, **kwargs):
            pass
        return unused_callback

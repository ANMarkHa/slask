# -*- coding: UTF-8 -*-
import os
import sys

from nose.tools import eq_

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(DIR, '../../limbo/plugins'))

from banner import on_message

def test_basic():
    ret = on_message({"text": u"!banner llimllib --font morse"}, None)
    eq_(ret, u'```.-.. .-.. .. -- .-.. .-.. .. -...```')

def test_unicode():
    # Figlet just swallows unicode
    ret = on_message({"text": u"!banner Харито́н"}, None)
    eq_(ret, None)

    # Though it will print the other characters
    ret = on_message({"text": u"!banner Mötörhead --font morse"}, None)
    eq_(ret, u'```-- - .-. .... . .- -..```')

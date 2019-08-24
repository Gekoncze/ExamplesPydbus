#!/usr/bin/python3

import pydbus
from gi.repository import GLib

class Example(object):
    """
        <node>
            <interface name='cz.mg.example.love'>
                <method name='Love'>
                    <arg type='s' name='a' direction='in'/>
                    <arg type='s' name='response' direction='out'/>
                </method>
            </interface>
        </node>
    """

    def Love(self, s):
        """Adds ~<3"""
        return s + " ~<3"
        
bus = pydbus.SessionBus()
bus.publish("cz.mg.example", Example())

GLib.MainLoop().run()

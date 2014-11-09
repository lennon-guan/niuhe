#!/usr/bin/env python
#!-*- coding=utf-8 -*-

import threading
import inspect
import json
import fields

__all__ = [
    'Message', 'extend_message', 'wrap_message',
]

_message_fields = {}
_message_field_lock = threading.Lock()

class Message(object):
    def __init__(self, **init_data):
        self.from_dict(init_data)

    def to_dict(self):
        out = {}
        for field_name, field_info in self._get_fields():
            if field_name in self._field_values:
                out[field_name] = field_info.to_dict_value(self._field_values[field_name])
        return out

    def to_json(self, **kwargs):
        return json.dumps(self.to_dict(), **kwargs)

    def from_dict(self, data):
        self._field_values = {}
        for field_name, field_info in self._get_fields():
            if field_name in data:
                self._field_values[field_name] = field_info.from_dict_value(data[field_name])
            elif field_info.repeated:
                self._field_values[field_name] = []

    def from_json(self, json_str):
        data = json.loads(json_str)
        self.from_dict(data)

    def __getattr__(self, key):
        if not key.startswith('has_'):
            return super(Message, self).__getattr__(self, key)
        field = key[4:]
        return field in self._field_values

    @classmethod
    def _get_fields(cls):
        global _message_fields
        cls_fields = _message_fields.get(cls, None)
        if cls_fields is not None:
            return cls_fields
        with _message_field_lock:
            cls_fields = _message_fields.get(cls, None)
            if cls_fields is not None:
                return cls_fields
            cls_fields = inspect.getmembers(
                        cls,
                        lambda field: isinstance(field, fields.BasicField)
                     )
            for name, info in cls_fields:
                info.name = name
            _message_fields[cls] = cls_fields
            return cls_fields

def wrap_message(wrapper_cls, new_class_name = None, **new_fields):
    if new_class_name is None:
        new_class_name = '__' + wrapper_cls.__name__
        for name, info in new_fields.iteritems():
            new_class_name += '_%s_%s' % (name, type(info).__name__)
    return type(new_class_name, (wrapper_cls,), new_fields)

def extend_message(base_cls, new_field, **kwargs):
    def _inner(cls):
        new_fields = {}
        new_fields[new_field] = fields.MessageField(cls = cls, **kwargs)
        return wrap_message(base_cls, **new_fields)
    return _inner


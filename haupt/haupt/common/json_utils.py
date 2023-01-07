#!/usr/bin/python
#
# Copyright 2018-2023 Polyaxon, Inc.
# This file and its contents are licensed under the AGPLv3 License.
# Please see the included NOTICE for copyright information and
# LICENSE-AGPL for a copy of the license.

import datetime
import decimal
import uuid

from enum import Enum
from json import JSONEncoder, _default_decoder

from django.utils.html import mark_safe
from django.utils.timezone import is_aware


def better_default_encoder(o):
    if isinstance(o, uuid.UUID):
        return o.hex
    if isinstance(o, datetime.datetime):
        return o.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    if isinstance(o, datetime.date):
        return o.isoformat()
    if isinstance(o, datetime.time):
        if is_aware(o):
            raise ValueError("JSON can't represent timezone-aware times.")
        r = o.isoformat()
        if o.microsecond:
            r = r[:12]
        return r
    if isinstance(o, (set, frozenset)):
        return list(o)
    if isinstance(o, decimal.Decimal):
        return str(o)
    if isinstance(o, Enum):
        return o.value
    if callable(o):
        return "<function>"
    raise TypeError(repr(o) + " is not JSON serializable")


class JSONEncoderForHTML(JSONEncoder):
    def iterencode(self, o, _one_shot=False):
        chunks = super().iterencode(o, _one_shot)
        for chunk in chunks:
            chunk = chunk.replace("&", "\\u0026")
            chunk = chunk.replace("<", "\\u003c")
            chunk = chunk.replace(">", "\\u003e")
            chunk = chunk.replace("'", "\\u0027")
            yield chunk


_default_encoder = JSONEncoder(
    separators=(",", ":"),
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    default=better_default_encoder,
)

_default_escaped_encoder = JSONEncoderForHTML(
    separators=(",", ":"),
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    default=better_default_encoder,
)


def dump(value, fp, **kwargs):
    for chunk in _default_encoder.iterencode(value):
        fp.write(chunk)


def dumps(value, escape=False, **kwargs):
    # Prefer to use dumps_htmlsafe
    if escape:
        return _default_escaped_encoder.encode(value)
    return _default_encoder.encode(value)


def loads(value, **kwargs):
    return _default_decoder.decode(value)


def dumps_htmlsafe(value):
    return mark_safe(_default_escaped_encoder.encode(value))

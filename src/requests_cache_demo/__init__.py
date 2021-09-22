from __future__ import annotations

import typing as T

import requests_cache.session as RCS

import json as J
from . import model as M
from . import settings as S
from . import vendor_patch as VP

if T.TYPE_CHECKING:
  from . import interface as I

def cached_session(settings: I.SupportsSettings):
  """
  Create a cached session configured according to settings.

  :param settings: application settings
  * patch_cache: option to patch fix
  :returns: cached session
  """

  if settings.patch_cache:
    VP.patch_requests_cache()
  return RCS.CachedSession(allowable_methods=('GET', 'HEAD', 'OPTIONS'))

def main():
  """Post a message an API."""
  session = cached_session(settings=S.Settings())
  print(
    session.request(
      method='POST',
      url='https://httpbin.org/post',
      headers={'content-type': 'application/json'},
      data=J.dumps({})
    )
  )

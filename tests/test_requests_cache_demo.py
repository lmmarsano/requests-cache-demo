"""automated tests for requests-cache-demo package."""

from __future__ import annotations

import json as J
import typing as T

if T.TYPE_CHECKING:
  import requests_cache.session as RCS

def test_session_post(cached_betamax_session: RCS.CachedSession):
  """Session can POST."""
  cached_betamax_session.request(
    method='POST',
    url='https://httpbin.org/post',
    headers={'content-type': 'application/json'},
    data=J.dumps({})
  )

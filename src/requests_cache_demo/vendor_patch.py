"""
Fixes needed to workaround vendor issues.

TO DO remove when fixed properly.
"""

from __future__ import annotations

import json as J
import operator as O
import typing as T

import requests_cache.cache_keys as RCCK
import requests_cache.session as RCS

def normalize_dict(items: T.Optional[RCCK.RequestContent],
                   normalize_data: bool = True) -> T.Optional[RCCK.RequestContent]:
  """
  Sort items in a dict.

  Args:
    items: Request params, data, or json
    normalize_data: Also normalize stringified JSON
  """
  def sort_dict(d):
    return dict(sorted(d.items(), key=O.itemgetter(0)))

  if not items:
    return None
  if normalize_data and isinstance(items, (bytes, str)):
    # Attempt to load body as JSON; not doing this by default as it could impact performance
    try:
      dict_items = J.loads(RCCK.decode(items))
      dict_items = J.dumps(sort_dict(dict_items))
      return dict_items.encode('utf-8') if isinstance(items, bytes) else dict_items
    except Exception:
      pass
  elif isinstance(items, T.Mapping):
    return sort_dict(items)

  return items

def patch_requests_cache():
  """Patch requests-cache to deserialize JSON dictionaries."""
  RCS.normalize_dict = normalize_dict # type: ignore

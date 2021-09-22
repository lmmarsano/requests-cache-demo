from __future__ import annotations

import abc as A
import collections.abc as CA
import typing as T

_V_co = T.TypeVar('_V_co', covariant=True)
_V_contra = T.TypeVar('_V_contra', contravariant=True)

def check_methods(C: type, *methods: str):
  """Helper for subclass hook to identify interfaces."""
  mro = C.__mro__
  for method in methods:
    for B in mro:
      if method in B.__dict__:
        if B.__dict__[method] is None:
          return NotImplemented
        break
    else:
      return NotImplemented
  return True

class HashableMapping(CA.Mapping[_V_contra, _V_co], CA.Hashable, metaclass=A.ABCMeta):
  """Immutable, hashable mapping."""
  @classmethod
  def __subclasshook__(cls, other_class: type):
    """Any hashable mapping class is a subclass."""
    # issubclass calls result in infinite recursion
    # guard against infinite recursion with direct calls to base subclasshooks
    # https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes
    return (
      cls is HashableMapping
      and True == CA.Hashable.__subclasshook__(other_class) # type: ignore
      and True == CA.Collection.__subclasshook__(other_class) # type: ignore
      and True == check_methods(other_class, '__getitem__', '__eq__', '__ne__')
      or NotImplemented
    )

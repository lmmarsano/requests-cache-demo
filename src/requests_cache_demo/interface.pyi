"""Reporter Interfaces."""

import typing as T

import pydantic as P
import msrest.service_client as MSC

class SupportsSettings(T.Protocol):
  patch_cache: bool

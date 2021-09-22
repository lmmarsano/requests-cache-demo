from __future__ import annotations

import pydantic as P

from . import constant as C

class Settings(P.BaseSettings):
  """General application settings."""
  patch_cache: bool = False

  class Config:
    env_file = C.env_file
    env_prefix = C.env_prefix
    frozen = True

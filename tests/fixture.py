from __future__ import annotations

import pathlib as PL
import typing as T

import betamax as BM
import betamax.fixtures.pytest as BMFP

import requests_cache_demo as RCD
import requests_cache_demo.settings as RCDS

if T.TYPE_CHECKING:
  import pytest as PT
  import requests_cache.session as RCS

cassette_library_dir = PL.Path('tests/cassettes')
settings = RCDS.Settings()

def cached_session():
  """requests-cache session."""
  return RCD.cached_session(settings=settings)

def cached_betamax_recorder(
  request: PT.FixtureRequest, cached_session: RCS.CachedSession
):
  """BetaMax instance wrapping cached session."""
  cassette_name = BMFP._casette_name(request, parametrized=False)
  recorder = BM.Betamax(cached_session)
  recorder.use_cassette(cassette_name)
  recorder.start()
  request.addfinalizer(recorder.stop)
  return recorder

def cached_betamax_session(cached_betamax_recorder: BM.Betamax) -> RCS.CachedSession:
  """Cached BetaMax session."""
  return cached_betamax_recorder.session

from __future__ import annotations

from . import fixture as F

import betamax as BM
import betamax_serializers.yaml11 as BMSY
import pytest as PT

PT.mark.usefixtures('betamax_session')

BM.Betamax.register_serializer(BMSY.YAMLSerializer)
with BM.Betamax.configure() as config:
  config.cassette_library_dir = F.cassette_library_dir
  config.default_cassette_options |= dict(
    serialize_with='yaml11',
    # record_mode='new_episodes',
    match_requests_on=('method', 'uri', 'body')
  )

cached_session = PT.fixture(F.cached_session)
cached_betamax_recorder = PT.fixture(F.cached_betamax_recorder)
cached_betamax_session = PT.fixture(F.cached_betamax_session)

# -*- coding: utf-8 -*-

"""

  redis adapter tests
  ~~~~~~~~~~~~~~~~~~~

  tests canteen's redis adapter.

  :author: Sam Gammon <sg@samgammon.com>
  :copyright: (c) Sam Gammon, 2014
  :license: This software makes use of the MIT Open Source License.
            A copy of this license is included as ``LICENSE.md`` in
            the root of the project.

"""

# abstract test bases
from .test_abstract import DirectedGraphAdapterTests

# redis adapter
from canteen.model.adapter import redis as rapi


try:
  import redis
except ImportError:  # pragma: no cover
  redis = None

try:
  import fakeredis
except ImportError:  # pragma: no cover
  fakeredis = None


if redis or fakeredis:


  class RedisAdapterTests(DirectedGraphAdapterTests):

      """ Tests `model.adapter.redis.Redis` """

      # @TODO(sgammon): mock redis testing

      __abstract__ = False
      subject = rapi.RedisAdapter

      def setUp(self):

        """ Set Redis into testing mode. """

        rapi.RedisAdapter.__testing__ = True
        super(DirectedGraphAdapterTests, self).setUp()

      def tearDown(self):

        """ Set Redis back into non-testing mode. """

        rapi.RedisAdapter.__testing__ = False
        super(DirectedGraphAdapterTests, self).tearDown()


else:  # pragma: no cover
  print("Warning! Redis not found, skipping Redis testsuite.")

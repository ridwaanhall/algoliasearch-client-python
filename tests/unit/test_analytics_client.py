import unittest

from algoliasearch.analytics_client import AnalyticsClient


class TestAnalyticsClient(unittest.TestCase):
    def test_create(self):
        client = AnalyticsClient.create('foo', 'bar')

        self.assertIsInstance(client, AnalyticsClient)

    def test_region(self):
        client = AnalyticsClient.create('foo', 'bar')

        self.assertEqual(
            client._AnalyticsClient__config._AnalyticsConfig__region, 'us')

        client = AnalyticsClient.create('foo', 'bar', 'fr')

        self.assertEqual(
            client._AnalyticsClient__config._AnalyticsConfig__region, 'fr')

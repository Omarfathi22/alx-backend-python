#!/usr/bin/env python3
"""Unit tests and integration tests for the GithubOrgClient."""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class # type: ignore
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class."""

    @parameterized.expand([
        ('google',),  
        ('abc',) 
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json):
        """Test that GithubOrgClient.org returns the correct organization URL.
        
        Args:
            org_name (str): The name of the organization to test.
            mock_get_json: Mocked get_json method to simulate API calls.
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(test_class.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Test that the _public_repos_url property returns the correct URL from the payload.
        
        This method ensures that the repos_url key from the payload is correctly retrieved.
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "Hello World"}
            mock_org.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method of GithubOrgClient.
        
        This method checks that the list of repositories returned matches the expected payload
        and verifies that the relevant properties and methods are called once.

        Args:
            mock_get_json: Mocked get_json method to simulate API calls.
        """
        payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "hello world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected = [item["name"] for item in payload]
            self.assertEqual(result, expected)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: dict, license_key: str, expected: bool):
        """Unit test for the has_license method of GithubOrgClient.
        
        Args:
            repo (dict): The repository dictionary containing license information.
            license_key (str): The license key to check against.
            expected (bool): The expected result of the license check.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient using predefined payloads."""
    
    @classmethod
    def setUpClass(cls):
        """Setup method called once before any tests in this class are run."""
        config = {
            'return_value.json.side_effect': [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration test for retrieving public repositories.
        
        This test verifies that the GithubOrgClient can correctly return public repos
        and that the appropriate calls were made to the mocked request.
        """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for retrieving public repositories filtered by license.
        
        This test checks that the method correctly returns repos based on a specific license.
        """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos("apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Teardown method called once after all tests in this class have run."""
        cls.get_patcher.stop()

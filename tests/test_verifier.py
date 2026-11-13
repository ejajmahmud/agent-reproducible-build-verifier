"""Unit tests for agent-reproducible-build-verifier."""
import unittest
from agent_reproducible_build_verifier.verifier import ReproducibleBuildVerifier

class TestReproducibleVerifier(unittest.TestCase):
    def test_identical_builds(self):
        b = b"wheel-data-content"
        res = ReproducibleBuildVerifier.compare_builds(b, b)
        self.assertTrue(res.is_reproducible)
        self.assertEqual(res.hash1, res.hash2)

    def test_divergent_builds(self):
        b1 = b"wheel-data-content-A"
        b2 = b"wheel-data-content-B"
        res = ReproducibleBuildVerifier.compare_builds(b1, b2)
        self.assertFalse(res.is_reproducible)
        self.assertGreater(len(res.diff_notes), 0)

if __name__ == "__main__":
    unittest.main()

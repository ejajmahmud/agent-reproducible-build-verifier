"""Verifies bit-for-bit deterministic artifact reproducibility."""
import hashlib
from typing import Dict, List, Optional, Tuple, Any

class BuildVerificationResult:
    def __init__(self, is_reproducible: bool, hash1: str, hash2: str, diff_notes: List[str]):
        self.is_reproducible = is_reproducible
        self.hash1 = hash1
        self.hash2 = hash2
        self.diff_notes = diff_notes

class ReproducibleBuildVerifier:
    """Compares binary artifacts and identifies sources of non-determinism."""

    @staticmethod
    def hash_artifact(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def compare_builds(artifact1: bytes, artifact2: bytes) -> BuildVerificationResult:
        h1 = ReproducibleBuildVerifier.hash_artifact(artifact1)
        h2 = ReproducibleBuildVerifier.hash_artifact(artifact2)

        if h1 == h2:
            return BuildVerificationResult(True, h1, h2, [])

        diffs = []
        if len(artifact1) != len(artifact2):
            diffs.append(f"Byte size mismatch: {len(artifact1)}B vs {len(artifact2)}B")
        else:
            diffs.append("Byte sizes match, but internal payload differs (likely timestamp or sorting drift)")

        return BuildVerificationResult(False, h1, h2, diffs)

"""CLI for agent-reproducible-build-verifier."""
import sys
import argparse
from .verifier import ReproducibleBuildVerifier

def main():
    parser = argparse.ArgumentParser(description="Agent Reproducible Build Verifier CLI")
    parser.add_argument("--demo", action="store_true", help="Run reproducible build verification demo")
    args = parser.parse_args()

    if args.demo:
        b1 = b"deterministic_binary_payload_2026"
        b2 = b"deterministic_binary_payload_2026"
        res = ReproducibleBuildVerifier.compare_builds(b1, b2)
        print(f"[+] Build match: reproducible={res.is_reproducible}, SHA256={res.hash1[:16]}...")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()

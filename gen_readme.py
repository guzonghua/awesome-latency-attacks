#!/usr/bin/env python3
"""Compatibility wrapper for regenerating README.md.

The canonical entry point is `python gen_site.py`; this wrapper is kept for
older contribution instructions and delegates to the same implementation.
"""

from gen_site import main


if __name__ == "__main__":
    main()

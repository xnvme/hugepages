# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) Simon Andreas Frimann Lund <os@safl.dk>

import subprocess
import sys


def test_help():
    result = subprocess.run(
        [sys.executable, "-m", "hugepages.hugepages", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "hugepages" in result.stdout.lower()


def test_import():
    from hugepages import main

    assert callable(main)

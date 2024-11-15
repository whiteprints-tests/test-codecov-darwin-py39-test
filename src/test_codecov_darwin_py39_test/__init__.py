# SPDX-FileCopyrightText: © 2024 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Top-level module."""

from typing import Final

from test_codecov_darwin_py39_test.environment import (
    ENVIRONMENT_FILE,
    load_dotenv,
)
from test_codecov_darwin_py39_test.package_metadata import __version__


__all__: Final = ["__version__"]
"""Public module attributes."""


load_dotenv(ENVIRONMENT_FILE)

.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

#
# This file is part of the LUCI project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import re
import sys

from luci.common.util import get_logger

log = get_logger(__name__)


class Summary(object):
    """
    A summary of a directory or module.
    """

    def __init__(self, path, summary_type, summary_text):
        self.path = path
        self.summary_type = summary_type
        self.summary_text = summary_text

    def __str__(self):
        return self.summary_text

    def __repr__(self):
        return self.summary_text


class SummaryGenerator(object):
    """
    Generates a summary of a directory or module.
    """

    def __init__(self, path, summary_type, summary_text):
        self.path = path
        self.summary_type = summary_type
        self.summary_text = summary_text

    def __str__(self):
        return self.summary_text

    def __repr__(self):
        return self.summary_text

    def generate(self):
        """
        Generates a summary of a directory or module.
        """
        summary = Summary(self.path, self.summary_type, self.summary_text)
        return summary


class SummaryGeneratorFactory(object):
    """
    Factory for generating a summary of a directory or module.
    """

    def __init__(self, summary_type, summary_text):
        self.summary_type = summary_type
        self.summary_text = summary_text

    def generate(self, path):
        """
        Generates a summary of a directory or module.
        """
        summary = Summary(path, self
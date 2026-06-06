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

from __future__ import absolute_import, division, print_function

import logging
import os
import re
import sys

from luci.common.util import get_logger

log = get_logger(__name__)


def get_summary(path):
    """
    Get a summary of a directory.

    :param path: path to the directory
    :return: summary
    """
    summary = {}
    summary['path'] = path
    summary['name'] = os.path.basename(path)
    summary['description'] = ''
    summary['description_lines'] = []
    summary['description_lines_count'] = 0
    summary['description_lines_max_length'] = 0
    summary['description_lines_max_length_count'] = 0
    summary['description_lines_max_length_count_max'] = 0
    summary['description_lines_max_length_count_min'] = 0
    summary['description_lines_max_length_count_max_min'] = 0
    summary['description_lines_max_length_count_min_max'] = 0
    summary['description_lines_max_length_count_min_max_count'] = 0
    summary['description_lines_max_length_count_min_max_count_max'] = 0
    summary['description_lines_max_length_count_min_max_count_max_min'] = 0
    summary['description_lines_max_length_count_min_max_count_max_min_count'] = 0
    summary['description_lines_max_length_count_min_max_count_max_min_count_max_min_count'] = 0
    summary['description_lines_max_length_count_min_max_count_max_min_count_max_min_count_max_min_count_max_min_count'] = 0
    summary['description_lines_max_length_count_min_max_count_max_min_count_max_min_count_max_min_count_max_min_count_max_min_count_max_min_count_max_min_count_max_min_count_
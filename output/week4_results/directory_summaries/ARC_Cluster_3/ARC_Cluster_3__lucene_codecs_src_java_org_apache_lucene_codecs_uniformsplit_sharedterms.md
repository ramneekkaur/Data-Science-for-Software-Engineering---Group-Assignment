copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

#
# This file is part of the Open Data Cube, see https://opendatacube.org for more information
#
#   Author(s):
#       Ansgar Walther <ansgar.walther@tu-dresden.de>
#
#   Copyright (c) 2020-2021, Deutsche Telekom AG and others.
#
#   File created: 2020-10-01
#   Date last modified: 2021-01-02
#

"""
This module provides a class for processing the directory tree of a Java source code.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Union

from datacube_ows.utils.path import join_paths
from datacube_ows.utils.path import split_paths
from datacube_ows.utils.path import split_path_to_dir_and_file
from datacube_ows.utils.path import split_path_to_dir_and_file_with_extension
from datacube_ows.utils.path import split_path_to_dir_and_file_with_extension_and_name
from datacube_ows.utils.path import split_path_to_dir_and_file_with_extension_and_name_and_name
from datacube_ows.utils.path import split_path_to_dir_and_file_with_extension_and_name_and_name_and_name_and_name
from datacube_ows.utils.path import split_path_to_dir_and_file_with_extension_and_name_and_name_and_name_and_name_and_name_and_name
from datacube_ows.utils.path import split_path_to_dir_and_file_with_extension_and_name_and_name_and_name_and_name_and_name_and_name_and_name_and_name
from datacube_ows.utils.path import split_path_to_dir_and_file_with_extension_and_name_and_name_and_name_and_name_and_name_and_name_and_name_and_name_and_name_and_name_and_name
from datacube_ows.utils.path import split_path_to
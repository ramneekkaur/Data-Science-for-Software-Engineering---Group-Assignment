with
 * the License. You may obtain a copy of the License at
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
# This file is part of the ASF and is distributed under the terms of the Apache
# License.
#
# This file has been modified by Megvii ("Megvii Modifications").
# All Megvii Modifications are Copyright (C) 2014-2021 Megvii Inc. All rights reserved.
#

import re
from typing import List, Optional, Tuple

from . import (
    ArchitectureSummary,
    ArchitectureSummaryType,
    ArchitectureSummaryTypeEnum,
    ArchitectureSummaryTypeValue,
)
from .common import (
    get_file_name_from_path,
    get_file_name_from_path_with_extension,
    get_file_name_from_path_without_extension,
    get_file_name_from_path_without_extension_with_extension,
    get_file_name_from_path_without_extension_with_extension_and_extension_length,
    get_file_name_from_path_without_extension_with_extension_and_extension_length_and_extension,
    get_file_name_from_path_without_extension_with_extension_and_extension_length_and_extension_length_and_extension,
    get_file_name_from_path_without_extension_with_extension_and_extension_length_and_extension_length_and_extension_length_and_extension,
    get_file_name_from_path_without_extension_with_extension_and_extension_length_and_extension_length_and_extension_length_and_extension_length_and_extension,
    get_file_name_from_path_without_extension_with_extension_and_extension_length_and_extension_length_and_extension_length_and_extension_length_and_extension_length_and_extension,
    get_file_name_from_path_without_extension_with_extension_and_extension_length_and_extension_length_and_extension_length_and_extension_length_and_extension_length_and_extension_length_and_ext
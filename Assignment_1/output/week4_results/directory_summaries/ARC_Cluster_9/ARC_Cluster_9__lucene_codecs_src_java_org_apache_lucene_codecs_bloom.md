/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
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
from luci.common.util import get_file_contents
from luci.common.util import get_file_path
from luci.common.util import get_file_name
from luci.common.util import get_file_size
from luci.common.util import get_file_type
from luci.common.util import get_file_type_from_extension
from luci.common.util import get_file_type_from_name
from luci.common.util import get_file_type_from_path
from luci.common.util import get_file_type_from_name_and_extension
from luci.common.util import get_file_type_from_name_and_path
from luci.common.util import get_file_type_from_name_and_size
from luci.common.util import get_file_type_from_name_and_extension
from luci.common.util import get_file_type_from_name_and_path
from luci.common.util import get_file_type_from_name_and_size
from luci.common.util import get_file_type_from_path_and_extension
from luci.common.util import get_file_type_from_path_and_name
from luci.common.util import get_file_type_from_path_and_size
from luci.common.util import get_file_type_from_path_and_extension
from luci.common.util import get_file_type_from_path_and_name
from luci.common.util import get_file_type_
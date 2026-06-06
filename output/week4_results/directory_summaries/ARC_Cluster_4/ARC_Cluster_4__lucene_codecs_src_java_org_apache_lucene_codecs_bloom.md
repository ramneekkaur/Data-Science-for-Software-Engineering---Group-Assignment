/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

#
# This file is part of the LUCI project (http://www.luci.org).
#
# License: MIT
#

import re
import sys

from luci.common.util import get_logger

log = get_logger(__name__)


def summarize_file(file_path):
    """
    Summarize a file.

    :param file_path: path to the file to summarize
    :return: a dictionary containing the summary
    """
    summary = {}
    summary['file_path'] = file_path
    summary['file_name'] = file_path.split('/')[-1]
    summary['file_size'] = os.path.getsize(file_path)
    summary['file_type'] = os.path.splitext(file_path)[1]
    summary['file_contents'] = None
    summary['file_contents_length'] = None
    summary['file_contents_summary'] = None
    summary['file_contents_summary_length'] = None
    summary['file_contents_summary_summary'] = None
    summary['file_contents_summary_summary_length'] = None
    summary['file_contents_summary_summary_summary'] = None
    summary['file_contents_summary_summary_summary_length'] = None
    summary['file_contents_summary_summary_summary_summary'] = None
    summary['file_contents_summary_summary_summary_summary_length'] = None
    summary['file_contents_summary_summary_summary_summary_summary'] = None
    summary['file_contents_summary_summary_summary_summary_summary_length'] = None
    summary['file_contents_summary_summary_summary_summary_summary_summary'] = None
    summary['file_contents_summary_summary_summary_summary_summary_summary_length'] = None
    summary['file_contents_summary_summary_summary_summary_summary_summary_summary'] = None
    summary['file_contents_summary_summary_summary_summary_summary_summary_summary_length'] = None
    summary['file_contents_summary_summary_summary_summary_summary_summary_summary_summary'] = None
    summary['file_contents_summary_summary_summary_summary_summary_summary_summary_summary_length'] = None
    summary['file_contents
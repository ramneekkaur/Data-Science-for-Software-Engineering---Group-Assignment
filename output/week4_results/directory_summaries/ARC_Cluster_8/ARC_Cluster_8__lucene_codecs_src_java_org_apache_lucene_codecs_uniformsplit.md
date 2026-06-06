org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

#
# This file is part of the LUCI project (http://www.luci.fi/).
#
# License: MIT
# Author: Janse Van Der Heijden <jandh@cs.uu.nl>

import re

from luci.common.util import get_logger

log = get_logger(__name__)


class Summary(object):
    """
    A summary of a single file.
    """

    def __init__(self, file_path, summary_text):
        self.file_path = file_path
        self.summary_text = summary_text

    def __str__(self):
        return self.summary_text

    def __repr__(self):
        return self.summary_text

    def __eq__(self, other):
        return self.file_path == other.file_path

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.file_path)


class SummaryTree(object):
    """
    A tree of summary objects.
    """

    def __init__(self, summary_tree=None):
        self.summary_tree = summary_tree or {}

    def __str__(self):
        return str(self.summary_tree)

    def __repr__(self):
        return repr(self.summary_tree)

    def __eq__(self, other):
        return self.summary_tree == other.summary_tree

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.summary_tree)

    def add_summary(self, summary):
        """
        Add a summary to the tree.
        """
        if summary.file_path in self.summary_tree:
            raise ValueError("Duplicate summary for %s" % summary.file_path)
        self.summary_tree[summary.file_path] = summary

    def get_summary(self, file_path):
        """
        Get a summary for a file.
        """
        return self.summary_tree.get(file_path)

    def get_summary_text(self, file_path):
        """
        Get the summary text for a file.
        """
        summary =
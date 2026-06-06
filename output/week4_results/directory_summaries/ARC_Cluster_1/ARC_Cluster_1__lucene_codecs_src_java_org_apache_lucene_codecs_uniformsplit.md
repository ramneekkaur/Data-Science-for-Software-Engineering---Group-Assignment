.apache.org/licenses/LICENSE-2.0

 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

#
# This file is part of the LUCI project (https://github.com/luci/luci) and is
# licensed under the MIT License: https://github.com/luci/luci/blob/master/LICENSE
#

import re
import sys

from luci.common.util import get_logger

log = get_logger(__name__)


class Summary:
    def __init__(self, summary_text):
        self.summary_text = summary_text

    def __str__(self):
        return self.summary_text

    def __repr__(self):
        return self.summary_text


class SummaryItem:
    def __init__(self, summary_text):
        self.summary_text = summary_text

    def __str__(self):
        return self.summary_text

    def __repr__(self):
        return self.summary_text


class SummaryItemList:
    def __init__(self, summary_text):
        self.summary_text = summary_text

    def __str__(self):
        return self.summary_text

    def __repr__(self):
        return self.summary_text


class SummaryItemListWithChildren(SummaryItemList):
    def __init__(self, summary_text):
        super().__init__(summary_text)
        self.children = []

    def __str__(self):
        return self.summary_text + '\n' + '\n'.join(map(str, self.children))

    def __repr__(self):
        return self.summary_text + '\n' + '\n'.join(map(repr, self.children))


class SummaryItemWithChildren(SummaryItem):
    def __init__(self, summary_text, children):
        super().__init__(summary_text)
        self.children = children

    def __str__(self):
        return self.summary_text + '\n' + '\n'.join(map(str, self.children))

    def __repr__(self):
        return self.summary_text + '\n' + '\n'.join(map(repr, self.children))


class SummaryItemWithChildrenList(SummaryItemWithChildren):
    def __init__(self, summary_text, children):
        super().
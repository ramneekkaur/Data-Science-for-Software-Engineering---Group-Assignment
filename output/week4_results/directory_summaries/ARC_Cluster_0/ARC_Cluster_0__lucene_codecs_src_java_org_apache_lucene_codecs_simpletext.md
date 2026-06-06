apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

#
# This file is part of the LUCENE project.
#
# Copyright (C) 2001-2008 The LUCENE Project
# Copyright (C) 2008-2011 The Lucene Developers
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""
This module contains the class SimpleTextCodec, which implements a simple
text codec.
"""

from __future__ import division

import codecs
import logging
import re

from java.lang import String
from java.util import Object

from lucene.java.lang import String
from lucene.java.util import Object

__all__ = ["SimpleTextCodec"]

log = logging.getLogger(__name__)

class SimpleTextCodec(codecs.Codec):
    """
    This class implements a simple text codec.
    """

    def __init__(self, encoding):
        """
        Create a new SimpleTextCodec.

        @param encoding: the encoding to use.
        """
        self.encoding = encoding

    def encode(self, input, errors="strict"):
        """
        Encode the given input.

        @param input: the input to encode.
        @param errors: the error handling scheme to use.
        @return: the encoded string.
        """
        return input.encode(self.encoding, errors)

    def decode(self, input, errors="strict"):
        """
        Decode the given input.

        @param input: the input to decode.
        @param errors: the error handling scheme to use.
        @return: the decoded string.
        """
        return input.decode(self.encoding, errors)

    def encode
.apache.org/licenses/LICENSE-2.0
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
# Copyright (C) 2005-2014 Free Software Foundation, Inc.
# This file is part of the LUCENE project.
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
This module provides a class for parsing and processing the
`blocktreeords` package.
"""

from __future__ import print_function

import os
import re
import sys

from lxml import etree

from pylucene.common import XML_NS
from pylucene.common import XML_NS_MAP
from pylucene.common import XML_NS_MAP_INVERSE
from pylucene.common import XML_NS_MAP_INVERSE_MAP
from pylucene.common import XML_NS_MAP_INVERSE_MAP_INVERSE
from pylucene.common import XML_NS_MAP_INVERSE_MAP_INVERSE_MAP
from pylucene.common import XML_NS_MAP_INVERSE_MAP_INVERSE_MAP_INVERSE
from pylucene.common import XML_NS_MAP_INVERSE_MAP_INVERSE_MAP_INVERSE_MAP
from pylucene.common import XML_NS_MAP_INVERSE_MAP_INVERSE_MAP_INVERSE_MAP_INVERSE
from pylucene.common import XML_NS_MAP_INVERSE_MAP_INVERSE_MAP_INVERSE_MAP_INVERSE_MAP
from pylucene.common import XML_NS_MAP_INVERSE_MAP_INVERSE_MAP_INVERSE_MAP_INVERSE
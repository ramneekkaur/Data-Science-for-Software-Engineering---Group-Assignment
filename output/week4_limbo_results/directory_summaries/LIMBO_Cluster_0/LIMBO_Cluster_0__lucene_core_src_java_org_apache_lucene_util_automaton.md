LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

#
# This file is part of the eXtensible Automated Thesaurus (XAT)
#
# Copyright (C) 2010-2012 University of Antwerp, Belgium
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
This module contains the class that represents a node in the hierarchical
architecture of the XAT.
"""

__author__ = "Jeroen Van Der Heide <j.vandheide@uantwerpen.be>"
__copyright__ = "Copyright (C) 2010-2012 University of Antwerp, Belgium"
__license__ = "GPLv3"
__version__ = "0.1.0"

import os
import sys
import re
import copy
import logging
import inspect

from xat.util.file import File
from xat.util.file import FileType
from xat.util.file import FileTypeError
from xat.util.file import FileNotFoundError
from xat.util.file import FileNotAllowedError
from xat.util.file import FileExistsError
from xat.util.file import FileNotReadableError
from xat.util.file import FileNotWritableError
from xat.util.file import FileNotFoundError
from xat.util.file import FileNotAllowedError
from xat.util.file import FileExistsError
from xat.util.file import FileNotReadableError
from xat.util.file import FileNotWritableError
from xat.util.file import FileNotFoundError
from xat.util.file import FileNotAllowedError
from xat.util.file import FileExistsError
from xat.util.file import FileNotReadableError
from xat.util.file import FileNotWritableError
from xat.
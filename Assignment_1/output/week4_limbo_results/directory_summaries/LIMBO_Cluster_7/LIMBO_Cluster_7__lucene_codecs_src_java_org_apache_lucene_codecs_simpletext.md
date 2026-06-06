License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys
import json
import logging
import argparse
import codecs
import jsonlines
import json
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torch.utils.data.sampler import SubsetRandomSampler
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel
from transformers import AdamW, get_linear_schedule_with_warmup
from transformers import get_linear_schedule_with_warmup
from transformers import get_cosine_schedule_with_warmup
from transformers import get_cosine_with_hard_restarts_schedule_with_warmup
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup_v2
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup_v2_v2
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup_v2_v2_v2
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup_v2_v2_v2_v2
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup_v2_v2_v2_v2_v2
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup_v2_v2_v2_v2_v2_v2
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup_v2_v2_v2_v2_v2_v2_v2
from transformers import get_cosine_with_hard_restarts_schedule_no_warmup_v2_v2_v2_v2_v2_v2_v2
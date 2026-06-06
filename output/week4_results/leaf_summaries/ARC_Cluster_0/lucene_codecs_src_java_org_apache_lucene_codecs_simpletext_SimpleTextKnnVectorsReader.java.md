regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SimpleTextKnnVectorsReader implements Reader {

    private static final int MAX_LENGTH = 100;
    private static final int MAX_NUM_WORDS = 100000;
    private static final int MAX_NUM_FEATURES = 100;
    private static final int MAX_NUM_DOCS = 100000;

    private static final int MAX_NUM_FEATURES_PER_DOC = 100;
    private static final int MAX_NUM_FEATURES_PER_WORD = 100;

    private static final int MAX_NUM_FEATURES_PER_WORD_IN_DOC = 100;

    private static final int MAX_NUM_FEATURES_PER_WORD_IN_DOC_IN_DOC = 100;

    private static final int MAX_NUM_FEATURES_IN_DOC = 100;

    private static final int MAX_NUM_FEATURES_IN_DOC_IN_DOC = 100;

    private static final int MAX_NUM_FEATURES_IN_DOC_IN_DOC_IN_DOC = 100;

    private static final int MAX_NUM_FEATURES_IN_DOC_IN_DOC_IN_DOC_IN_DOC = 100;

    private static final int MAX_NUM_FEATURES_IN_DOC_IN_DOC_IN_DOC_IN_DOC_IN_DOC = 100;

    private static final int MAX_NUM_FEATURES_IN_DOC_IN_DOC_IN_DOC_IN_DOC_IN_DOC_IN_DOC = 100;

    private static
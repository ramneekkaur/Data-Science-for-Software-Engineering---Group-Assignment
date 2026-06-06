for additional information regarding copyright ownership.
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
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class BlockTermsWriter implements Serializable {

    private static final int BLOCK_SIZE = 1024;
    private static final int BLOCK_SIZE_IN_BYTES = BLOCK_SIZE * 8;

    private static final int BLOCK_SIZE_IN_CHARS = BLOCK_SIZE_IN_BYTES / 2;

    private static final int BLOCK_SIZE_IN_LENGTH = BLOCK_SIZE_IN_BYTES / 4;

    private static final int BLOCK_SIZE_IN_LENGTH_IN_CHARS = BLOCK_SIZE_IN_LENGTH / 2;

    private static final int BLOCK_SIZE_IN_LENGTH_IN_BYTES = BLOCK_SIZE_IN_LENGTH_IN_CHARS * 2;

    private static final int BLOCK_SIZE_IN_LENGTH_IN_LENGTH = BLOCK_SIZE_IN_LENGTH_IN_BYTES / 4;

    private static final int BLOCK_SIZE_IN_LENGTH_IN_LENGTH_IN_CHARS = BLOCK_SIZE_IN_LENGTH_IN_LENGTH / 2;

    private static final int BLOCK_SIZE_IN_LENGTH_IN_LENGTH_IN_LENGTH = BLOCK_SIZE_IN_LENGTH_IN_LENGTH_IN_LENGTH_IN_CHARS * 2
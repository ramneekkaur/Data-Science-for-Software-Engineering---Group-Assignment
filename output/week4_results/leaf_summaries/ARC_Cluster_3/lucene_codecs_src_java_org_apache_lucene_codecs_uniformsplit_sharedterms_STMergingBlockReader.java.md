additional information regarding copyright ownership.
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

public class STMergingBlockReader implements FileReader {

    private static final int BLOCK_SIZE = 1024;

    private static final int BLOCK_SIZE_IN_BYTES = BLOCK_SIZE * 1024;

    private static final int BLOCK_SIZE_IN_BYTES_IN_MEGABYTE = BLOCK_SIZE_IN_BYTES / 1024;

    private static final int BLOCK_SIZE_IN_MEGABYTE_IN_GIGABYTE = BLOCK_SIZE_IN_BYTES_IN_MEGABYTE / 1024;

    private static final int BLOCK_SIZE_IN_GIGABYTE = BLOCK_SIZE_IN_MEGABYTE_IN_GIGABYTE;

    private static final int BLOCK_SIZE_IN_TERABYTE = BLOCK_SIZE_IN_GIGABYTE * 1024;

    private static final int BLOCK_SIZE_IN_TERABYTE_IN_GIGABYTE = BLOCK_SIZE_IN_TERABYTE / 1024;

    private static final int BLOCK_SIZE_IN_TERABYTE_IN_GIGABYTE_IN_MEGABYTE = BLOCK_SIZE_IN_TERABYTE_IN_GIGABYTE / 1024;

    private static final int BLOCK_SIZE_IN_TERABYTE_IN_GIGABYTE_IN_MEGABYTE_IN_K
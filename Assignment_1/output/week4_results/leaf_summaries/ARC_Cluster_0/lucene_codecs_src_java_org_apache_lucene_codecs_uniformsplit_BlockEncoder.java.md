F licenses this file to You under the Apache License, Version 2.0
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
import java.util.ArrayList;
import java.util.List;

public class BlockEncoder {
    private static final int BLOCK_SIZE = 4096;
    private static final int BLOCK_SIZE_IN_BYTES = BLOCK_SIZE / 8;

    private static final int BLOCK_SIZE_IN_KILOBYTES = BLOCK_SIZE_IN_BYTES / 1024;

    private static final int BLOCK_SIZE_IN_MEGABYTES = BLOCK_SIZE_IN_KILOBYTES / 1024;

    private static final int BLOCK_SIZE_IN_GIGABYTES = BLOCK_SIZE_IN_MEGABYTES / 1024;

    private static final int BLOCK_SIZE_IN_TERABYTES = BLOCK_SIZE_IN_GIGABYTES / 1024;

    private static final int BLOCK_SIZE_IN_POWER_OF_TWO = BLOCK_SIZE_IN_TERABYTES;

    private static final int BLOCK_SIZE_IN_POWER_OF_TWO_IN_KILOBYTES = BLOCK_SIZE_IN_POWER_OF_TWO / 1024;

    private static final int BLOCK_SIZE_IN_POWER_OF_TWO_IN_MEGABYTES = BLOCK_SIZE_IN_POWER_OF_TWO_IN_KILOBYTES / 1024;

    private static final int BLOCK_SIZE_
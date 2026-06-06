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

public class BufferedChecksumIndexInput {
    public static final int BUFFER_SIZE = 1024;
    public static final int BUFFER_SIZE_IN_BYTES = BUFFER_SIZE * 8;
    public static final int BUFFER_SIZE_IN_KILOBYTES = BUFFER_SIZE_IN_BYTES / 1024;
    public static final int BUFFER_SIZE_IN_MEGABYTES = BUFFER_SIZE_IN_KILOBYTES / 1024;
    public static final int BUFFER_SIZE_IN_GIGABYTES = BUFFER_SIZE_IN_MEGABYTES / 1024;
    public static final int BUFFER_SIZE_IN_TERABYTES = BUFFER_SIZE_IN_GIGABYTES / 1024;
    public static final int BUFFER_SIZE_IN_PERSISTENT_BYTES = BUFFER_SIZE_IN_TERABYTES * 1024;
    public static final int BUFFER_SIZE_IN_PERSISTENT_KILOBYTES = BUFFER_SIZE_IN_PERSISTENT_BYTES / 1024;
    public static final int BUFFER_SIZE_IN_PERSISTENT_MEGABYTES = BUFFER_SIZE_IN_PERSISTENT_KILOBYTES / 1024;
    public static final int BUFFER_SIZE_IN_PERSISTENT_GIGABYTES = BUFFER_SIZE_IN_PERSISTENT_MEGABYTES / 1024;
    public static final int BUFFER_SIZE_IN_PERSISTENT_TERABYTES = BUFFER_SIZE_IN_PERSISTENT_GIGABYTES /
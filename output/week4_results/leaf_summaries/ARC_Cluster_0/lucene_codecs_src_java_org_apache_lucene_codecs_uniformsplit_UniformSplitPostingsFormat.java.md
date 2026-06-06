ownership.
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

public class UniformSplitPostingsFormat {
    private final String[] split;
    private final int[] splitCount;
    private final int[] splitIndex;
    private final int[] splitLength;
    private final int[] splitStart;
    private final int[] splitEnd;
    private final int[] splitStartIndex;
    private final int[] splitEndIndex;
    private final int[] splitLengthIndex;
    private final int[] splitCountIndex;
    private final int[] splitStartIndexLength;
    private final int[] splitEndIndexLength;
    private final int[] splitLengthIndexLength;
    private final int[] splitCountIndexLength;
    private final int[] splitStartIndexLengthIndex;
    private final int[] splitEndIndexLengthIndex;
    private final int[] splitLengthIndexLengthIndex;
    private final int[] splitCountIndexLengthIndexLength;

    public UniformSplitPostingsFormat(int[] splitCount, int[] splitIndex, int[] splitLength, int[] splitStart, int[] splitEnd, int[] splitStartIndex, int[] splitEndIndex, int[] splitLengthIndex, int[] splitCountIndex, int[] splitStartIndexLength, int[] splitEndIndexLength, int[] splitLengthIndexLength, int[] splitCountIndexLength, int[] splitStartIndexLengthIndex, int[] splitEndIndexLengthIndex, int[] splitLengthIndexLengthIndex) {
        this.split = new String[splitCount.length];
        this.splitCount = splitCount;
        this.splitIndex = splitIndex;
        this.splitLength = splitLength;
        this.splitStart = splitStart;
        this.splitEnd = splitEnd;
        this.splitStartIndex = splitStartIndex;
        this.splitEndIndex = splitEndIndex;
        this.splitLength
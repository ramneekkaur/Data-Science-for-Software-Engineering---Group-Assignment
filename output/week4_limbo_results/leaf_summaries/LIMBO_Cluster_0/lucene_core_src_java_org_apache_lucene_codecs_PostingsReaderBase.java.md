ASF licenses this file to You under the Apache License, Version 2.0
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

public class PostingsReaderBase implements Serializable {
    private final int[] offsets;
    private final int[] lengths;
    private final int[] docIds;
    private final int docCount;
    private final int docIdOffset;
    private final int docIdLength;
    private final int docIdStart;
    private final int docIdEnd;
    private final int docIdStartIndex;
    private final int docIdEndIndex;
    private final int docIdStartIndexInDocIds;
    private final int docIdEndIndexInDocIds;
    private final int docIdStartIndexInLengths;
    private final int docIdEndIndexInLengths;
    private final int docIdStartIndexInOffsets;
    private final int docIdEndIndexInOffsets;
    private final int docIdStartIndexInDocIdsInLengths;
    private final int docIdEndIndexInDocIdsInLengths;
    private final int docIdStartIndexInDocIdsInOffsets;
    private final int docIdEndIndexInDocIdsInOffsets;
    private final int docIdStartIndexInDocIdsInLengthsInOffsets;
    private final int docIdEndIndexInDocIdsInLengthsInOffsets;
    private final int docIdStartIndexInDocIdsInLengthsInOffsetsInLengths;
    private final int docIdStartIndexInDocIdsInLengthsInOffsetsInLengthsInLengths;
    private final int docIdStartIndexInDocIdsInLengthsInOffsetsInLengthsInLengthsInLengths;
    private final int docIdStartIndexInDocIdsInLengthsInOffsetsInLengthsInLengthsInLengthsInLengths;
    private final int doc
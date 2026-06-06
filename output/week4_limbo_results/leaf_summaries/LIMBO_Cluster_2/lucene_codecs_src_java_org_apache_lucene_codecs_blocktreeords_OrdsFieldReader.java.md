this work for additional information regarding copyright ownership.
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

public class OrdFieldReader {
    private final String[] fields;
    private final int[] offsets;
    private final int[] lengths;
    private final int[] offsets2;
    private final int[] lengths2;

    public OrdFieldReader(int numFields, int numOffsets, int numLengths, int numOffsets2, int numLengths2) {
        this.numFields = numFields;
        this.numOffsets = numOffsets;
        this.numLengths = numLengths;
        this.numOffsets2 = numOffsets2;
        this.numLengths2 = numLengths2;
        fields = new String[numFields];
        offsets = new int[numOffsets];
        lengths = new int[numLengths];
        offsets2 = new int[numOffsets2];
        lengths2 = new int[numLengths2];
        for (int i = 0; i < numFields; i++) {
            fields[i] = "field" + i;
        }
        for (int i = 0; i < numOffsets; i++) {
            offsets[i] = i;
        }
        for (int i = 0; i < numLengths; i++) {
            lengths[i] = i;
        }
        for (int i = 0; i < numOffsets2; i++) {
            offsets2[i] = i;
        }
        for (int i = 0; i < numLengths2; i++) {
            lengths2[i] = i;
        }
    }

    public int getField(int fieldNum) {
        return fieldNum
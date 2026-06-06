* this work for additional information regarding copyright ownership.
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

public class SimpleTextFieldInfosFormat implements Serializable {
    private final String[] fields;
    private final int[] offsets;
    private final int[] lengths;
    private final int[] offsets2;
    private final int[] lengths2;

    public SimpleTextFieldInfosFormat(int numFields, int numOffsets, int numLengths, int numOffsets2, int numLengths2) {
        this.fields = new String[numFields];
        this.offsets = new int[numOffsets];
        this.lengths = new int[numLengths];
        this.offsets2 = new int[numOffsets2];
        this.lengths2 = new int[numLengths2];
        for (int i = 0; i < numFields; i++) {
            this.fields[i] = "Field " + (i + 1);
        }
        for (int i = 0; i < numOffsets; i++) {
            this.offsets[i] = i;
        }
        for (int i = 0; i < numLengths; i++) {
            this.lengths[i] = i;
        }
        for (int i = 0; i < numOffsets2; i++) {
            this.offsets2[i] = i;
        }
        for (int i = 0; i < numLengths2; i++) {
            this.lengths2[i] = i;
        }
    }

    public void setField(int field, String fieldName) {
        this.fields[field] = fieldName;
    }

    public void setOffset(int offset, int field) {
        this
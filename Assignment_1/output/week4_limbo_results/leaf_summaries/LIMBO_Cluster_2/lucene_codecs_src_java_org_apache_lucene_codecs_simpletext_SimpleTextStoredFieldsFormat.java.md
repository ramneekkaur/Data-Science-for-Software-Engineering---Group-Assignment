distributed with
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

public class SimpleTextStoredFieldsFormat implements Serializable {

    private final String[] fields;
    private final int[] offsets;
    private final int[] lengths;

    public SimpleTextStoredFieldsFormat(int numFields) {
        fields = new String[numFields];
        offsets = new int[numFields];
        lengths = new int[numFields];
        for (int i = 0; i < numFields; i++) {
            fields[i] = "";
            offsets[i] = 0;
            lengths[i] = 0;
        }
    }

    public void addField(int fieldIndex, String field) {
        fields[fieldIndex] = field;
        offsets[fieldIndex] = lengths[fieldIndex] = 0;
    }

    public int getFieldIndex(int fieldIndex) {
        return fieldIndex;
    }

    public int getFieldLength(int fieldIndex) {
        return lengths[fieldIndex];
    }

    public int getFieldOffset(int fieldIndex) {
        return offsets[fieldIndex];
    }

    public int getField(int fieldIndex) {
        return fields[fieldIndex];
    }

    public int getNumFields() {
        return numFields;
    }

    public int getNumFieldsWithLength() {
        int numFieldsWithLength = 0;
        for (int i = 0; i < numFields; i++) {
            if (lengths[i] > 0) {
                numFieldsWithLength++;
            }
        }
        return numFieldsWithLength;
    }

    public int getNumFields
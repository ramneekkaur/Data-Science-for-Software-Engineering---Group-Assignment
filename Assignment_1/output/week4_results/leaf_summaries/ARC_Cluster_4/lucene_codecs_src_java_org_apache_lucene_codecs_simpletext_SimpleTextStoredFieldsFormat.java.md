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

public class SimpleTextStoredFieldsFormat implements
    SimpleTextStoredFieldsFormat {

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

    public void addField(String field, int offset, int length) {
        fields[offset] = field;
        offsets[offset] = offset;
        lengths[offset] = length;
    }

    public String getField(int offset) {
        return fields[offsets[offset]];
    }

    public int getFieldLength(int offset) {
        return lengths[offsets[offset]];
    }

    public int getFieldOffset(int offset) {
        return offsets[offset];
    }

    public int getNumFields() {
        return numFields;
    }

    public int getNumFieldsWithData() {
        int numFieldsWithData = 0;
        for (int i = 0; i < numFields; i++) {
            if (lengths[i] > 0) {
                numFieldsWithData++;
            }
        }
        return numFieldsWithData;
    }

    public int getNumFieldsWithDataAndEmptyFields() {
        int numFieldsWithDataAndEmptyFields
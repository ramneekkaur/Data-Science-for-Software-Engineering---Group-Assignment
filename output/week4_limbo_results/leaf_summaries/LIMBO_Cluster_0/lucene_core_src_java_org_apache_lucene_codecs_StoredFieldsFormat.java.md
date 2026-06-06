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

public class StoredFieldsFormat implements Serializable {

    private final String[] fields;
    private final int[] offsets;
    private final int[] lengths;

    public StoredFieldsFormat(int numFields, int numBytesPerField) {
        fields = new String[numFields];
        offsets = new int[numFields + 1];
        lengths = new int[numFields + 1];
        offsets[0] = 0;
        lengths[0] = numBytesPerField;
        for (int i = 1; i < numFields; i++) {
            fields[i] = "";
            lengths[i] = 0;
        }
    }

    public void setField(int fieldIndex, String fieldValue) {
        fields[fieldIndex] = fieldValue;
        lengths[fieldIndex + 1] = lengths[fieldIndex] + fieldValue.length();
        offsets[fieldIndex + 1] = offsets[fieldIndex] + lengths[fieldIndex];
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("StoredFieldsFormat{");
        for (int i = 0; i < numFields; i++) {
            sb.append("\n\t" + fields[i] + ", ");
            sb.append("length=" + lengths[i] + ", ");
            sb.append("offset=" + offsets[i] + ", ");
        }
        sb.append("\n}");
        return sb.toString();
    }

    public int getField(int fieldIndex) {
        return lengths[fieldIndex + 1] - lengths[fieldIndex];
    }

    public int getFieldOffset
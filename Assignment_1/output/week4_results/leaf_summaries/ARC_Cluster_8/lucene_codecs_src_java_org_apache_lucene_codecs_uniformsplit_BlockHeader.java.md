this file to You under the Apache License, Version 2.0
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

public class BlockHeader implements Serializable {
    private final String[] fields;
    private final int[] offsets;
    private final int[] lengths;

    public BlockHeader(String[] fields, int[] offsets, int[] lengths) {
        this.fields = fields;
        this.offsets = offsets;
        this.lengths = lengths;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("BlockHeader{");
        sb.append("\n\tfields=");
        for (int i = 0; i < fields.length; i++) {
            sb.append(fields[i]);
            if (i < fields.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("\n\toffsets=");
        for (int i = 0; i < offsets.length; i++) {
            sb.append(offsets[i]);
            if (i < offsets.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("\n\tlengths=");
        for (int i = 0; i < lengths.length; i++) {
            sb.append(lengths[i]);
            if (i < lengths.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("}");
        return sb.toString();
    }

    public int getField(int fieldIndex) {
        return fields[fieldIndex];
    }

    public int getOffset(int fieldIndex) {
        return offsets[fieldIndex];
    }

    public int getLength(int fieldIndex) {
        return lengths[fieldIndex];
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

public class SimpleTextSegmentInfoFormat implements SegmentInfoFormat {

    private final String[] fields;

    public SimpleTextSegmentInfoFormat(String[] fields) {
        this.fields = fields;
    }

    public String getField(int fieldIndex) {
        return fields[fieldIndex];
    }

    public int getFieldCount() {
        return fields.length;
    }

    public String toString() {
        return fields[0] + ": " + fields[1] + ": " + fields[2] + ": " + fields[3] + ": " + fields[4] + ": " + fields[5] + ": " + fields[6] + ": " + fields[7] + ": " + fields[8] + ": " + fields[9] + ": " + fields[10] + ": " + fields[11] + ": " + fields[12] + ": " + fields[13] + ": " + fields[14] + ": " + fields[15] + ": " + fields[16] + ": " + fields[17] + ": " + fields[18] + ": " + fields[19] + ": " + fields[20] + ": " + fields[21] + ": " + fields[22] + ": " + fields[23] + ": " + fields[24] + ": " + fields[25] + ": " + fields[26] + ": " + fields[27] + ": " + fields[28] + ": " + fields[29] + ": " + fields[30] + ": " + fields[31] + ": " + fields[32] + ": " + fields[33
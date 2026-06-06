licenses this file to You under the Apache License, Version 2.0
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

public class CompoundFormat implements Serializable {
    private final String[] tokens;
    private final int[] offsets;
    private final int[] lengths;
    private final int[] offsets2;
    private final int[] lengths2;

    public CompoundFormat(String[] tokens, int[] offsets, int[] lengths, int[] offsets2, int[] lengths2) {
        this.tokens = tokens;
        this.offsets = offsets;
        this.lengths = lengths;
        this.offsets2 = offsets2;
        this.lengths2 = lengths2;
    }

    public String toString() {
        StringBuffer sb = new StringBuffer();
        sb.append("\t" + "Tokens: " + Arrays.toString(tokens));
        sb.append("\n\t" + "Offsets: " + Arrays.toString(offsets));
        sb.append("\n\t" + "Lengths: " + Arrays.toString(lengths));
        sb.append("\n\t" + "Offsets2: " + Arrays.toString(offsets2));
        sb.append("\n\t" + "Lengths2: " + Arrays.toString(lengths2));
        return sb.toString();
    }

    public int getTokenIndex(String token) {
        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i].equals(token)) {
                return i;
            }
        }
        return -1;
    }

    public int getOffset(String token) {
        for (int i = 0; i < offsets.length; i++) {
            if (tokens[i
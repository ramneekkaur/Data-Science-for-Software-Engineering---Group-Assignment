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

public class SimpleTextFieldsReader implements Serializable {

    private final StringBuilder sb = new StringBuilder();

    public SimpleTextFieldsReader(String fileName) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line = null;
            while ((line = br.readLine()) != null) {
                sb.append(line).append("\n");
            }
        }
    }

    public String toString() {
        return sb.toString();
    }

    public String read() {
        return sb.toString();
    }

    public int readInt() {
        return Integer.parseInt(sb.toString());
    }

    public int readDouble() {
        return Double.parseDouble(sb.toString());
    }

    public int readBoolean() {
        return Boolean.parseBoolean(sb.toString());
    }

    public int readString() {
        return sb.toString().length();
    }

    public int readUTF() {
        return sb.toString().length();
    }

    public int readUTF16() {
        return sb.toString().length();
    }

    public int readUTF32() {
        return sb.toString().length();
    }

    public int readUTF64() {
        return sb.toString().length();
    }

    public int readUTF8() {
        return sb.toString().length();
    }

    public int readUTF16BE() {
        return sb.toString().length();
    }

    public int readUTF16LE() {
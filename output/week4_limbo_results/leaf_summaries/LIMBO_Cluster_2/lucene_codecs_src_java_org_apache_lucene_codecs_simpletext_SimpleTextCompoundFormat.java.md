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

public class SimpleTextCompoundFormat implements Serializable {
    private final String[] lines;
    private final int lineNumber;

    public SimpleTextCompoundFormat(int lineNumber, String[] lines) {
        this.lines = lines;
        this.lineNumber = lineNumber;
    }

    public String toString() {
        return lines[lineNumber];
    }

    public int getLineNumber() {
        return lineNumber;
    }

    public int getLineCount() {
        return lines.length;
    }

    public int getLine(int lineNumber) {
        return lineNumber < lines.length ? lines[lineNumber] : null;
    }

    public int getLineCount(int lineNumber) {
        return lineNumber < lines.length ? 1 : 0;
    }

    public int getLineCount(int lineNumber, int lineLength) {
        return lineNumber < lines.length ? lineLength
                + lineNumber - 1
                + lines.length - lineNumber
                + 1
                : 0;
    }

    public int getLineCount(int lineNumber, int lineLength) {
        return lineNumber < lines.length ? lineLength
                + lineNumber - 1
                + lines.length - lineNumber
                + 1
                : 0;
    }

    public int getLineCount(int lineNumber, int lineLength) {
        return lineNumber < lines.length ? lineLength
                + lineNumber - 1
                + lines.length - lineNumber
                + 1
                : 0;
    }

    public int getLineCount(int lineNumber, int lineLength) {
        return lineNumber < lines.length ? lineLength
                + lineNumber - 1
The ASF licenses this file to You under the Apache License, Version 2.0
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

public class SimpleTextDocValuesWriter implements Serializable {

    private final StringBuilder sb = new StringBuilder();

    public SimpleTextDocValuesWriter(StringBuilder sb) {
        this.sb = sb;
    }

    public void write(Document doc) {
        sb.append("\n\n");
        sb.append("SimpleTextDocValuesWriter\n");
        sb.append("\n\n");
        sb.append("Inputs: ");
        for (String input : doc.getInputs()) {
            sb.append(input + ", ");
        }
        sb.append("\n\n");
        sb.append("Outputs: ");
        for (String output : doc.getOutputs()) {
            sb.append(output + ", ");
        }
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n\n");
        sb.append("\n
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

public class SimpleTextDocValuesWriter implements Serializable {

    private final StringBuilder sb = new StringBuilder();

    public SimpleTextDocValuesWriter(StringBuilder sb) {
        this.sb = sb;
    }

    public void write(Document doc) {
        sb.append("SimpleTextDocValuesWriter\n");
        sb.append("\tInputs:\n");
        for (String input : doc.getInputs()) {
            sb.append("\t\t" + input + "\n");
        }
        sb.append("\tOutputs:\n");
        for (String output : doc.getOutputs()) {
            sb.append("\t\t" + output + "\n");
        }
        sb.append("\tCore logic:\n");
        for (String line : doc.getCoreLogic()) {
            sb.append("\t\t" + line + "\n");
        }
        sb.append("\tInternal and external dependencies:\n");
        for (String dep : doc.getInternalAndExternalDependencies()) {
            sb.append("\t\t" + dep + "\n");
        }
        sb.append("\tArchitectural role inside the cluster:\n");
        sb.append("\t\t" + doc.getArchitecturalRole() + "\n");
        sb.append("\tImportant classes/methods:\n");
        for (String line : doc.getImportantClassesAndMethods()) {
            sb.append("\t\t" + line + "\n");
        }
    }

    public String toString() {
        return sb.toString();
    }
}
``
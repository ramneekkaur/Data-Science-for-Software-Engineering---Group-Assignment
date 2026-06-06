The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

public class SimpleTextNormsFormat implements Serializable {

    private final String text;
    private final String normalizedText;

    public SimpleTextNormsFormat(String text) {
        this.text = text;
        normalizedText = normalize(text);
    }

    public String getText() {
        return text;
    }

    public String getNormalizedText() {
        return normalizedText;
    }

    public String normalize(String text) {
        String normalizedText = "";
        if (text.length() > 0) {
            normalizedText = text.toLowerCase();
            normalizedText = normalize(normalizedText);
        }
        return normalizedText;
    }

    public static String normalize(String text) {
        if (text.length() > 0) {
            text = text.toLowerCase();
            text = text.replace("'", "''");
            text = text.replace("-", "--");
            text = text.replace(".", " . ");
            text = text.replace(",", " , ");
            text = text.replace("(", " ( ");
            text = text.replace(")", " ) ");
            text = text.replace("[", " [ ");
            text = text.replace("]", " ] ");
            text = text.replace("{", " { ");
            text = text.replace("}", " } ");
            text = text.replace("\\", " \\ ");
            text = text.replace("/", " / ");
            text = text.replace("\n", " \n ");
            text = text.replace("\r", " \r ");
            text = text.replace("\
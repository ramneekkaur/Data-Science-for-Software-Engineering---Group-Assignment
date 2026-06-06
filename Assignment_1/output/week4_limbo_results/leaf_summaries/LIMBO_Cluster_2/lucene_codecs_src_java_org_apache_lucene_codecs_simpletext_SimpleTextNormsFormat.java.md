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

public class SimpleTextNormsFormat implements Serializable {

    private final String[] normalizationRules;

    public SimpleTextNormsFormat(String[] normalizationRules) {
        this.normalizationRules = normalizationRules;
    }

    public String toString() {
        return normalizationRules[0];
    }

    public static SimpleTextNormsFormat fromString(String normalizationRule) {
        return new SimpleTextNormsFormat(Arrays.asList(normalizationRule.split("\\s*,\\s*")));
    }

    public static SimpleTextNormsFormat fromFile(File file) {
        return new SimpleTextNormsFormat(Files.readAllLines(file.toFile()));
    }

    public static SimpleTextNormsFormat fromStringList(String[] normalizationRuleList) {
        return new SimpleTextNormsFormat(Arrays.asList(normalizationRuleList));
    }

    public static SimpleTextNormsFormat fromFileList(File[] fileList) {
        return new SimpleTextNormsFormat(Files.readAllLines(fileList));
    }

    public static SimpleTextNormsFormat fromStringList(String[] normalizationRuleList) {
        return new SimpleTextNormsFormat(Arrays.asList(normalizationRuleList));
    }

    public static SimpleTextNormsFormat fromFileList(File[] fileList) {
        return new SimpleTextNormsFormat(Files.readAllLines(fileList));
    }

    public static SimpleTextNormsFormat fromStringList(String[] normalizationRuleList) {
        return new SimpleTextNormsFormat(Arrays.asList(normalizationRuleList));
    }

    public static SimpleTextNorms
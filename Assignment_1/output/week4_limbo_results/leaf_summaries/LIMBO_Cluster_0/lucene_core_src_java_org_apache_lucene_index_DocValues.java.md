* You may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

public class DocValues {
    /**
     * @param doc
     *            Document to be indexed
     * @param index
     *            Index to be indexed
     * @param field
     *            Field to be indexed
     * @param value
     *            Value to be indexed
     * @param field_type
     *            Field type
     */
    public void index(Document doc, Index index, String field, String value,
            FieldType fieldType) {
        if (fieldType == FieldType.TEXT) {
            index.add(doc.get(field), value);
        } else if (fieldType == FieldType.DATE) {
            index.add(doc.get(field), new Date(value));
        } else if (fieldType == FieldType.NUMBER) {
            index.add(doc.get(field), new Double(value));
        } else if (fieldType == FieldType.BOOLEAN) {
            index.add(doc.get(field), new Boolean(value));
        } else if (fieldType == FieldType.DICT) {
            index.add(doc.get(field), new Dict(value));
        } else if (fieldType == FieldType.LIST) {
            index.add(doc.get(field), new List(value));
        } else if (fieldType == FieldType.MAP) {
            index.add(doc.get(field), new Map(value));
        } else if (fieldType == FieldType.STRING) {
            index.add(doc.get(field), new String(value));
        } else if (fieldType == FieldType.DATE_DICT) {
            index.add(doc.get(field), new DateDict(value));
        } else if (fieldType == FieldType.DATE_LIST) {
            index.add
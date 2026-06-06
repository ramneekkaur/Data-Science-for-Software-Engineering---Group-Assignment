You under the Apache License, Version 2.0
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

public class DocValuesType implements DocValues {
    /**
     * The DocValuesType class represents a single document value.
     *
     * @param doc
     *            The document value.
     * @param docId
     *            The document value's id.
     * @param docType
     *            The document value's type.
     * @param docValue
     *            The document value's value.
     */
    public DocValuesType(Document doc, int docId, String docType, Object docValue) {
        this.doc = doc;
        this.docId = docId;
        this.docType = docType;
        this.docValue = docValue;
    }

    /**
     * The doc value.
     */
    public Object doc {
        @Override
        public Object getDoc() {
            return doc;
        }

        @Override
        public Object setDoc(Object doc) {
            this.doc = doc;
            return this;
        }

        @Override
        public Object getDocId() {
            return docId;
        }

        @Override
        public Object setDocId(Object docId) {
            this.docId = docId;
            return this;
        }

        @Override
        public String getDocType() {
            return docType;
        }

        @Override
        public Object setDocType(String docType) {
            this.docType = docType;
            return this;
        }

        @Override
        public Object getDocValue() {
            return docValue;
        }

        @Override
        public Object setDocValue(Object docValue) {
            this.docValue = docValue;
            return this;
        }

        @Override
        public String
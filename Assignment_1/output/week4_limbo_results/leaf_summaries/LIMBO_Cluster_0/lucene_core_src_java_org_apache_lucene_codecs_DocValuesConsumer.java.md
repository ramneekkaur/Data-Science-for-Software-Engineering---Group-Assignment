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

public class DocValuesConsumer implements DocValuesConsumer {

    public void process(DocValues docValues) {
        System.out.println("Processing DocValues: " + docValues);
    }

    public void process(String docId, String docType, String docText) {
        System.out.println("Processing DocId: " + docId + ", DocType: " + docType + ", DocText: " + docText);
    }

    public void process(String docId, String docType, String docText, String docTags) {
        System.out.println("Processing DocId: " + docId + ", DocType: " + docType + ", DocText: " + docText + ", DocTags: " + docTags);
    }

    public void process(String docId, String docType, String docText, String docTags, String docTags2) {
        System.out.println("Processing DocId: " + docId + ", DocType: " + docType + ", DocText: " + docText + ", DocTags: " + docTags + ", DocTags2: " + docTags2);
    }

    public void process(String docId, String docType, String docText, String docTags, String docTags2, String docTags3) {
        System.out.println("Processing DocId: " + docId + ", DocType: " + docType + ", DocText: " + docText + ", DocTags: " + docTags + ", DocTags2: " + docTags2 + ", DocTags3: " + docTags3);
    }

    public void process(String docId, String docType, String docText, String docTags, String docTags2, String docTags3, String docTags4) {
        System.out.
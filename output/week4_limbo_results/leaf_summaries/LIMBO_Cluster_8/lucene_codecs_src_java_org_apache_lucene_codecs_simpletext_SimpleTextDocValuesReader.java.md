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

public class SimpleTextDocValuesReader implements
    SimpleTextDocValuesReader {

    /**
     * @param doc
     *            the document to read
     * @return
     *            the values of the document
     */
    public static <T> T[] read(Document doc) {
        return doc.getValues();
    }

    /**
     * @param doc
     *            the document to read
     * @return
     *            the values of the document
     */
    public static <T> T[] read(DocumentValues doc) {
        return doc.getValues();
    }

    /**
     * @param doc
     *            the document to read
     * @return
     *            the values of the document
     */
    public static <T> T[] read(DocumentValuesValues doc) {
        return doc.getValues();
    }

    /**
     * @param doc
     *            the document to read
     * @return
     *            the values of the document
     */
    public static <T> T[] read(DocumentValuesValuesValues doc) {
        return doc.getValues();
    }

    /**
     * @param doc
     *            the document to read
     * @return
     *            the values of the document
     */
    public static <T> T[] read(DocumentValuesValuesValuesValues doc) {
        return doc.getValues();
    }

    /**
     * @param doc
     *            the document to read
     * @return
     *            the values of the document
     */
    public static <T> T[] read(DocumentValuesValuesValuesValuesValues doc) {
        return doc.getValues();
    }
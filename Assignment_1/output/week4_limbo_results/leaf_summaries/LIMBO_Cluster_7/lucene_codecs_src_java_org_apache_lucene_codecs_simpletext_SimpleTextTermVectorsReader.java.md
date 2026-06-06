distributed with
 * this work for additional information regarding copyright ownership.
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

public class SimpleTextTermVectorsReader implements
    SimpleTextTermVectorsReader {

    /**
     * @param input
     *            the input file
     */
    private final FileInputStream input;

    /**
     * @param term_vector_file
     *            the term vector file
     */
    private final File termVectorFile;

    /**
     * @param term_vector_format
     *            the term vector format
     */
    private final String termVectorFormat;

    /**
     * @param term_vector_type
     *            the term vector type
     */
    private final String termVectorType;

    /**
     * @param term_vector_field_separator
     *            the term vector field separator
     */
    private final String termVectorFieldSeparator;

    /**
     * @param term_vector_field_delimiter
     *            the term vector field delimiter
     */
    private final String termVectorFieldDelimiter;

    /**
     * @param term_vector_field_quoting
     *            the term vector field quoting
     */
    private final String termVectorFieldQuoting;

    /**
     * @param term_vector_field_quoting_mode
     *            the term vector field quoting mode
     */
    private final String termVectorFieldQuotingMode;

    /**
     * @param term_vector_field_quoting_options
     *            the term vector field quoting options
     */
    private final String termVectorFieldQuotingOptions;

    /**
     * @param term_vector_field_quoting_options
     *            the term vector field quoting options
     */
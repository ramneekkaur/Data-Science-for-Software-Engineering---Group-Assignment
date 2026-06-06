additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

public class OrdIntersectTermsEnum {

    /**
     * @param terms
     * @param order
     * @return
     */
    public static OrdIntersectTermsEnum(Set<String> terms, int order) {
        if (terms == null) {
            throw new IllegalArgumentException("terms cannot be null");
        }
        if (order < 0) {
            throw new IllegalArgumentException("order must be >= 0");
        }
        if (order == 0) {
            return new OrdIntersectTermsEnum();
        }
        if (order == 1) {
            return new OrdIntersectTermsEnum(terms);
        }
        if (order == 2) {
            return new OrdIntersectTermsEnum(terms, terms);
        }
        if (order == 3) {
            return new OrdIntersectTermsEnum(terms, terms, terms);
        }
        if (order == 4) {
            return new OrdIntersectTermsEnum(terms, terms, terms, terms);
        }
        if (order == 5) {
            return new OrdIntersectTermsEnum(terms, terms, terms, terms, terms);
        }
        if (order == 6) {
            return new OrdIntersectTermsEnum(terms, terms, terms, terms, terms, terms);
        }
        if (order == 7) {
            return new OrdIntersectTermsEnum(terms, terms, terms, terms, terms, terms, terms, terms);
        }
        if (order == 8) {
            return new OrdIntersectTermsEnum(terms, terms, terms, terms, terms, terms, terms, terms, terms
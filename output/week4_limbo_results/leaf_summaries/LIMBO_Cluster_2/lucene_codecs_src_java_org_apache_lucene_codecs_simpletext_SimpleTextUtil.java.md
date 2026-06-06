for additional information regarding copyright ownership.
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

public class SimpleTextUtil {
    public static String toUpperCase(String s) {
        return s.toUpperCase();
    }

    public static String toLowerCase(String s) {
        return s.toLowerCase();
    }

    public static String toTitleCase(String s) {
        return s.toUpperCase().substring(0, 1).toLowerCase() + s.substring(1);
    }

    public static String toUpperCaseFirstLetter(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }

    public static String toUpperCaseFirstLetterAndAfterSpace(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }

    public static String toUpperCaseFirstLetterAndAfterComma(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }

    public static String toUpperCaseFirstLetterAndAfterColon(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }

    public static String toUpperCaseFirstLetterAndAfterSemicolon(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }

    public static String toUpperCaseFirstLetterAndAfterQuestionMark(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }

    public static String to
* you under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
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

public class StringHelper {
    public static String toUpperCase(String s) {
        return s.toUpperCase();
    }

    public static String toLowerCase(String s) {
        return s.toLowerCase();
    }

    public static String capitalize(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }

    public static String trim(String s) {
        return s.trim();
    }

    public static String replace(String s, String old, String new) {
        return s.replace(old, new);
    }

    public static String replaceAll(String s, String old, String new) {
        return s.replaceAll(old, new);
    }

    public static String replaceFirst(String s, String old, String new) {
        return s.replaceFirst(old, new);
    }

    public static String replaceLast(String s, String old, String new) {
        return s.replaceLast(old, new);
    }

    public static String replaceFirstOrLast(String s, String old, String new) {
        return s.replaceFirstOrLast(old, new);
    }

    public static String remove(String s, String old) {
        return s.replace(old, "");
    }

    public static String removeAll(String s, String old) {
        return s.replaceAll(old, "");
    }

    public static String removeFirst(String s, String old) {
        return s.replaceFirst(old, "");
    }

    public static String removeLast(String s, String old) {
        return s.replaceLast(old, "");
    }

    public static String removeFirst
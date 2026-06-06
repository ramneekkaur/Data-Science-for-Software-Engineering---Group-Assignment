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

public class ArrayUtil {
    public static <T> T[] toArray(T[] a) {
        if (a == null) {
            return null;
        }
        if (a.length == 0) {
            return a;
        }
        T[] result = (T[]) Array.newInstance(a.getClass().getComponentType(), a.length);
        for (int i = 0; i < a.length; i++) {
            result[i] = a[i];
        }
        return result;
    }

    public static <T> T[] toArray(T[] a, int start, int end) {
        if (a == null) {
            return null;
        }
        if (start < 0 || end < 0 || start > a.length || end > a.length) {
            throw new IndexOutOfBoundsException();
        }
        T[] result = (T[]) Array.newInstance(a.getClass().getComponentType(), end - start);
        for (int i = start; i < end; i++) {
            result[i - start] = a[i];
        }
        return result;
    }

    public static <T> T[] toArray(T[] a, int start, int end, T[] b) {
        if (a == null) {
            return null;
        }
        if (start < 0 || end < 0 || start > a.length || end > a.length) {
            throw new IndexOutOfBoundsException();
        }
        if (b == null) {
            b = (T[]) Array.newInstance(a.getClass().getComponentType(), a.length);
        }
        for (int i = start; i < end; i++)
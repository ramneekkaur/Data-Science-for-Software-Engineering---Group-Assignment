file to You under the Apache License, Version 2.0
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

public class CharsRefBuilder {
    private final StringBuilder sb;
    private final int count;
    private final int start;
    private final int end;

    public CharsRefBuilder(int count, int start, int end) {
        sb = new StringBuilder(count);
        this.count = count;
        this.start = start;
        this.end = end;
    }

    public CharsRefBuilder(String s) {
        sb = new StringBuilder(s.length());
        sb.append(s);
        this.count = s.length();
        this.start = 0;
        this.end = s.length();
    }

    public CharsRefBuilder(String s, int start, int end) {
        sb = new StringBuilder(s.length());
        sb.append(s);
        this.count = s.length();
        this.start = start;
        this.end = end;
    }

    public CharsRefBuilder(String s, int start, int end, int count) {
        sb = new StringBuilder(s.length());
        sb.append(s);
        this.count = count;
        this.start = start;
        this.end = end;
    }

    public String toString() {
        return sb.substring(start, end);
    }

    public int length() {
        return end - start;
    }

    public int getStart() {
        return start;
    }

    public int getEnd() {
        return end;
    }

    public int getCount() {
        return count;
    }

    public int getCharAt(int index) {
        return sb.charAt(index);
    }

    public
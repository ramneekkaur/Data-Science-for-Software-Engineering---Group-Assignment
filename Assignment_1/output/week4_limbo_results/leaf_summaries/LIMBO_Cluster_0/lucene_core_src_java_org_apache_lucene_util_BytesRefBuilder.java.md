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

public class BytesRefBuilder {
    private final byte[] buf;
    private final int len;
    private final int start;
    private final int end;

    public BytesRefBuilder(byte[] buf, int len, int start, int end) {
        this.buf = buf;
        this.len = len;
        this.start = start;
        this.end = end;
    }

    public byte[] getBytes() {
        return buf;
    }

    public int getLength() {
        return len;
    }

    public int getStart() {
        return start;
    }

    public int getEnd() {
        return end;
    }

    public BytesRefBuilder copy(int start, int end) {
        return new BytesRefBuilder(buf, len, start, end);
    }

    public BytesRefBuilder copy(byte[] buf, int len, int start, int end) {
        return new BytesRefBuilder(buf, len, start, end);
    }

    public BytesRefBuilder copy(int start, int end) {
        return new BytesRefBuilder(buf, len, start, end);
    }

    public BytesRefBuilder copy(byte[] buf, int len, int start, int end) {
        return new BytesRefBuilder(buf, len, start, end);
    }

    public BytesRefBuilder copy(int start, int end) {
        return new BytesRefBuilder(buf, len, start, end);
    }

    public BytesRefBuilder copy(byte[] buf, int len, int start, int end) {
        return new BytesRefBuilder(buf, len, start, end);
    }

    public BytesRefBuilder copy(int start, int end)
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

public class Impact implements java.io.FileInputStream {
    private static final int BUFFER_SIZE = 1024;
    private static final int BUFFER_SIZE_IN_BYTES = BUFFER_SIZE * 1;

    public Impact(FileInputStream f) {
        this.f = f;
    }

    public void read(byte[] buf, int off, int len) {
        int bytesRead = 0;
        while (bytesRead < len) {
            int bytesRead = f.read(buf, off, len - bytesRead);
            if (bytesRead == 0) {
                break;
            }
            off += bytesRead;
        }
    }

    public int read(byte[] buf, int off, int len) {
        int bytesRead = 0;
        while (bytesRead < len) {
            int bytesRead = f.read(buf, off, len - bytesRead);
            if (bytesRead == 0) {
                break;
            }
            off += bytesRead;
        }
        return bytesRead;
    }

    public int read(byte[] buf, int off, int len) {
        int bytesRead = 0;
        while (bytesRead < len) {
            int bytesRead = f.read(buf, off, len - bytesRead);
            if (bytesRead == 0) {
                break;
            }
            off += bytesRead;
        }
        return bytesRead;
    }

    public int read(byte[] buf, int off, int len) {
        int bytesRead = 0;
        while (bytesRead < len) {
            int bytesRead = f.read(buf, off, len - bytesRead);
            if (bytesRead == 0) {
                break;
            }
            off +=
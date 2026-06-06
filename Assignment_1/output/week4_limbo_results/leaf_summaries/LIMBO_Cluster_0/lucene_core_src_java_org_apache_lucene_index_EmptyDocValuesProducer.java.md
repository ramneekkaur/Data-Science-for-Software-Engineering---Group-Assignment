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

public class EmptyDocValuesProducer implements
    java.io.FileWriter {
    private final int BUFFER_SIZE = 1024;
    private final int BUFFER_SIZE_IN_BYTES = BUFFER_SIZE * 1024;

    public void write(Object[] values) {
        int count = 0;
        for (Object value : values) {
            if (value == null) {
                continue;
            }
            count++;
            try {
                write(value);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (count > 0) {
            try {
                write(new String(new char[count]).replace('\0', '\n'));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public void write(Object value) {
        try {
            write(value.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void write(byte[] value) {
        try {
            write(new String(value));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void write(byte[] value) {
        try {
            write(new String(value));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void write(byte[] value) {
        try {
            write(new String(value));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void write(byte[] value) {
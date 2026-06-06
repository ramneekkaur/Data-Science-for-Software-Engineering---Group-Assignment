ownership.
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

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;

public class FSTOrdsOutputs {

    private static final int MAX_LINE_LENGTH = 1024;

    public static void main(String[] args) throws FileNotFoundException, IOException {
        File file = new File("/tmp/fstords.java");
        try (InputStream is = new FileInputStream(file);
             OutputStream os = new FileOutputStream("/tmp/fstords.java")) {
            List<String> lines = new ArrayList<>();
            while ((line = is.readLine()) != null) {
                if (line.length() > MAX_LINE_LENGTH) {
                    lines.add(line.substring(0, MAX_LINE_LENGTH) + "...");
                } else {
                    lines.add(line);
                }
            }
            os.write(lines.toString().getBytes());
        }
    }
}
```
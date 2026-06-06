this file to You under the Apache License, Version 2.0
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
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class BlockLine {

    private static final int BLOCK_SIZE = 1024;

    public static void main(String[] args) throws FileNotFoundException, IOException {
        File file = new File("/path/to/file");
        FileInputStream fis = new FileInputStream(file);
        FileOutputStream fos = new FileOutputStream("/path/to/output");
        FileReader fr = new FileReader(file);
        List<String> lines = new ArrayList<String>();
        while ((lines = fr.readLine()) != null) {
            fos.write(lines.toString().getBytes());
        }
        fis.close();
        fr.close();
        fos.close();
    }
}
```
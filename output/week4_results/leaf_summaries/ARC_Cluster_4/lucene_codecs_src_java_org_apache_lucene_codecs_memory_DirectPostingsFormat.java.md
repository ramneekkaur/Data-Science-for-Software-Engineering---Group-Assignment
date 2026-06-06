this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;

public class DirectPostingsFormat {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        File file = new File("lucene/codecs/src/java/org/apache/lucene/codecs/memory/DirectPostingsFormat.java");
        try {
            InputStream is = new FileInputStream(file);
            OutputStream os = new FileOutputStream(file);
            byte[] data = new byte[1024];
            int count = 0;
            while ((count = is.read(data)) > 0) {
                os.write(data, 0, count);
            }
            is.close();
            os.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

```
File title: org.apache.lucene.codecs.memory.DirectPostingsFormat
Key functionality: Computes a DirectPostingsFormat for a given input file.
Core logic: Reads the input file and writes the output file.
Inputs and outputs: Input file, output file.
Internal and external dependencies: No dependencies.
Architectural role inside the cluster: Input file is read and output file is written.
Important classes/methods: DirectPostingsFormat, File, InputStream, OutputStream, byte[]
```
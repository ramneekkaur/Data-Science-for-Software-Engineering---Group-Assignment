The ASF licenses this file to You under the Apache License, Version 2.0
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
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class IntersectBlockReader {

    private static final int BLOCK_SIZE = 4096;

    public static void main(String[] args) throws FileNotFoundException, IOException {
        File file = new File("intersect_block_reader.txt");
        FileReader fileReader = new FileReader(file);
        byte[] buffer = new byte[BLOCK_SIZE];
        int blockNumber = 0;
        int blockStart = 0;
        int blockEnd = 0;
        int blockSize = 0;
        int blockCount = 0;
        List<String> lines = new ArrayList<String>();
        while ((blockStart = fileReader.read(buffer)) != -1) {
            blockEnd = blockStart + BLOCK_SIZE;
            if (blockEnd > file.length()) {
                blockEnd = file.length();
            }
            String line = new String(buffer, 0, blockEnd - blockStart);
            if (line.length() > 0) {
                lines.add(line);
            }
            blockCount++;
            if (blockCount % 100 == 0) {
                System.out.println("Processed " + blockCount + " blocks");
            }
        }
        fileReader.close();
        System.out.println("Processed " + blockCount + " blocks");
        for (String line : lines) {
            System.out.println(line);
        }
    }
}
```

```
1. File title: IntersectBlockReader
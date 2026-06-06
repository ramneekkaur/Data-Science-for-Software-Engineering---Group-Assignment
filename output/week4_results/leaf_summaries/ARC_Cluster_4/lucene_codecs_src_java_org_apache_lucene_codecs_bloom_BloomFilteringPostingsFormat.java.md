* The ASF licenses this file to You under the Apache License, Version 2.0
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
import java.util.ArrayList;
import java.util.List;

public class BloomFilteringPostingsFormat {

    private static final int BLOOM_FILTER_SIZE = 1000000;
    private static final int BLOOM_FILTER_HASH_COUNT = 100;

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("bloomfilteringpostingsformat.java");
        try {
            FileInputStream fstream = new FileInputStream(file);
            DataInputStream in = new DataInputStream(fstream);
            byte[] inputData = new byte[in.available()];
            in.readFully(inputData);
            in.close();
            in = new DataInputStream(new FileInputStream(file));
            byte[] outputData = new byte[BLOOM_FILTER_SIZE];
            boolean[] bloomFilter = new boolean[BLOOM_FILTER_SIZE];
            for (int i = 0; i < BLOOM_FILTER_HASH_COUNT; i++) {
                in.readFully(outputData);
                for (int j = 0; j < BLOOM_FILTER_SIZE; j++) {
                    bloomFilter[j] = (byte) (outputData[j] & 0xFF);
                }
            }
            in.close();
            System.out.println("Bloom Filtering Postings Format successfully loaded.");
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }
    }
}
```

```
File title: org.apache
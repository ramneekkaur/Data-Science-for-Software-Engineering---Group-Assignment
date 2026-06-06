for additional information regarding copyright ownership.
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
import java.util.Scanner;

public class BlockTermsReader {

    private static final int BLOCK_TERM_SIZE = 1024;
    private static final int BLOCK_TERM_COUNT = 1024;
    private static final int BLOCK_TERM_COUNT_IN_BLOCK = BLOCK_TERM_COUNT / BLOCK_TERM_SIZE;

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("lucene/codecs/src/java/org/apache/lucene/codecs/blockterms/BlockTermsReader.java");
        Scanner scanner = new Scanner(file);
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.startsWith("public static void main(String[] args)")
                    && line.endsWith("}")) {
                StringBuilder sb = new StringBuilder();
                sb.append("File title: ");
                sb.append(line);
                System.out.println(sb.toString());
            }
        }
        scanner.close();
    }
}
```
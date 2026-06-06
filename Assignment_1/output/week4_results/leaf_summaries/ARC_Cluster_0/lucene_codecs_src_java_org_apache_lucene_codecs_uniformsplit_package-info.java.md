F licenses this file to You under the Apache License, Version 2.0
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

package-info;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class PackageInfo {

    private static final String FILE_NAME = "package-info.java";

    public static void main(String[] args) throws FileNotFoundException, IOException {
        List<String> lines = new ArrayList<String>();
        File file = new File(FILE_NAME);
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line = null;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
        }
        System.out.println("File title: " + lines.get(0));
        System.out.println("Key functionality: " + lines.get(1));
        System.out.println("Core logic: " + lines.get(2));
        System.out.println("Inputs and outputs: " + lines.get(3));
        System.out.println("Internal and external dependencies: " + lines.get(4));
        System.out.println("Architectural role inside the cluster: " + lines.get(5));
        System.out.println("Important classes/methods: " + lines.get(6));
    }
}
```

```
File title: org.apache.lucene.codecs.uniformsplit.package-info
Key functionality: This class provides a uniform split of a file into a list of lines.
Core logic: public static List<String> split(File file) {
    List<String> lines = new ArrayList<
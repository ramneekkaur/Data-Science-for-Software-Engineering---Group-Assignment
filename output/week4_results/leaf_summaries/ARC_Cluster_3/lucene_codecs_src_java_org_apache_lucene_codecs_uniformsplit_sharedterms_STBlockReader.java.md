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
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class STBlockReader {

    private static final int BLOCK_SIZE = 1024;

    public static void main(String[] args) throws FileNotFoundException, IOException {
        File file = new File("/path/to/file");
        List<String> lines = new ArrayList<String>();
        try {
            FileInputStream fstream = new FileInputStream(file);
            BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
            String line = "";
            while ((line = br.readLine()) != null) {
                lines.add(line);
            }
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        STBlockReader reader = new STBlockReader(lines);
        System.out.println(reader.getTitle());
        System.out.println(reader.getKeyFunctionality());
        System.out.println(reader.getCoreLogic());
        System.out.println(reader.getInputsAndOutputs());
        System.out.println(reader.getInternalAndExternalDependencies());
        System.out.println(reader.getArchitecturalRoleInsideTheCluster());
        System.out.println(reader.getImportantClassesAndMethods());
    }

    private String getTitle() {
        return "STBlockReader";
    }

    private String getKeyFunctionality() {
        return "Reads a file and returns a list of lines.";
    }

    private String
regarding copyright ownership.
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
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class OrdBlockTreeTermsReader {

    private static final String INPUT_FILE_PATH = "input.txt";

    public static void main(String[] args) {
        try {
            File file = new File(INPUT_FILE_PATH);
            FileReader fileReader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            List<String> lines = new ArrayList<String>();
            String line = null;
            while ((line = bufferedReader.readLine()) != null) {
                lines.add(line);
            }

            List<String> terms = new ArrayList<String>();
            for (String line : lines) {
                terms.add(line);
            }

            System.out.println("File title: " + file.getAbsoluteFile());
            System.out.println("Key functionality: " + terms.size());
            System.out.println("Core logic: " + terms.get(0));
            System.out.println("Inputs and outputs: " + terms.get(1));
            System.out.println("Internal and external dependencies: " + terms.get(2));
            System.out.println("Architectural role inside the cluster: " + terms.get(3));
            System.out.println("Important classes/methods: " + terms.get(4));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
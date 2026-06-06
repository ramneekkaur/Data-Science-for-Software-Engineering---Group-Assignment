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
import java.util.ArrayList;
import java.util.List;

public class OrdFieldReader {

    private static final String INPUT_FILE_PATH = "input.txt";
    private static final String OUTPUT_FILE_PATH = "output.txt";

    public static void main(String[] args) throws FileNotFoundException {
        // TODO Auto-generated method stub

        // Read the input file
        List<String> lines = readLines(INPUT_FILE_PATH);

        // Process the lines
        List<OrdField> fields = processLines(lines);

        // Write the output file
        writeLines(OUTPUT_FILE_PATH, fields);
    }

    private static List<String> readLines(String filePath) throws FileNotFoundException {
        List<String> lines = new ArrayList<>();
        try (File file = new File(filePath)) {
            FileInputStream fstream = new FileInputStream(file);
            BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
            String line = br.readLine();
            while (line != null) {
                lines.add(line);
                line = br.readLine();
            }
            br.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return lines;
    }

    private static List<OrdField> processLines(List<String> lines) {
        List<OrdField> fields = new ArrayList<>();
        for (String line : lines) {
            OrdField field = processLine(line);
            if (field !=
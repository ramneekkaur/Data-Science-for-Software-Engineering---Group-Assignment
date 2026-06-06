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
import java.util.HashMap;
import java.util.Map;

public class TermsIndexReaderBase {

    private static final String INPUT_FILE_NAME = "terms.txt";
    private static final String OUTPUT_FILE_NAME = "terms.json";

    private static final Map<String, String> TERMS_MAP = new HashMap<>();

    public static void main(String[] args) throws FileNotFoundException {
        try {
            // Read terms from file
            File file = new File(INPUT_FILE_NAME);
            FileReader fileReader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            // Read terms from file
            String line = bufferedReader.readLine();
            while (line != null) {
                String[] terms = line.split("\\s+");
                for (String term : terms) {
                    TERMS_MAP.put(term, term);
                }
                line = bufferedReader.readLine();
            }

            // Write terms to file
            File fileWriter = new File(OUTPUT_FILE_NAME);
            FileWriter fileWriter = new FileWriter(fileWriter);
            FileWriter fileWriter = new FileWriter(fileWriter);
            try {
                // Write terms to file
                for (String term : TERMS_MAP.keySet()) {
                    fileWriter.write(term + ",");
                }
                fileWriter.write("\n");
            } catch (IOException e) {
                e.printStackTrace();
            }
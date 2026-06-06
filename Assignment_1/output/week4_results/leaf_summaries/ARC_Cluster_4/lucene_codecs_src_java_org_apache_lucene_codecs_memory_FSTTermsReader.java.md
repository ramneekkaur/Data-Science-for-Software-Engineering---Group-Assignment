F licenses this file to You under the Apache License, Version 2.0
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

public class FSTTermsReader {

    private static final String INPUT_FILE_PATH = "input.txt";
    private static final String OUTPUT_FILE_PATH = "output.txt";

    public static void main(String[] args) {
        try {
            File inputFile = new File(INPUT_FILE_PATH);
            FileOutputStream outputStream = new FileOutputStream(OUTPUT_FILE_PATH);
            FileInputStream inputStream = new FileInputStream(inputFile);
            InputStreamReader inputReader = new InputStreamReader(inputStream);
            BufferedReader bufferedReader = new BufferedReader(inputReader);

            List<String> lines = new ArrayList<String>();
            String line = bufferedReader.readLine();
            while (line != null) {
                lines.add(line);
                line = bufferedReader.readLine();
            }

            List<String> terms = new ArrayList<String>();
            for (String line : lines) {
                terms.add(line);
            }

            FSTTermsReader fstTermsReader = new FSTTermsReader();
            fstTermsReader.processTerms(terms);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                outputStream.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private void processTerms(List<String
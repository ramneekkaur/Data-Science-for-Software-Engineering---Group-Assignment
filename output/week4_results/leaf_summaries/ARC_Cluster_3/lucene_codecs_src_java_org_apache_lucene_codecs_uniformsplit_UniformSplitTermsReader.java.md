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
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class UniformSplitTermsReader implements
    java.io.FileReader {

    private static final String INPUT_FILE_PATH = "input.txt";
    private static final String OUTPUT_FILE_PATH = "output.txt";

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        // Create a new instance of the UniformSplitTermsReader class
        UniformSplitTermsReader reader = new UniformSplitTermsReader();

        // Read the input file
        try (BufferedReader inputFile = new BufferedReader(new FileReader(INPUT_FILE_PATH))
                ) {
            // Create an ArrayList to store the terms
            List<String> terms = new ArrayList<>();

            // Read each line of the input file
            String line = inputFile.readLine();
            while (line != null) {
                // Split the line into terms
                String[] termsInLine = line.split("\\s+");

                // Add each term to the list
                for (String term : termsInLine) {
                    terms.add(term);
                }

                // Read the next line
                line = inputFile.readLine();
            }

            // Write the terms to the output file
            try (BufferedWriter outputFile = new BufferedWriter(new FileWriter(OUTPUT_FILE_PATH))
                    ) {
                // Write the number of terms
                outputFile.write(terms.size() + "\n");
additional information regarding copyright ownership.
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

public class UnionFieldMetadataBuilder {

    private static final String INPUT_FILE_PATH = "input.txt";
    private static final String OUTPUT_FILE_PATH = "output.txt";

    public static void main(String[] args) {
        try {
            // Read input file
            FileReader fileReader = new FileReader(INPUT_FILE_PATH);
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            // Create a list to store the input lines
            List<String> inputLines = new ArrayList<>();

            // Read each line from the input file
            String line = bufferedReader.readLine();
            while (line != null) {
                inputLines.add(line);
                line = bufferedReader.readLine();
            }

            // Close the input file
            bufferedReader.close();

            // Create a list to store the output lines
            List<String> outputLines = new ArrayList<>();

            // Process each input line
            for (String line : inputLines) {
                // Parse the input line
                String[] tokens = line.split("\\s+");

                // Create a new output line
                StringBuilder outputLine = new StringBuilder();

                // Add the file title
                outputLine.append("File title: ");
                outputLine.append(tokens[0]);

                // Add the key functionality
                outputLine.append("\nKey functionality: ");
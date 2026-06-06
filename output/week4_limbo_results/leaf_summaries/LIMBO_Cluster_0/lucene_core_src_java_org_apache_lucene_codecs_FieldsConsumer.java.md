licenses this file to You under the Apache License, Version 2.0
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

public class FieldsConsumer {
    private static final int MAX_LINE_LENGTH = 1024;

    public static void main(String[] args) throws FileNotFoundException, IOException {
        File file = new File("lucene.core.src.java.org.apache.lucene.codecs.FieldsConsumer.java");
        FileReader reader = new FileReader(file);
        List<String> lines = new ArrayList<String>();
        while ((line = reader.readLine()) != null) {
            lines.add(line);
        }
        reader.close();
        System.out.println("File title: " + file.getAbsoluteFile());
        System.out.println("Key functionality: FieldsConsumer");
        System.out.println("Core logic:")
        for (String line : lines) {
            if (line.length() > MAX_LINE_LENGTH) {
                System.out.println(line.substring(0, MAX_LINE_LENGTH));
            } else {
                System.out.println(line);
            }
        }
        System.out.println("Inputs and outputs:")
        for (String line : lines) {
            if (line.startsWith("public static void main(String[] args)") || line.startsWith("public static void main(String[] args) throws FileNotFoundException, IOException")) {
                System.out.println(line);
            }
        }
        System.out.println("Internal and external dependencies:")
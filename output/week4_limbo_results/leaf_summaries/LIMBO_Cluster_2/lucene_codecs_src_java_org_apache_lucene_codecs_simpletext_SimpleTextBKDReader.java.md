* this work for additional information regarding copyright ownership.
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

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SimpleTextBKDReader implements BKDReader {

    private static final int BUFFER_SIZE = 1024;

    public static void main(String[] args) throws IOException {
        try {
            FileInputStream fstream = new FileInputStream("lucene.codecs.src.java.org.apache.lucene.codecs.simpletext.SimpleTextBKDReader.java");
            BKDReader bkdr = new BKDReader(fstream);
            bkdr.read();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static class SimpleTextBKDReader {

        private final String fileName;
        private final List<String> lines;
        private final List<String> lines2;

        public SimpleTextBKDReader(FileInputStream fstream) throws IOException {
            this.fileName = fstream.getAbsoluteFile();
            lines = new ArrayList<String>();
            lines2 = new ArrayList<String>();
            try {
                while (true) {
                    String line = readLine();
                    if (line == null) {
                        break;
                    }
                    lines.add(line);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        public void
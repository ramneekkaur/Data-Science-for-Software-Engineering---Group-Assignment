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

public class SimpleTextFieldsWriter implements Serializable {
    private final StringBuilder sb = new StringBuilder();
    private final int lineNumber = 0;

    public SimpleTextFieldsWriter(String fileName) throws IOException {
        try (FileInputStream fstream = new FileInputStream(fileName);
             DataInputStream in = new DataInputStream(fstream);
             BufferedInputStream bufferedInputStream = new BufferedInputStream(in);
             InputStreamReader isr = new InputStreamReader(bufferedInputStream);
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(isr, true))) {
            String line;
            while ((line = isr.readLine()) != null) {
                sb.append(line);
                lineNumber++;
            }
        }
    }

    public String toString() {
        return sb.toString();
    }

    public void write(String line) {
        sb.append(line);
        lineNumber++;
    }

    public int getLineNumber() {
        return lineNumber;
    }

    public static void main(String[] args) {
        SimpleTextFieldsWriter writer = new SimpleTextFieldsWriter("lucene/codecs/src/java/org/apache/lucene/codecs/simpletext/SimpleTextFieldsWriter.java");
        writer.write("This is a test line.");
        writer.write("This is another test line.");
        writer.write("This is a third test line.");
        System.out.println(writer.getLineNumber());
    }
}
```

```
1. File title: SimpleTextFieldsWriter
2. Key functionality: Writes text to a
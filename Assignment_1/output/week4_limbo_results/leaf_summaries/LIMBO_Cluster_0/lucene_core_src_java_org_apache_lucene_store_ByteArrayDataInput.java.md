file to You under the Apache License, Version 2.0
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

public class ByteArrayDataInput {
    public static void main(String[] args) {
        byte[] data = new byte[1024];
        try {
            FileInputStream fis = new FileInputStream("/tmp/data.bin");
            InputStreamReader isr = new InputStreamReader(fis);
            BufferedReader br = new BufferedReader(isr);
            String line = br.readLine();
            while (line != null) {
                String[] tokens = line.split(" ");
                int i = Integer.parseInt(tokens[0]);
                byte[] bytes = new byte[i];
                br.read(bytes);
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < bytes.length; j++) {
                    sb.append(Integer.toHexString(bytes[j]));
                }
                System.out.println(sb.toString());
                line = br.readLine();
            }
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
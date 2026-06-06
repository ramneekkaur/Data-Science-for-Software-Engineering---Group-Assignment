for additional information regarding copyright ownership.
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

public class SimpleTextCodec implements Serializable {

    private final StringBuilder sb;

    public SimpleTextCodec(StringBuilder sb) {
        this.sb = sb;
    }

    public void encode(String text) {
        sb.append(text);
    }

    public String decode(String text) {
        return sb.toString();
    }

    public static SimpleTextCodec decode(String text) {
        return new SimpleTextCodec(new StringBuilder(text));
    }

    public static SimpleTextCodec encode(String text) {
        return new SimpleTextCodec(new StringBuilder(text));
    }

    public static void main(String[] args) {
        System.out.println(encode("Hello World"));
        System.out.println(decode("Hello World"));
    }
}
```

```
1. File title: SimpleTextCodec
2. Key functionality: Encodes and decodes text
3. Core logic: Appends text to a StringBuilder
4. Inputs and outputs: String
5. Internal and external dependencies: None
6. Architectural role inside the cluster: Input/Output
7. Important classes/methods: encode, decode, decode(String), encode(String)
```

```
1. File title: lucene.codecs.src.java.org.apache.lucene.codecs.simpletext.SimpleTextCodec
2. Key functionality: Encodes and decodes text
3. Core logic: Appends text to a StringBuilder
4. Inputs and outputs: String
5. Internal and external dependencies: None
6. Architectural role inside the cluster: Input/Output
7
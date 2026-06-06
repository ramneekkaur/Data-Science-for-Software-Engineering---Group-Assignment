distributed with
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

public class SimpleTextStoredFieldsWriter implements Serializable {

    private final StringBuilder sb = new StringBuilder();

    public SimpleTextStoredFieldsWriter(StringBuilder sb) {
        this.sb = sb;
    }

    public void write(String key, String value) {
        sb.append(key).append("=").append(value);
    }

    public String toString() {
        return sb.toString();
    }

    public static void main(String[] args) {
        SimpleTextStoredFieldsWriter sf = new SimpleTextStoredFieldsWriter();
        sf.write("foo", "bar");
        System.out.println(sf);
    }
}
```

```
1. File title: SimpleTextStoredFieldsWriter
2. Key functionality: Writes key-value pairs to a StringBuilder
3. Core logic: Appends key-value pairs to the StringBuilder
4. Inputs and outputs: Key, value
5. Internal and external dependencies: None
6. Architectural role inside the cluster: Leaf node
7. Important classes/methods: None
```

```
1. File title: SimpleTextStoredFieldsWriter
2. Key functionality: Writes key-value pairs to a StringBuilder
3. Core logic: Appends key-value pairs to the StringBuilder
4. Inputs and outputs: Key, value
5. Internal and external dependencies: None
6. Architectural role inside the cluster: Leaf node
7. Important classes/methods: None
```

```
1. File title: SimpleTextStoredFieldsWriter
2. Key functionality: Writes key-value pairs to a
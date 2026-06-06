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

public class FSTDictionary {
    private final String[] keys;
    private final String[] values;
    private final int size;

    public FSTDictionary(int size) {
        this.size = size;
        keys = new String[size];
        values = new String[size];
    }

    public void add(String key, String value) {
        if (size == 0) {
            keys[0] = key;
            values[0] = value;
            size++;
        } else {
            int i = 0;
            while (i < size) {
                if (key.compareTo(keys[i]) < 0) {
                    keys[i + 1] = key;
                    values[i + 1] = value;
                    size++;
                    break;
                }
                i++;
            }
            if (i == size) {
                keys[size] = key;
                values[size] = value;
                size++;
            }
        }
    }

    public String get(String key) {
        int i = 0;
        while (i < size) {
            if (key.compareTo(keys[i]) == 0) {
                return values[i];
            }
            i++;
        }
        return null;
    }

    public String[] getKeys() {
        return keys;
    }

    public String[] getValues() {
        return values;
    }

    public int getSize() {
        return size;
    }
}
```

```
File title: org.apache.lucene.codecs.uniformsplit.FSTDictionary
Key functionality: A class for storing a set of key-value pairs.
Core logic: The add method
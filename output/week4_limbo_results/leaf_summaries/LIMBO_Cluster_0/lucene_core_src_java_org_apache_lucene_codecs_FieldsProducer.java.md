ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

public class FieldsProducer implements FieldsProducer {

    private final String[] fields;
    private final int[] fieldIndices;
    private final int fieldCount;

    public FieldsProducer(int fieldCount) {
        this.fieldCount = fieldCount;
        fields = new String[fieldCount];
        fieldIndices = new int[fieldCount];
        for (int i = 0; i < fieldCount; i++) {
            fields[i] = "field" + i;
            fieldIndices[i] = i;
        }
    }

    public void produce(Document document) {
        for (int i = 0; i < fieldCount; i++) {
            String field = fields[i];
            int fieldIndex = fieldIndices[i];
            document.setField(field, document.getField(fieldIndex));
        }
    }

    public int getFieldCount() {
        return fieldCount;
    }

    public String[] getFields() {
        return fields;
    }

    public int[] getFieldIndices() {
        return fieldIndices;
    }
}
```

```
1. File title: lucene.core.src.java.org.apache.lucene.codecs.FieldsProducer
2. Key functionality: Produces fields for a document
3. Core logic: Produces fields for a document
4. Inputs and outputs: Document, fields, field indices
5. Internal and external dependencies: Apache Lucene
6. Architectural role inside the cluster: Core component
7. Important classes/methods: produce, setField, getFieldCount, getFields, getFieldIndices
```

```
# Exercise 1:
# Write a Python function that takes a list of
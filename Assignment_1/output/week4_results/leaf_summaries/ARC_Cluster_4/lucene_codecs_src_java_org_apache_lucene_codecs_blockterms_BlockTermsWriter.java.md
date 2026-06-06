F licenses this file to You under the Apache License, Version 2.0
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

import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class BlockTermsWriter implements Serializable {

    private final String fileName;
    private final List<String> terms;

    public BlockTermsWriter(String fileName) {
        this.fileName = fileName;
        terms = new ArrayList<String>();
    }

    public void addTerm(String term) {
        terms.add(term);
    }

    public void write() throws IOException {
        try {
            FileWriter fw = new FileWriter(fileName);
            OutputStreamWriter osw = new OutputStreamWriter(fw);
            for (String term : terms) {
                osw.write(term);
                osw.write("\n");
            }
            osw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String toString() {
        return terms.toString();
    }
}
```

```java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under
* you under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

public class Terms {
    /**
     * The class that represents a term in a document.
     */
    private final String term;
    private final int frequency;

    /**
     * Constructs a new Term.
     *
     * @param term
     *            The term to represent.
     * @param frequency
     *            The number of times the term appears in the document.
     */
    public Term(String term, int frequency) {
        this.term = term;
        this.frequency = frequency;
    }

    /**
     * Returns the term.
     */
    public String getTerm() {
        return term;
    }

    /**
     * Returns the frequency.
     */
    public int getFrequency() {
        return frequency;
    }

    /**
     * Returns the term and frequency as a string.
     */
    public String toString() {
        return term + ": " + frequency;
    }

    /**
     * Returns the term and frequency as a JSON string.
     */
    public String toJSON() {
        return term + ": " + frequency;
    }
}
```

```
1. File title: lucene.core.src.java.org.apache.lucene.index.Terms
2. Key functionality: Represents a term in a document.
3. Core logic: The class that represents a term in a document.
4. Inputs and outputs: Takes a term and its frequency as input and returns a Term object.
5. Internal and external dependencies: No external dependencies.
6. Architectural role inside the cluster: Core component of the Lucene indexing system.
7. Important classes/methods: Term, toString, toJSON
```

```java
/*
 *
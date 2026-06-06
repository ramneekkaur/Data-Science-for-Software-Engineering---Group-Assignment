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

public class AlreadyClosedException extends Exception {
    private final String message;

    public AlreadyClosedException(String message) {
        this.message = message;
    }

    public AlreadyClosedException(String message, String... args) {
        this.message = message;
        this.args = args;
    }

    @Override
    public String toString() {
        return message;
    }

    @Override
    public String toString(String... args) {
        return message + args.length > 0 ? args.toString() : "";
    }
}
```

```java
/*
 * File title: AlreadyClosedException
 * Key functionality: Exception class for already closed files
 * Core logic: Inherits from Exception class and overrides toString() method
 * Inputs and outputs: None
 * Internal and external dependencies: Apache Commons Lang library
 * Architectural role inside the cluster: Exception class
 * Important classes/methods: toString()
 */
```

```java
/*
 * File title: AlreadyClosedException
 * Key functionality: Exception class for already closed files
 * Core logic: Inherits from Exception class and overrides toString() method
 * Inputs and outputs: None
 * Internal and external dependencies: Apache Commons Lang library
 * Architectural role inside the cluster: Exception class
 * Important classes/methods: toString()
 */
```

```java
/*
 * File title: AlreadyClosedException
 * Key functionality: Exception class for already closed files
 * Core logic: Inherits from Exception class and overrides toString() method
 * Inputs and outputs: None
 * Internal and external dependencies: Apache Commons Lang library
 * Architectural role inside the cluster: Exception class
 * Important classes/methods: toString()
 */
```
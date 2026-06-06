ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

package-info;

import java.util.HashMap;
import java.util.Map;

public class PackageInfo {

    private static final Map<String, String> INPUTS = new HashMap<>();
    private static final Map<String, String> OUTPUTS = new HashMap<>();
    private static final Map<String, String> DEPENDENCIES = new HashMap<>();
    private static final Map<String, String> ARCHITECTURAL_ROLE = new HashMap<>();
    private static final Map<String, String> IMPORTANT_CLASSES = new HashMap<>();

    public static void main(String[] args) {
        INPUTS.put("input1", "input1_description");
        INPUTS.put("input2", "input2_description");
        OUTPUTS.put("output1", "output1_description");
        OUTPUTS.put("output2", "output2_description");
        DEPENDENCIES.put("dependency1", "dependency1_description");
        DEPENDENCIES.put("dependency2", "dependency2_description");
        ARCHITECTURAL_ROLE.put("role1", "role1_description");
        ARCHITECTURAL_ROLE.put("role2", "role2_description");
        IMPORTANT_CLASSES.put("class1", "class1_description");
        IMPORTANT_CLASSES.put("class2", "class2_description");
    }
}
```

```
File title: package-info
Key functionality: Provides information about a package
Core logic: The package contains a static map of inputs, outputs, dependencies,
architectural
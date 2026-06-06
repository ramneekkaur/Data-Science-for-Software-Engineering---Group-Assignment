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

public class ImpactsEnum {
    public static final int IMPACT_NONE = 0;
    public static final int IMPACT_SUBSTANTIAL = 1;
    public static final int IMPACT_MODERATE = 2;
    public static final int IMPACT_LOW = 3;
    public static final int IMPACT_HIGH = 4;
    public static final int IMPACT_VERY_HIGH = 5;
    public static final int IMPACT_VERY_LOW = 6;
    public static final int IMPACT_UNKNOWN = 7;

    public static int getImpact(String name) {
        if (name.equals("NONE")) {
            return IMPACT_NONE;
        } else if (name.equals("SUBSTANTIAL")) {
            return IMPACT_SUBSTANTIAL;
        } else if (name.equals("MODERATE")) {
            return IMPACT_MODERATE;
        } else if (name.equals("LOW")) {
            return IMPACT_LOW;
        } else if (name.equals("HIGH")) {
            return IMPACT_HIGH;
        } else if (name.equals("VERY_HIGH")) {
            return IMPACT_VERY_HIGH;
        } else if (name.equals("VERY_LOW")) {
            return IMPACT_VERY_LOW;
        } else {
            return IMPACT_UNKNOWN;
        }
    }
}
```

```
File title: ImpactsEnum
Key functionality: A class that maps impact levels to their names
Core logic: A static method that returns the impact level for a given name
Inputs and outputs: None
Internal and external dependencies: None
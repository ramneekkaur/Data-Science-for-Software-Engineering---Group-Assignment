ASF licenses this file to You under the Apache License, Version 2.0
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

public class PackedInts {
    public static int[] pack(int[] ints) {
        int[] packed = new int[ints.length];
        int i = 0;
        for (int j = 0; j < ints.length; j++) {
            packed[j] = ints[j];
            if (j < ints.length - 1) {
                packed[j + 1] = packed[j] + ints[j + 1];
            }
        }
        return packed;
    }

    public static int[] unpack(int[] packed) {
        int[] ints = new int[packed.length];
        int i = 0;
        for (int j = 0; j < packed.length; j++) {
            ints[j] = packed[j];
            if (j < packed.length - 1) {
                ints[j + 1] = ints[j] + packed[j + 1];
            }
        }
        return ints;
    }
}
```
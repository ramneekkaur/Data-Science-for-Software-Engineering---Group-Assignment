You under the Apache License, Version 2.0
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

public class FixedBitSet {
    private final int size;
    private final int[] bits;

    public FixedBitSet(int size) {
        this.size = size;
        bits = new int[size];
    }

    public boolean contains(int i) {
        return (bits[i] == 1);
    }

    public void set(int i, boolean value) {
        bits[i] = value;
    }

    public void clear(int i) {
        bits[i] = 0;
    }

    public int get(int i) {
        return (bits[i] == 1);
    }

    public int getSize() {
        return size;
    }

    public int getBitCount(int i) {
        return (bits[i] == 1);
    }

    public int getBitCount() {
        int count = 0;
        for (int i = 0; i < size; i++) {
            if (bits[i] == 1) {
                count++;
            }
        }
        return count;
    }

    public int getBitCount() {
        int count = 0;
        for (int i = 0; i < size; i++) {
            if (bits[i] == 1) {
                count++;
            }
        }
        return count;
    }

    public int getBitCount() {
        int count = 0;
        for (int i = 0; i < size; i++) {
            if (bits[i] == 1) {
                count++;
            }
        }
        return count;
    }

    public int getBitCount() {
        int count = 0;
        for (int i = 0; i < size; i++) {
            if
.
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

public class HeapPointWriter implements HeapPointWriter {

    private final int[] points;
    private final int[] weights;
    private final int[] indices;

    public HeapPointWriter(int n) {
        points = new int[n];
        weights = new int[n];
        indices = new int[n];
        for (int i = 0; i < n; i++) {
            points[i] = i;
            weights[i] = 0;
            indices[i] = i;
        }
    }

    public void addPoint(int point, int weight) {
        int i = findIndex(point);
        if (i == -1) {
            points[n] = point;
            weights[n] = weight;
            indices[n] = n;
            n++;
        } else {
            points[i] = point;
            weights[i] = weight;
            indices[i] = n;
        }
    }

    public int findIndex(int point) {
        for (int i = 0; i < n; i++) {
            if (points[i] == point) {
                return i;
            }
        }
        return -1;
    }

    public int findWeight(int point) {
        int i = findIndex(point);
        if (i == -1) {
            return 0;
        } else {
            return weights[i];
        }
    }

    public int findIndexOfWeight(int weight) {
        for (int i = 0; i < n; i++) {
            if (weights[i] == weight) {
                return indices[i];
            }
        }
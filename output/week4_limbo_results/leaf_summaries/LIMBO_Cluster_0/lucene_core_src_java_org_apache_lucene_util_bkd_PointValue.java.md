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

public class PointValue {
    public static final int MAX_DISTANCE = 1000000000;
    public static final int MAX_DISTANCE_DELTA = 1000000000;
    public static final int MAX_DISTANCE_DELTA_DELTA = 1000000000;

    public static int distance(PointValue p1, PointValue p2) {
        int dx = p1.x - p2.x;
        int dy = p1.y - p2.y;
        return Math.sqrt(dx * dx + dy * dy);
    }

    public static int distance(PointValue p1, PointValue p2, int delta) {
        int dx = p1.x - p2.x;
        int dy = p1.y - p2.y;
        return Math.sqrt(dx * dx + dy * dy) <= delta ? delta : Math.sqrt(dx * dx + dy * dy);
    }

    public static int distance(PointValue p1, PointValue p2, int delta, int delta2) {
        int dx = p1.x - p2.x;
        int dy = p1.y - p2.y;
        return Math.sqrt(dx * dx + dy * dy) <= delta ? delta : Math.sqrt(dx * dx + dy * dy) <= delta2 ? delta2 : delta;
    }

    public static int distance(PointValue p1, PointValue p2, int delta, int delta2, int delta3) {
        int dx = p1.x - p2.x;
        int dy = p1.y - p2.y;
        return Math.sqrt(dx * dx + dy * dy) <= delta ? delta : Math.sqrt(dx
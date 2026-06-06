file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

public class PointsWriter implements Serializable {
    private final int width;
    private final int height;
    private final int x;
    private final int y;
    private final int x2;
    private final int y2;

    public PointsWriter(int width, int height, int x, int y, int x2, int y2) {
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
        this.x2 = x2;
        this.y2 = y2;
    }

    public void write(PointsWriter other) {
        this.x = other.x;
        this.y = other.y;
        this.x2 = other.x2;
        this.y2 = other.y2;
    }

    public void write(PointsWriter[] other) {
        for (PointsWriter other : other) {
            this.x = other.x;
            this.y = other.y;
            this.x2 = other.x2;
            this.y2 = other.y2;
        }
    }

    public void write(PointsWriter[] other) {
        for (PointsWriter other : other) {
            this.x = other.x;
            this.y = other.y;
            this.x2 = other.x2;
            this.y2 = other.y2;
        }
    }

    public void write(PointsWriter[] other) {
        for (PointsWriter other : other) {
            this.x = other.x;
            this.y = other.y;
            this.x2 = other.x2;
            this.y2 = other.y2;
        }
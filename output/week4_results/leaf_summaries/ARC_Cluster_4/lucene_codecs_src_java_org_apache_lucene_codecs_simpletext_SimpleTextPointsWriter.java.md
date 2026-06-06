F licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

public class SimpleTextPointsWriter implements Serializable {

    private final StringBuilder sb = new StringBuilder();

    public SimpleTextPointsWriter(StringBuilder sb) {
        this.sb = sb;
    }

    public void write(SimpleTextPoint point) {
        sb.append(point.getText());
        sb.append("\n");
    }

    public String toString() {
        return sb.toString();
    }

    public static SimpleTextPointsWriter fromString(String s) {
        return new SimpleTextPointsWriter(new StringBuilder(s));
    }

    public static SimpleTextPointsWriter fromFile(File file) {
        return new SimpleTextPointsWriter(new StringBuilder(file.toString()));
    }

    public static SimpleTextPointsWriter fromFile(String file) {
        return new SimpleTextPointsWriter(new StringBuilder(file));
    }

    public static SimpleTextPointsWriter fromFile(String file) {
        return new SimpleTextPointsWriter(new StringBuilder(file));
    }

    public static SimpleTextPointsWriter fromFile(String file) {
        return new SimpleTextPointsWriter(new StringBuilder(file));
    }

    public static SimpleTextPointsWriter fromFile(String file) {
        return new SimpleTextPointsWriter(new StringBuilder(file));
    }

    public static SimpleTextPointsWriter fromFile(String file) {
        return new SimpleTextPointsWriter(new StringBuilder(file));
    }

    public static SimpleTextPointsWriter fromFile(String file) {
        return new SimpleTextPointsWriter(new StringBuilder(file));
    }

    public static SimpleTextPointsWriter fromFile(String file) {
        return new SimpleTextPointsWriter(new StringBuilder(file));
    }
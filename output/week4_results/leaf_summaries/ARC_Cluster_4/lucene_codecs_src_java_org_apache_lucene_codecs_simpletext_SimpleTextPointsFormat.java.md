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

public class SimpleTextPointsFormat implements Serializable {

    private final String[] points;

    public SimpleTextPointsFormat(String[] points) {
        this.points = points;
    }

    public String toString() {
        return Arrays.toString(points);
    }

    public static SimpleTextPointsFormat fromString(String s) {
        return new SimpleTextPointsFormat(Arrays.asList(s.split("\\s*,\\s*")));
    }

    public static SimpleTextPointsFormat fromFile(File file) {
        return new SimpleTextPointsFormat(Files.readAllLines(file.toFile()));
    }

    public static SimpleTextPointsFormat fromStringList(List<String> s) {
        return new SimpleTextPointsFormat(s);
    }

    public static SimpleTextPointsFormat fromStringList(List<String> s) {
        return new SimpleTextPointsFormat(s);
    }

    public static SimpleTextPointsFormat fromStringList(List<String> s) {
        return new SimpleTextPointsFormat(s);
    }

    public static SimpleTextPointsFormat fromStringList(List<String> s) {
        return new SimpleTextPointsFormat(s);
    }

    public static SimpleTextPointsFormat fromStringList(List<String> s) {
        return new SimpleTextPointsFormat(s);
    }

    public static SimpleTextPointsFormat fromStringList(List<String> s) {
        return new SimpleTextPointsFormat(s);
    }

    public static SimpleTextPointsFormat fromStringList(List<String> s) {
        return new SimpleTextPointsFormat(s);
    }

    public static SimpleTextPointsFormat fromStringList(List<String> s) {
        return new SimpleTextPoints
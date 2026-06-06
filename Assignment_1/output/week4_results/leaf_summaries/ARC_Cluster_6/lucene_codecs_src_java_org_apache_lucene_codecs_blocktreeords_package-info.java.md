F licenses this file to You under the Apache License, Version 2.0
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

package-info;

import java.util.HashMap;
import java.util.Map;

public class PackageInfo {
    private Map<String, String> inputs = new HashMap<>();
    private Map<String, String> outputs = new HashMap<>();
    private Map<String, String> dependencies = new HashMap<>();
    private String title;
    private String description;
    private String version;
    private String author;
    private String maintainer;
    private String home;
    private String url;
    private String license;

    public PackageInfo(String title, String description, String version, String author, String maintainer, String home, String url, String license) {
        this.title = title;
        this.description = description;
        this.version = version;
        this.author = author;
        this.maintainer = maintainer;
        this.home = home;
        this.url = url;
        this.license = license;
    }

    public void addInput(String input) {
        this.inputs.put(input, "input");
    }

    public void addOutput(String output) {
        this.outputs.put(output, "output");
    }

    public void addDependency(String dependency) {
        this.dependencies.put(dependency, "dependency");
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public String getVersion() {
        return version;
    }

    public String getAuthor() {
        return author;
    }

    public String getMaintainer() {
        return maintainer;
    }

    public
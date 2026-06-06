licenses this file to You under the Apache License, Version 2.0
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

public class TrackingDirectoryWrapper {
    private final DirectoryDirectoryEntry directory;
    private final DirectoryDirectoryEntry[] directoryEntries;

    public TrackingDirectoryWrapper(DirectoryDirectoryEntry directory) {
        this.directory = directory;
        directoryEntries = new DirectoryDirectoryEntry[directory.getNumberOfEntries()];
        for (int i = 0; i < directory.getNumberOfEntries(); i++) {
            directoryEntries[i] = directory.getEntry(i);
        }
    }

    public void setDirectory(DirectoryDirectoryEntry directory) {
        this.directory = directory;
        directoryEntries = new DirectoryDirectoryEntry[directory.getNumberOfEntries()];
        for (int i = 0; i < directory.getNumberOfEntries(); i++) {
            directoryEntries[i] = directory.getEntry(i);
        }
    }

    public DirectoryDirectoryEntry getDirectoryEntry(int index) {
        return directoryEntries[index];
    }

    public int getNumberOfEntries() {
        return directory.getNumberOfEntries();
    }

    public int getNumberOfEntries() {
        return directory.getNumberOfEntries();
    }

    public int getNumberOfEntries() {
        return directory.getNumberOfEntries();
    }

    public int getNumberOfEntries() {
        return directory.getNumberOfEntries();
    }

    public int getNumberOfEntries() {
        return directory.getNumberOfEntries();
    }

    public int getNumberOfEntries() {
        return directory.getNumberOfEntries();
    }

    public int getNumberOfEntries() {
        return directory.getNumberOfEntries();
    }

    public int getNumber
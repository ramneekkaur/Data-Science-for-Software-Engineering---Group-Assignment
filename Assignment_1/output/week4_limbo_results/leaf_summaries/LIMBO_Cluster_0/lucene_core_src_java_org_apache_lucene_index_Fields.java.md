* you under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

public class Fields {
    /**
     * Fields is a class that implements the interface
     * @link java.io.File
     * @link java.io.FileInputStream
     * @link java.io.FileOutputStream
     * @link java.io.FileNotFoundException
     * @link java.io.IOException
     * @link java.io.File
     * @link java.io.FileInputStream
     * @link java.io.FileOutputStream
     * @link java.io.FileNotFoundException
     * @link java.io.IOException
     */
    public static final File file;
    public static final FileInputStream fileInputStream;
    public static final FileOutputStream fileOutputStream;
    public static final FileNotFoundException fileNotFoundException;
    public static final IOException ioException;

    /**
     * @param file
     * @param fileInputStream
     * @param fileOutputStream
     * @param fileNotFoundException
     * @param ioException
     */
    public static final Fields(File file, FileInputStream fileInputStream,
            FileOutputStream fileOutputStream, FileNotFoundException fileNotFoundException,
            IOException ioException) {
        this.file = file;
        this.fileInputStream = fileInputStream;
        this.fileOutputStream = fileOutputStream;
        this.fileNotFoundException = fileNotFoundException;
        this.ioException = ioException;
    }

    /**
     * @return the file
     */
    public static File getFile() {
        return file;
    }

    /**
     * @return the fileInputStream
     */
    public static FileInputStream getFileInputStream() {
        return fileInputStream;
    }

    /**
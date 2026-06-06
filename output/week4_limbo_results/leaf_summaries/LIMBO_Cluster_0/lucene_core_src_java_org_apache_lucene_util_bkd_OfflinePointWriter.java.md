* The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

public class OfflinePointWriter implements
    java.io.FileWriter {
    private static final int MAX_POINTS_PER_LINE = 100;
    private static final int MAX_POINTS_PER_FILE = 100000;

    private int points;
    private int pointsInFile;
    private int pointsInLine;
    private int lineNumber;
    private int fileNumber;
    private int fileSize;
    private int fileSizeInBytes;
    private int fileSizeInKiB;
    private int fileSizeInMiB;
    private int fileSizeInGiB;
    private int fileSizeInTiB;
    private int fileSizeInPiB;
    private int fileSizeInEiB;
    private int fileSizeInZiB;
    private int fileSizeInYiB;
    private int fileSizeInYoB;
    private int fileSizeInYob;
    private int fileSizeInYobInKiB;
    private int fileSizeInYobInMiB;
    private int fileSizeInYobInGiB;
    private int fileSizeInYobInTiB;
    private int fileSizeInYobInPiB;
    private int fileSizeInYobInEiB;
    private int fileSizeInYobInZiB;
    private int fileSizeInYobInYiB;
    private int fileSizeInYobInYoB;
    private int fileSizeInYobInYobInKiB;
    private int fileSizeInYobInYobInMiB;
    private int fileSizeInYobInYobInGiB;
    private int fileSizeInYobInYobInTiB;
    private int fileSizeInYob
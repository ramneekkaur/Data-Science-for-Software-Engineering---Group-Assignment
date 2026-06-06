distributed with
 * this work for additional information regarding copyright ownership.
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

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class FixedGapTermsIndexWriter implements Serializable {

    private final int blockSize;
    private final int gapSize;
    private final int blockCount;
    private final int gapCount;
    private final int blockStart;
    private final int gapStart;
    private final int blockEnd;
    private final int gapEnd;
    private final int blockCountInGap;
    private final int gapCountInGap;
    private final int blockStartInGap;
    private final int gapStartInGap;
    private final int blockEndInGap;
    private final int gapEndInGap;
    private final int blockCountInGapInGap;
    private final int gapCountInGapInGap;
    private final int blockStartInGapInGap;
    private final int gapStartInGapInGap;
    private final int blockEndInGapInGap;
    private final int gapEndInGapInGap;

    public FixedGapTermsIndexWriter(int blockSize, int gapSize) {
        this.blockSize = blockSize;
        this.gapSize = gapSize;
        blockCount = 0;
        gapCount = 0;
        blockStart = 0;
        gapStart = 0;
        blockEnd = 0;
        gapEnd = 0;
        blockCountInGap = 0;
        gapCountInGap = 0;
        blockStart
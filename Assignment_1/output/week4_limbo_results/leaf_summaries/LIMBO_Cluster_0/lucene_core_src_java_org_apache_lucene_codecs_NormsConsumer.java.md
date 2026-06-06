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

public class NormsConsumer {
    private final String[] normData;
    private final int normDataLength;
    private final int normDataIndex;

    public NormsConsumer(String[] normData) {
        this.normData = normData;
        this.normDataLength = normData.length;
        this.normDataIndex = 0;
    }

    public void consume() {
        while (normDataIndex < normDataLength) {
            String normDataItem = normData[normDataIndex];
            normDataIndex++;
            if (normDataItem.equals("<") && normDataIndex < normDataLength) {
                String nextNormDataItem = normData[normDataIndex];
                normDataIndex++;
                if (nextNormDataItem.equals(">") && normDataIndex < normDataLength) {
                    String nextNextNormDataItem = normData[normDataIndex];
                    normDataIndex++;
                    if (nextNextNormDataItem.equals("=")) {
                        String nextNextNextNormDataItem = normData[normDataIndex];
                        normDataIndex++;
                        if (nextNextNextNormDataItem.equals("<") && normDataIndex < normDataLength) {
                            String nextNextNextNextNormDataItem = normData[normDataIndex];
                            normDataIndex++;
                            if (nextNextNextNextNormDataItem.equals(">") && normDataIndex < normDataLength) {
                                String nextNextNextNextNextNormDataItem = normData[normDataIndex];
                                normDataIndex++;
                                if (nextNextNextNextNextNormDataItem.equals("=")) {
                                    String nextNextNextNextNextNormDataItem = normData[normDataIndex];
                                    normDataIndex++;
                                    if (nextNext
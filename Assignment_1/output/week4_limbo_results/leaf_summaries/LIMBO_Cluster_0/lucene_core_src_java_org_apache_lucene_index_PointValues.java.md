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

public class PointValues {
    public static void main(String[] args) {
        PointValues pv = new PointValues();
        pv.setPointValues(new PointValues() {
            public void setPointValues(PointValues pv2) {
                pv2.setPointValues(pv);
            }
        });
        System.out.println(pv.getPointValues());
    }

    private PointValues() {
        this.pointValues = new PointValues();
    }

    private PointValues(PointValues pv) {
        this.pointValues = pv;
    }

    private PointValues setPointValues(PointValues pv) {
        this.pointValues = pv;
        return this;
    }

    private PointValues getPointValues() {
        return this.pointValues;
    }

    private int count() {
        return this.pointValues.count();
    }

    private int sum() {
        return this.pointValues.sum();
    }

    private int mean() {
        return this.pointValues.mean();
    }

    private int median() {
        return this.pointValues.median();
    }

    private int mode() {
        return this.pointValues.mode();
    }

    private int variance() {
        return this.pointValues.variance();
    }

    private int standardDeviation() {
        return this.pointValues.standardDeviation();
    }

    private int skewness() {
        return this.pointValues.skewness();
    }

    private int kurtosis() {
        return this.pointValues.kurtosis();
    }

    private int skewness() {
        return this.pointValues.skewness
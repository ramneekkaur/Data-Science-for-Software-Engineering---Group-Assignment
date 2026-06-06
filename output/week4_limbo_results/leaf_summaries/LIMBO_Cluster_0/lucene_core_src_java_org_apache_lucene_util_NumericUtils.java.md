file to You under the Apache License, Version 2.0
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

public class NumericUtils {
    public static double log10(double x) {
        return Math.log(x) / Math.log(10.0);
    }

    public static double log2(double x) {
        return Math.log(x) / Math.log(2.0);
    }

    public static double log1p(double x) {
        return Math.log(1.0 + x);
    }

    public static double log1p2(double x) {
        return Math.log(1.0 + x) + Math.log(2.0);
    }

    public static double log1p3(double x) {
        return Math.log(1.0 + x) + Math.log(3.0);
    }

    public static double log1p4(double x) {
        return Math.log(1.0 + x) + Math.log(4.0);
    }

    public static double log1p5(double x) {
        return Math.log(1.0 + x) + Math.log(5.0);
    }

    public static double log1p6(double x) {
        return Math.log(1.0 + x) + Math.log(6.0);
    }

    public static double log1p7(double x) {
        return Math.log(1.0 + x) + Math.log(7.0);
    }

    public static double log1p8(double x) {
        return Math.log(1.0 + x) + Math.log(8.0);
    }

    public static double log1p9(double x) {
        return Math.log(1.0 + x) + Math.log(9
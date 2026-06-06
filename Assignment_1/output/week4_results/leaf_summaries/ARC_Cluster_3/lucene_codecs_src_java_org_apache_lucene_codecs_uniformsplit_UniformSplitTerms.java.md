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

public class UniformSplitTerms implements
    java.io.FileInputStream {
    
    private static final int INPUT_SIZE = 1024;
    
    private static final int INPUT_SIZE_IN_BYTES = INPUT_SIZE * 8;
    
    private static final int INPUT_SIZE_IN_KILOBYTES = INPUT_SIZE / 1024;
    
    private static final int INPUT_SIZE_IN_MEGABYTES = INPUT_SIZE / 1024 / 1024;
    
    private static final int INPUT_SIZE_IN_GIGABYTES = INPUT_SIZE / 1024 / 1024 / 1024;
    
    private static final int INPUT_SIZE_IN_TERABYTES = INPUT_SIZE / 1024 / 1024 / 1024 / 1024;
    
    private static final int INPUT_SIZE_IN_PYTHON_BYTES = INPUT_SIZE;
    
    private static final int INPUT_SIZE_IN_PYTHON_KILOBYTES = INPUT_SIZE / 1024;
    
    private static final int INPUT_SIZE_IN_PYTHON_MEGABYTES = INPUT_SIZE / 1024 / 1024;
    
    private static final int INPUT_SIZE_IN_PYTHON_GIGABYTES = INPUT_SIZE / 1024 / 1024 / 1024;
    
    private static final int INPUT_SIZE_IN_PYTHON_TERABYTES = INPUT_SIZE / 1024 / 1024 / 1024 / 1024;
    
    private static final int INPUT_SIZE_IN_PYTHON_TINYBYTES = INPUT_SIZE;
    
    private static final int
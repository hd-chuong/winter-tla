# TLA+ Visualisation

## Installation

### Step 1. Clone this repository
~~~
git clone https://github.com/hd-chuong/winter-tla.git
~~~
### Step 2. Install Python
Ensure you have Python 3 installed in your computer. Python is needed to host a minimal REST Server. The demo needs a server because otherwise, the JSON loading component does not work.

### Step 3. Start up the Python simple Server

From your Terminal / PowerShell
~~~
python -m http.server 7999
~~~

### Step 4. Access the vis demo

From your browser

Viewing the graph-view
~~~
http://localhost:7999/graphview.html
~~~


Viewing the matrix-view
~~~
http://localhost:7999/matrixview.html
~~~

## Usage

There is an option to upload datasets into either graph view or matrix view. The datasets are stored in `datasets` folder

**Note**: While the `matrixview` is stable and can handle all sample datasets, the `graphview` only handles `datasets/dataset1-graph-and-matrix.json`. Loading other datasets into `graphview` will cause run-time error. This is a bug and needs to be fixed in the next iterations.
# python-GICP
A python wrapper for the C++ implementation of GICP 

Installation: 
-------------

Compile the GICP C++ library in GICP/cppSource according to the instructions in GICP/cppSource/Readme.md. 
For Linux, you will need to have libann (>1.1.1) installed in system path. 
For other OSs, install libann from [here](https://www.cs.umd.edu/~mount/ANN/) and modify line 6 of Makefile in GICP/cppSource "CXXFLAGS += -O3 -I/usr/include/ANN" 
to include the installed libann include files.

Usage:
------

Example usage scripts are provided in algoScripts. The basic usage is to use the function runGICP from GICPCore.gicpWrapper.

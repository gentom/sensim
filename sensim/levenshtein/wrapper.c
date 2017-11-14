#include "Python.h"

extern int levenshtein(const char*, const char*);

PyObject* levenshtein(PyObject* self, PyObject* args){
    const char* str1 = NULL;
    const char* str2 = NULL;
    int result;
    if(!PyArg_ParseTuple(args, "ss", &str1, &str2)){
        return NULL;
    }else{
        result = levenshtein(str1, str2);
        return Py_BuildValue("i", result);
    }
}

static PyMethodDef levenshteinmethods[] = {
  {"levenshtein", levenshtein, METH_VARARGS},
  {NULL},
};
 
 
void initlevenshtein(){
  Py_InitModule("Levenshtein", levenshteinmethods);
}
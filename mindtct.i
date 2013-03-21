%module mindtct
%{
extern int extract_xyt(char* image_file, char* minutiae_file);
%}
extern int extract_xyt(char* image_file, char* minutiae_file);

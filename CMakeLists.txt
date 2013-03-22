cmake_minimum_required (VERSION 2.6)
project (mindtct)
include_directories("/usr/include/nbis" "/usr/java/default/include"
	"/usr/java/default/include/linux" .)
link_directories(/usr/lib64/nbis)
FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})
SWIG_ADD_MODULE(libmindtct java mindtct.i mindtct.c)
SWIG_LINK_LIBRARIES(libmindtct mindtct image an2k openjpeg ihead jpegb jpegl
	wsq png fet ioutil util m z)
install(FILES libmindtct.so DESTINATION usr/lib64)
install(FILES mindtct.jar DESTINATION usr/share/java)


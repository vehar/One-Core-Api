set_cpp(WITH_RUNTIME)

add_definitions(-D_WIN32_WINNT=0x600)

include_directories(${REACTOS_SOURCE_DIR}/sdk/include)
include_directories(${REACTOS_SOURCE_DIR}/sdk/include/lib/atl)
include_directories(${REACTOS_SOURCE_DIR}/sdk/include/psdk)
include_directories(${REACTOS_SOURCE_DIR}/sdk/include/reactos/wine)
include_directories(${REACTOS_SOURCE_DIR}/dll/wrappers/dependencies/propsys)
include_directories(${REACTOS_SOURCE_DIR}/dll/wrappers/dependencies/shellbase)
spec2def(shell32_wrapper_new.dll shell32_wrapper_new.spec)

list(APPEND SOURCE
	classes.c
	iconcache.c
    main.c
	misc.c
	path.c
	pidl.c
	shellitem.c
	shellpath.c
	shlmenu.c
	shlview_cmenu.c
	unimplemented.c
	version.rc
    ${CMAKE_CURRENT_BINARY_DIR}/shell32_wrapper_new_stubs.c
    ${CMAKE_CURRENT_BINARY_DIR}/shell32_wrapper_new.def)

	
add_library(shell32_wrapper_new SHARED ${SOURCE})

set_module_type(shell32_wrapper_new win32dll)
target_link_libraries(shell32_wrapper_new wine uuid)
add_importlibs(shell32_wrapper_new advapi32 msvcrt user32 kernel32 ntdll shellbase shellnew shlwapi secur32 ole32 netapi32 rpcrt4 propsys comctl32 userenv gdi32 browseui)
add_dependencies(shell32 shdocvw_v1)
add_cd_file(TARGET shell32_wrapper_new DESTINATION reactos/system32 FOR all)

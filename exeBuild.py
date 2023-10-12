from cx_Freeze import setup, Executable

 # Add any additional packages or modules that your program depends on
build_options = {
    'packages': [],
    'excludes': [],
    'include_files': ['presets.txt', 'products.json']
}
executables = [
    Executable('tkinterGUI.py', base=None)
]
setup(
    name='SystemetSorteraren',
    version='1.0',
    description='Sorterar systemets produkter APK samt filtrerar efter dina kriterier',
    options={'build_exe': build_options},
    executables=executables
)

import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(name="Old Snakes",

                options = {
                            "build_exe" :
                            {
                                "packages" : ["pygame"],
                                "include_files" : ["Apple.png", "Snakehead.png"]

                            }

                },
                version = "2.0.38",
                description = "Old Snake Game by Subin Khullar (c) 2021",
                executables = executables
                )

#python setup.py build
#python setup.py bdist_msi
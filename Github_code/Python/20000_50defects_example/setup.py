from setuptools import setup, Extension
from Cython.Build import cythonize
# 定义扩展模块
extensions = [
    Extension(
        "my_module",  # 模块的名称
        sources=["my_module.pyx"],  # Cython 文件的源代码
        extra_compile_args=["-O2", "-m64"],  # 添加编译选项（64 位）
    ),
]

setup(
    # ext_modules=cythonize("my_module.pyx"),
    # extra_compile_args=['-arch', 'x86_64'],  # 设置为 64 位 保证编译结果是可执行的64位文件，因为python解释器为64位，要确保输出的DLL文件也是64位
    name="my_module",
    ext_modules=cythonize(extensions)
)

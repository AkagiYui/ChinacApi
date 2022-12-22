import pathlib

from setuptools import find_packages, setup

long_description = pathlib.Path('README.md').read_text(encoding='utf-8')  # 读取README.md文件内容
setup(
    name='chinacapi',  # 包名
    version='0.1.1',  # 版本号
    author='AkagiYui',  # 作者
    author_email='akagiyui@yeah.net',  # 作者邮箱
    description='A chinac api operator',  # 描述
    long_description=long_description,  # 将 README.md 内容作为长描述
    long_description_content_type='text/markdown',
    url='https://github.com/AkagiYui/ChinacApi',  # 项目地址

    packages=find_packages('src'),  # 在此目录中寻找软件包
    package_dir={'': 'src'},
    classifiers=[  # PyPI分类
        'Development Status :: 4 - Beta',  # 开发进度
        'Programming Language :: Python :: 3.7',  # 编程语言，可以支持多种
        'Intended Audience :: Developers',  # 目标用户，可以有多个
        'License :: OSI Approved :: MIT License',  # 开源许可证
        'Operating System :: OS Independent'  # 支持系统，这里是不受限于操作系统的
    ],
    python_requires='>=3.7',  # Python版本限制
    install_requires=[]  # 安装依赖
)
